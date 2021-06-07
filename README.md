# Capstone Project Bangkit 2021 Group CAP-0233 (Cloud Computing Path)
## Architecture Design for Backend in Cloud with Firebase and Google Cloud Platform
![alt txt](https://github.com/raihanarfi12-lab/gcp-babgkit-b21-cap0233/blob/main/architecture.png)
### Workflow:
1. Mobile send information (register,login, comment, or post the job vacancy)
2. For saving entity (profile data, posting data,status), it will be saved at Realtime Database, but email and password will be saved in Firebase authentication for account authentication 
3. Event (update,delete,creat of comment) in Realtime Database will trigger Cloud Function to run source code
4. Cloud Function download ML model in Cloud Storage, then ML model classify the comment as hate and abusive or toxic status or not
5. File in Cloud Storage loaded to Cloud Function
6. If there is abusive and toxic comment, it will update data in Realtime Database and stream status to Bigquery 
7. Mobile app request to get data from Realtime Database and Cloud Storage

## Requirements:
1. Firebase Console
- Realtime Database
- Cloud Storage (extend into GCP automatically)
2. GCP Console
- GCP Project
- Service Account
- Cloud Function
- Bigquery

## Create Firebase Project (Firebase realtime database and Cloud Storage)
1. Open https://console.firebase.google.com
2. Click Add Project
3. Click bar in Enter Your Project Name. For integrated with GCP, you should enter GCP Project name
4. Slide toggle to not use Firebase Analytic and click project
5. In right side of Firebase console, you can click the service, then click get started for realtime database and cloud storage,ensure you keep realtime database and cloud storage link

For more information for Firebase, you can see the [documentation](https://firebase.google.com/docs)

## Make service account for Cloud Function
1. Open your GCP Project
2. Click Navigation > IAM & Admin > service accounts
3. Click Create Service Account
4. Enter name, then click create
5. For the testing,we set role owner for service account,select role > Basic > owner
6.  Click Done
7.  Create a new key as JSON for service account

## Create Cloud Storage
1. Open Home to GCP Dashboard > Navigate > Storage
2. Create Bucket
3. Enter name for bucket, it must unique, you can enter `[project-id]-bucket`for the name of bucket
4. Leave other default setting,Click Create

## Input ML file to Cloud Storage
1. Open powershell in GCP,ensure that cloud shell connect into your account and project
2. Clone this repository `git clone https://github.com/raihanarfi12-lab/gcp-babgkit-b21-cap0233.git`
3. To copy the ML file, you can copy this code
`cd babgkit-b21-cap0233`\
`gsutil cp tokenizer.pickle gs://[project-id]-bucket`\
`gsutil cp variables.data-00000-of-00001 gs://[project-id]-bucket`\
`gsutil cp variables.index gs://[project-id]-bucket`

## Create Bigquery Table
1. Open Home to GCP Dashboard > Navigate > Bigquery
2. Click Done for Welcoming in Bigquery UI
3. Click three-dot beside of your project ID,then create dataset
4. Enter 'jobstify' for dataset ID, and click create
5. Open dataset and Click Plus in the box symbol to create table
6. For table name, you can enter 'toxic_status'
7. For schema you can clik add field 3 times, then enter 'uid','full_name' and 'status' for the field
8. Click create table 

## Create Cloud Function
1. Open Home to GCP Dashboard > Navigate > Cloud Function
2. Create function
3. Choose Firebase Realtime Database as trigger
4. Input Firebase Realtime Database name
5. For databse path you can enter /Profile User/{push_id} and choose write for event type
6. Click Runtime, Build, and Connection setting
7. For Runtime service account, you can choose service account that you make
8. For Memory allocated, choose 4 GiB and choose 30 seconds for timeout, then click next
9. Open powershell editor, open gcp-babgkit-b21-cap0233 > main.py, you can edit name of [BUCKET-NAME] to bucket that have you made, then copy to Cloud Function
10. For runtime, you can choose Python 3.8
11. For entrypoint, keep default name of entrypoint, hello_rtdb. If you want to change, then change function name in main.py same with entrypoint
12. For requirements.txt, you can copy the the file from gcp-babgkit-b21-cap0233 > requirements.txt
13. Actually, key from service account downloaded automatically to your computer. Open the file with notepad,then copy the content of file. In Cloud Function, add file to deploy, give the filename "function.json"
14. Click Deploy to deploy Cloud Function \
\
NB: Sometimes, for deploy Cloud function, there is problem to load tensorflow. For that, you can try to deploy cloud function again

## Testing
1. Input with key name and status, then you can give random name and hate,abusive, and toxic status in Indonesia Language in Firebase Realtime Database
2. Check the logs in function, there will be output similiar like [0.56787], if prediction[0][0]>0.5, it will be toxic comment. Under of that, there will be information about status
3. After that, go to Bigquery, and in query editor type this query to get the table ``SELECT * FROM `[project-id].jobstify.toxic_status` `` \
NB: Table need  time to update content, if you directly check the table through project-id > jobstify > toxic_status, so we recommend to use query editor to look quickly the content,if you need simulation for testing, you can checkout [link](https://youtu.be/DhMnEhAfDd8)

## Monitoring
1. Open Home to GCP Dashboard > Navigate > Monitoring > Dashboard
2. Create Dashboard
3. Choose resource type and metrics for dashboard and choose stacked bar for the shape of graph
In our project we choose:
- Resource type : Firebase Realtime Database, Metric : Database Load
- Resource type : Cloud Function, Metric : Cloud Function
- Resource type : GCS Bucket , Metric : Received Bytes
- Resource type : Bigquery, Metric : Uploaded rows

