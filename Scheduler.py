from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
from time import *
from datetime import *
from functools import cmp_to_key

# get authorization
gauth = GoogleAuth()
gauth.LoadCredentialsFile("credentials.json")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("credentials.json")

drive = GoogleDrive(gauth)

database_folder = '1kkvHF8YdAhyspTZqbeVKEz6XNEWwP_ij'
database_file = {
    "Resources": '1gDMbXVq0Lgj5LGoMVZlA8EtUd1dwPnwN',  
    "Andheri": '1QxjK4TdW8UHn8-ySdrlViXDIoWjX0Dnk', 
    "Bandra": '1r2ShjWn8S972IoRO5RZsD3OIBNLrU4Kc', 
    "Bhandup": '19ap2PvVO-ERGGj_LijoPLPvVLMGsUK-B', 
    "Bhuleshwar": '1Fa8t7XZfQQpIkoEUYpoDS7W-2Nguu3sx',
    "Borivali": '1xU_K7YBWLrMhm3z1gVWN_2syxY6oKg_1', 
    "Breach_Candy": '17Urykk8jvu4ppquA4dUfD9e0KY0DYM6h', 
    "Chembur": '1bIg9f7hHX-Na-F3mFe4xJmpcu0_JAbYT',
    "Colaba": '1jefLO7aHB92MuTsP2dM8YQBLmxxGp9wh', 
    "Dadar": '1hHEff7HppBFaXzeT9VoIgefubAJpyZv-',
    "Dharavi": '1_HKagDggHWGCQy7BiuL8FAu14GAixAXQ',
    "Fort": '1UrOCR1udJfVb4NCVdXDSIAvPcjVZNM68', 
    "Ghatkopar": '1XgQpvBTwArD3CeCN-vJ3ATW0UIpUuB4b', 
    "Goregaon": '11zVyjMPiwEg0c0mGifEDVyWG27ZIjDec', 
    "Juhu": '1XesefIFase9Ff7O76XiyyGmb_5nwUxdU', 
    "Kandivali": '1DiODeKtPY_LgcNGASlsHPdPNakuQ7ULJ',    
    "Malabar_Hill": '1TIRFDh8ujIGhfbgrt-l0ARG8TpDtAgh-', 
    "Malad": '1OrtbmxDfTOMteImOk6mtsCS6FOjr7jpD', 
    "Mulund": '1MGCZ0u99lJbXTEWdC9H0b3AXF5c-KhrB', 
    "Pali_Hill": '1kGQwq6FGQKg0hh9VUMAUNpLK1WANUsGe', 
    "Powai": '15s3VZW_cU782COa3laqHjLN_w_yLbjnl', 
    "Tardeo": '1oO0nx7KPFfUcYv2ZUuAe2Qf6nLVWJzKf',
    "Versova": '1Q6HyxfhwhtGcEN75UI75fJ8xdNRHlP4R',  
    "Worli": '1tLzhEuwRzfTq2vqRgquwG62KoZoP8uSn', 
}

localities_list = ["Andheri","Bandra","Bhandup","Bhuleshwar","Borivali","Breach_Candy","Chembur","Colaba","Dadar","Dharavi","Fort","Ghatkopar","Goregaon","Juhu","Kandivali","Malabar_Hill","Malad","Mulund","Pali_Hill","Powai","Tardeo","Versova","Worli"]

# map categories to values
severity_map = {"Critical": 3, "Severe": 2, "Moderate": 1, "Mild": 0}
traffic_map = {"Extreme": 4, "Heavy": 3, "Medium": 2, "Light": 1, "Deserted": 0}
resources_list = ["Asphalt", "Bitumen", "Concrete", "Engineer", "Worker", "Machine Operator", "Bulldozer", "Road Roller", "Concrete Mixer", "Jackhammer"]

while True:
    current_date = date.today()
    current_time = datetime.now()

    # schedule tasks every 5 min
    sleep((5 - current_time.minute % 5)*60 - current_time.second)

    # get complaints
    complaints_df = pd.DataFrame(columns=['Locality','Street','Problem','Reporting Date','Severity','Traffic','Asphalt','Bitumen','Concrete','Bulldozer','Road Roller','Concrete Mixer','Jackhammer','Engineer','Worker','Machine Operator','Status','Completion Date'])
    for locality in localities_list:
        complaints_df = pd.concat([complaints_df,pd.read_csv('https://drive.google.com/uc?id='+database_file[locality])], ignore_index=True)

    # get resources
    resources_df = pd.read_csv('https://drive.google.com/uc?id='+database_file['Resources'])
    resources_available = {}
    resources_count = len(resources_df.index)
    for indx in range(resources_count):
        resources_available[resources_df['Name'][indx]] = resources_df['Units Available'][indx]

    # segregate pending and in-progress complaints
    pending_complaints_df = complaints_df[complaints_df['Status']=="Pending"]
    in_progress_tasks_df = complaints_df[complaints_df['Status']=="In Progress"]
    complaints_df.drop(complaints_df[complaints_df['Status']!="Completed"].index, inplace=True)
    pending_complaints_df.reset_index(inplace=True, drop=True)
    in_progress_tasks_df.reset_index(inplace=True, drop=True)


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
    file_obj = drive.CreateFile({'parents': [{'id': database_folder}], 'id': database_file['Resources']})
    resources_df.to_csv('temp.csv', index=False)
    file_obj.SetContentFile(filename = 'temp.csv')
    file_obj.Upload()
    
    complaints_df = pd.concat([complaints_df,pending_complaints_df], ignore_index=True)
    complaints_df = pd.concat([complaints_df,in_progress_tasks_df], ignore_index=True)
    for locality in localities_list:
        file_obj = drive.CreateFile({'parents': [{'id': database_folder}], 'id': database_file[locality]})
        complaints_df[complaints_df['Locality']==locality.replace('_',' ')].to_csv('temp.csv', index=False)
        file_obj.SetContentFile(filename = 'temp.csv')
        file_obj.Upload()