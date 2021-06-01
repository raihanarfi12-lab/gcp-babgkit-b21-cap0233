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

