# Capstone Project Bangkit 2021 Group CAP-0233 (Cloud Computing Path)
## Architecture Design for Backend in Cloud with Firebase and Google Cloud Platform
![alt txt](https://github.com/raihanarfi12-lab/gcp-babgkit-b21-cap0233/blob/main/architecture.png)
### Workflow:
1. Mobile send information (register,login, comment, or post the job vacancy)
2. For saving entity (profile data, posting data,status), it will be saved at Realtime Database, but email and password will be saved in Firebase authentication for account authentication 
3. For saving image (profile image, post image), it will be saved at Cloud Storage
4. Event (update,delete,creat of comment) in Realtime Database will trigger Cloud Function to run source code
5. Cloud Function download ML model in Cloud Storage, then ML model classify the comment as hate and abusive or toxic status or not
6. Cloud Function will stream detected toxic status to Bigquery 
7. Mobile app request to get data from Realtime Database and Cloud Storage

## Requirements:
1. Firebase Console
- Realtime Database
- Cloud Storage (extend into GCP automatically)
2. GCP Console
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
6. Click Done

## Create Cloud Storage
1. Open Home to GCP Dashboard > Navigate > Storage
2. Create Bucket
3. Enter name for bucket, it must unique, you can enter `[project-id]-bucket`for the name of bucket

## Input ML file to Cloud Storage
1. Open powershell in GCP,ensure that cloud shell connect into your account and project
2. Clone this repository `git clone https://github.com/raihanarfi12-lab/gcp-babgkit-b21-cap0233.git`
3. To copy the ML file, you can copy this code
`cd babgkit-b21-cap0233`
`gsutil cp tokenizer.pickle gs://[project-id]-bucket`
`gsutil cp variables.data-00000-of-00001 gs://[project-id]-bucket`
`gsutil cp variables.index gs://[project-id]-bucket`

## Create Bigquery Table
1. Open Home to GCP Dashboard > Navigate > Bigquery
2. Click Done for Welcoming in Bigquery UI
3. Click three-dot beside of your project ID,then create dataset
4. Enter 'jobstify' for dataset ID, and click create
5. Open dataset and Click Plus in the box symbol to create table
6. For table name, you can enter 'toxic_status'
7. For schema you can clik add field 2 times, then enter 'user_id' and 'status' for the field
8. Click create table 

## Create Cloud Function
1. Open Home to GCP Dashboard > Navigate > Cloud Function
2. Create function
3. Choose Firebase Realtime Database as trigger
4. Input Firebase Realtime Database name
5. For databse path you can enter jobstify/{push_id} and choose write for event type
6. Click Runtime, Build, and Connection setting
7. For Runtime service account, you can choose service account that you make
8. For Memory allocated, choose 4 GiB and timeout, choose 30 seconds, then click next
9. Open powershell editor, open gcp-babgkit-b21-cap0233 > main.py, you can edit name of [BUCKET-NAME] to bucket that have you made, then copy to Cloud Function
10.For requirements.txt, you can copy the the file from gcp-babgkit-b21-cap0233 > requirements.txt
11.Click Deploy to deploy cloud function 


