# Capstone Project Bangkit 2021 Group CAP-0233 (Cloud Computing Path)
## Architecture Design for Backend in Cloud with Firebase and Google Cloud Platform
![alt txt](https://github.com/raihanarfi12-lab/gcp-babgkit-b21-cap0233/blob/main/architecture.png)
### Workflow:
1. Mobile send information (register,login, comment, or post the job vacancy)
2. For saving entity (profile data, posting data,status), it will be saved at Realtime Database
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
