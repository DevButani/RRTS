# RRTS
Road Repair Tracking Software

A Python-based system software for registering complaints, allocating wokforce and resources, and reviewing the status of complaints.
Includes Tkinter-based UI for four users.

### USE CASES:

Clerk Page:
<ul>
  <li>Read user inputs from the clerk and update the database.</li>
</ul>

Supervisor Page:
<ul>
<li>Display complaint report and read severity, traffic, resources, etc. while updating the database.</li>
<li>Display schedule report and update status of repair on the database.</li>
</ul>

City Admin Page:
<ul>
<li>Display and update available resource counts on the database.</li>
<li>Approve and Authorize new users into the system.</li>
</ul>

Mayor Page:
<ul>
<li>Display resource utilization statistics for a given time period as input by the user.</li>
<li>Display repairs statistics such as number and type of repairs, and repairs outstanding at any point of time.</li>
</ul>

Scheduler:
<ul>
  <li>Retrieve appropriate information from the database and use it to schedule pending repairs according to the available resources.</li>
</ul>

### FEATURES:
<ul>
<li>Separate personalized storage space for each city</li>
<li>Customizable options for book-keeping activities</li>
<li>Real time updates</li>
<li>Access management functionality</li>
<li>Security: Password encryption, Restricted database file access</li>
</ul>

### TECH STACK:
<ul>
<li>Front-end: Tkinter (Python), Pillow for images</li>
<li>Back-end: Python</li>
<li>Modules used: os, re, pandas, time, datetime</li>
<li>Database: PyDrive module (Python) with Google Drive APIs to access csv files stored on the cloud.</li>
</ul>
