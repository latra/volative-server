### Users
The project involves different types of users, each with their specific roles and permissions to ensure smooth operation and division of responsibilities.


#### Admins
Admins have the highest level of access within the system. They are responsible for managing the overall structure, including creating new projects and assigning moderators. To avoid security or organizational issues, this role can only be assigned locally on the server, meaning it’s not accessible remotely or through a web interface.

##### Key Responsabilities
- Create and delete projects
- Assign or remove moderators for individual projects
- Mantain the overall system integrity

#### Moderators (Mods)
Moderators are responsible for managing individual projects. They are assigned by Admins on a per-project basis. Their role includes overseeing the workflow, managing voices (recordings), and interacting with collaborators by delegating tasks.
##### Key Responsabilities
- Register and manage voice recordings associated with the project.
- Create and send work batches to collaborators.
- Monitor and track the progress of ongoing tasks.
- Add or remove collaborators from the project as needed.


#### Collaborators
Collaborators are the workers who perform the actual tasks within the project. They are assigned specific jobs by the moderators and are responsible for downloading voice data, processing or working with it, and uploading the results.
##### Key Responsabilities
- Receive work orders from moderators.
- Download voice data related to tasks.
- Perform the required work (e.g., annotation, transcription, etc.).
- Upload completed work.
 
---
### Models

#### User
This model represents all users in the system. Each user has credentials and may or may not have admin privileges.- Username
##### Attrubutes
- **Username**: A unique identifier for each user.
- **Password**: A secure password for authentication.
- **Email**: Contact information for notifications or account management.
- **isAdmin**: A boolean field indicating if the user has Admin privileges (true or false).

#### Project
A project is the central entity that coordinates all tasks, data, and participants. It is created and managed by Admins, while Moderators handle its day-to-day operations.

##### Attrubutes

- **Name**: The project’s unique name for easy identification.
- **Description**: A brief overview of the project, its goals, and scope.
- **Work Batches**: Collections of tasks (jobs) that collaborators work on.
- **Voices**: Audio files (or similar) registered and processed during the project.
- **Moderators**: The moderators responsible for managing the project.
- **Collaborators**: The users assigned to complete jobs within the project.


#### Work Batch
A work batch groups together multiple jobs related to the project. Each batch can contain several tasks that are to be completed by collaborators. Moderators create these batches and distribute them among collaborators.

##### Attrubutes

- **Project**: The project to which this batch belongs.
- **Batch** ID: A unique identifier for the work batch.
- **Model**: The structure or framework that defines the specific tasks in the batch.
- **Jobs**: The individual tasks within the batch that will be handled by collaborators.

#### Job
A job is a single task assigned to a collaborator within a work batch. Each job represents a specific transcription.

##### Attrubutes
- **Work Batch**: The work batch that contains this job.
- **Job ID**: A unique identifier for the job.
- **Status**: The current status of the job (e.g., pending, in progress, completed).
- **Voice**: The specific voice file or data associated with this job.
- **Text**: Any related text or instructions that accompany the job.



### API Basic Functions
- [x] Login
- [x] Register
- [x] Create projects
- [ ] Delete projects
- [x] Assign project mods
- [x] Assign project collaborators
- [ ] Remove collaborators and mods
- [ ] Register voices
- [ ] Remove voices
- [ ] Send a Work Batch
- [ ] Check Work Batch status
- [ ] Check Job status
