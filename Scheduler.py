import pandas as pd
from datetime import *
from functools import cmp_to_key

# get complaints
complaints_file = "./Desktop/data.csv"
complaints_df = pd.read_csv(complaints_file)

# get resources
resources_file = "./Desktop/resources.csv"
resources_df = pd.read_csv(resources_file)

resources_available = {}
resources_count = len(resources_df.index)
for indx in range(resources_count):
    resources_available[resources_df['Name'][indx]] = resources_df['Units Available'][indx]

# segregate pending and in-progress complaints
pending_complaints_df = complaints_df[complaints_df['Status']=="Pending"]
in_progress_tasks_df = complaints_df[complaints_df['Status']=="In Progress"]
complaints_df.drop(complaints_df[complaints_df['Status']!="Completed"].index, inplace=True)
complaints_df.to_csv(complaints_file, index=False)
pending_complaints_df.reset_index(inplace=True, drop=True)
in_progress_tasks_df.reset_index(inplace=True, drop=True)

# map categories to values
current_date = date.today()
severity_map = {"Critical": 3, "Severe": 2, "Moderate": 1, "Mild": 0}
traffic_map = {"Extreme": 4, "Heavy": 3, "Medium": 2, "Light": 1, "Deserted": 0}
resources_list = ["Asphalt", "Bitumen", "Concrete", "Engineer", "Worker", "Machine Operator", "Bulldozer", "Road Roller", "Concrete Mixer", "Jackhammer"]

# create a list of score-bin number and resource-requirement coefficient for pending complaints
# score = 10*severity + 15*traffic + number of days elapsed since complaint was registered
# score-bin number = score/10 (creating bins of size 10 for score)
# resource-requirement coefficient = (total raw materials needed) + 10*(total personnel needed) + 100*(total machines needed)
pending_scheduler_score = []
pending_complaint_count = len(pending_complaints_df.index)
for indx in range(pending_complaint_count):
    score = 10*severity_map[pending_complaints_df['Severity'][indx]] + 15*traffic_map[pending_complaints_df['Traffic'][indx]] + (current_date - datetime.strptime(pending_complaints_df['Reporting Date'][indx], '%Y-%m-%d').date()).days
    resources_req = 0
    for i in range(len(resources_list)):
        resources_req += 10**(min(int(i/3),2)) * pending_complaints_df[resources_list[i]][indx]
    pending_scheduler_score.append((int(score/10),indx,resources_req))

# sort the list of pending complaints according to higher score-bin number and lower resource-requirement coefficients (for comparison within a bin)
def compare(item1, item2):
    if item1[0] > item2[0]:
        return -1
    elif item1[0] < item2[0]:
        return 1
    else: 
        return item1[2] - item2[2]
pending_scheduler_score = sorted(pending_scheduler_score, key=cmp_to_key(compare))

# create a list of score-bin number for in-progress tasks and sort in descending order
in_progress_scheduler_score = []
in_progress_task_count = len(in_progress_tasks_df.index)
for indx in range(in_progress_task_count):
    score = 10*severity_map[in_progress_tasks_df['Severity'][indx]] + 15*traffic_map[in_progress_tasks_df['Traffic'][indx]] + (datetime.strptime(in_progress_tasks_df['Completion Date'][indx], '%Y-%m-%d').date() - datetime.strptime(in_progress_tasks_df['Reporting Date'][indx], '%Y-%m-%d').date()).days
    in_progress_scheduler_score.append((int(score/10),indx))
in_progress_scheduler_score.sort(reverse=True)

# schedule the pending and in-progress tasks
# iterate over all pending complaints
# assign resources (if sufficient) to all in-progress tasks belonging to either the score-bin under consideration (to which the pending complaint belongs)
#  or its next bin (if insufficient resources then mark it as pending complaint, remove completion date)
# then assign resources (if sufficient) to the pending complaint under consideration
# change status of pending complaint to in-progress and assign completion date as current date (start date)
in_progress_index = 0
for item in pending_scheduler_score:
    while (in_progress_index < in_progress_task_count) and (in_progress_scheduler_score[in_progress_index][0] >= item[0] - 1):
        sufficient = True
        for resource in resources_list:
            if resources_available[resource] < in_progress_tasks_df[resource][in_progress_index]: 
                sufficient = False
                break
        if sufficient:
            for resource in resources_list:
                resources_available[resource] -= in_progress_tasks_df[resource][in_progress_index]
        else:
            in_progress_tasks_df.at[in_progress_index, 'Status'] = "Pending"
            in_progress_tasks_df.at[in_progress_index, 'Completion Date'] = pd.NA
        in_progress_index += 1

    sufficient = True
    for resource in resources_list:
        if resources_available[resource] < pending_complaints_df[resource][item[1]]: 
            sufficient = False
            break
    if sufficient:
        for resource in resources_list:
            resources_available[resource] -= pending_complaints_df[resource][item[1]]
        pending_complaints_df.at[item[1], 'Status'] = "In Progress"
        pending_complaints_df.at[item[1], 'Completion Date'] = str(current_date)

# assign resources (if sufficient) to all in-progress tasks not considered yet
while in_progress_index < in_progress_task_count:
    sufficient = True
    for resource in resources_list:
        if resources_available[resource] < in_progress_tasks_df[resource][in_progress_index]: 
            sufficient = False
            break
    if sufficient:
        for resource in resources_list:
            resources_available[resource] -= in_progress_tasks_df[resource][in_progress_index]
    else:
        in_progress_tasks_df.at[in_progress_index, 'Status'] = "Pending"
        in_progress_tasks_df.at[in_progress_index, 'Completion Date'] = pd.NA
    in_progress_index += 1

# update In-Use resource counts
for indx in range(resources_count):
    resources_df.at[indx, 'In Use'] = resources_df['Units Available'][indx] - resources_available[resources_df['Name'][indx]]

# push changes to the databases
resources_df.to_csv(resources_file, index=False)
pending_complaints_df.to_csv(complaints_file, mode='a', header=False, index=False)
in_progress_tasks_df.to_csv(complaints_file, mode='a', header=False, index=False)