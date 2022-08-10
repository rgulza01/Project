# DevOps project for QA - GF FLASK
### by: Radia Gulzan
A monolithic web application to help celiac people form a community where they can share gluten free recipes and stories about their gluten free life. Technologies utilised include: Azure database, Azure virtual machine, Jenkins, Docker, Docker-compose, Docker-Swarm, NGINX.

## Use cases:
In the following section I present the use case diagram based on the initial requirements identified. The diagram has been used to get a bird's eye view of GF FLASK and provide a visualisation of the external and internal factors influencing the system, in addition to requirement gathering purposes of successive iterations and optimisations of GF FLASK, following A/B testing.
<img width="941" alt="image" src="https://user-images.githubusercontent.com/56838325/181687042-740ce418-b1e8-4938-8aec-57ed271a86dd.png">

<img width="955" alt="image" src="https://user-images.githubusercontent.com/56838325/181744544-1d44692f-c236-411d-93f5-e2445d7dce5a.png">
<img width="1421" alt="image" src="https://user-images.githubusercontent.com/56838325/182073380-cfdbe14a-bfa0-4b4c-86f2-830b909d926d.png">

<img width="967" alt="image" src="https://user-images.githubusercontent.com/56838325/181707978-744fb8ab-a375-401d-a644-aaf0992513d9.png">
<img width="1396" alt="image" src="https://user-images.githubusercontent.com/56838325/182073610-ca2b6515-49b1-444d-b141-af8160372e8e.png">

<img width="959" alt="image" src="https://user-images.githubusercontent.com/56838325/181708931-a824e0fe-2dc7-4a5d-991b-19a595dd7825.png">
<img width="1267" alt="image" src="https://user-images.githubusercontent.com/56838325/181708491-76678db4-426e-4896-9144-3a0bf312e231.png">
<img width="966" alt="image" src="https://user-images.githubusercontent.com/56838325/181710190-f2c62d6b-c5ab-4881-872a-aa1be93f4536.png">
<img width="1328" alt="image" src="https://user-images.githubusercontent.com/56838325/182071796-03736582-303e-4c11-b27b-68afdf897a4d.png">
<img width="965" alt="image" src="https://user-images.githubusercontent.com/56838325/182072333-a84b6dba-fcb1-490a-9c7b-0f405e42cdab.png">
<img width="1057" alt="image" src="https://user-images.githubusercontent.com/56838325/182072247-c0be814a-94b0-46a9-8b81-2c5e655222f3.png">

# Application video
Below is the video describing the application. It's a 7 minutes video that starts with the app as it was in feature-2 but ends by introducing components of feature-3. It also includes mention about how the application has been deployed on the Jenkins pipeline and on Docker Swarm: 
https://drive.google.com/drive/folders/1gDfpDnDfW4baTHSugsVtHZDcIRwRToIk
I have included a document with the console output from Jenkins.
Docker images can be checked on hub:
<img width="980" alt="image" src="https://user-images.githubusercontent.com/56838325/181712053-6fea499a-7eba-44ca-addd-2468527ab57c.png">


## User stories 
I have worked in various iterations to implement product features, based on their values, for a better understanding of why users might want a certain functionality.

<img width="1416" alt="image" src="https://user-images.githubusercontent.com/56838325/181702730-5845e0b2-7e58-4c7f-a17a-1aab8f84004a.png">

## Project Management 
Ongoing for feature-3.
<img width="1131" alt="image" src="https://user-images.githubusercontent.com/56838325/181702622-1d8c9164-8e87-44c4-848c-5108d209a4a2.png">

## Risk management
In the risk assessment table I first identify risks and consider whether they are event driven, evolving, technical or non-technical, on top of examining the risk triggers in advance. In the second column I assess the impacts of the risks following the equation:
* Risk impact = risk likelihood x  risk consequences
<img width="454" alt="image" src="https://user-images.githubusercontent.com/56838325/181714482-26ea2c8f-9776-44a4-9910-ed13eabdec7c.png">
With the given numbers I derive a relative measure to be able to then rank the risks to focus on the ‘critical’ ones first, following RAG grading. The third column is a list of possible approaches to the risks: either by avoidance, by deflection (or transfer) or by contingency. 
<img width="847" alt="image" src="https://user-images.githubusercontent.com/56838325/181747103-fae998c5-8418-47b6-8a92-f2b304f2ae17.png">

## Technology Readiness Levels (TRL)
Software projects are challenging due to the complexity of the product, nonlinear scaling of resources, measurement of project and product, initial uncertainty in project and product scope, and knowledge gained as a project evolves. Technology Readiness Levels (TRL) are a type of measurement system used to assess the maturity level of a particular technology.  By the completion of the project, GF FLASK is at TRL 4, see table below:
<img width="1014" alt="image" src="https://user-images.githubusercontent.com/56838325/181717264-9f63e572-8380-4307-a049-5240f1646cf1.png">

## ORM relationship: many-to-many
User will be used as reader as well. Therefore a post can have many readers and a user can post/read many posts.
<img width="815" alt="image" src="https://user-images.githubusercontent.com/56838325/181731961-7db85938-91c7-4a68-a4b7-ea6130b3613d.png">

# Refactoring
The code has been refactored in several occasions. Below are some of the examples:
### - Refactoring the layout of the html template
* from 
<img width="731" alt="image" src="https://user-images.githubusercontent.com/56838325/181733314-7c6cfffe-0ae0-4519-8284-73f331618414.png">

* to
<img width="839" alt="image" src="https://user-images.githubusercontent.com/56838325/181733487-baabf3c2-3bed-4143-b49b-087b1158a973.png">

### - Refactoring database relationship from one-to-one to many-to-many
* from this view till feature-2
<img width="499" alt="image" src="https://user-images.githubusercontent.com/56838325/181737567-974dc77d-5417-4e0b-ba43-b11a2ae749c6.png">
* to this in feature-3
<img width="519" alt="image" src="https://user-images.githubusercontent.com/56838325/181737620-4873e705-af7d-4e96-a620-2472f691a7bf.png">

### - Refactoring database relationship many-to-many
I had suddently started getting the warning: 
create.py:13: SAWarning: relationship 'Post.users' will copy column user.id to column user_post.user_id, which conflicts with relationship(s): 'Post.user' (copies user.id to user_post.user_id), 'User.posts' (copies user.id to user_post.user_id). If this is not the intention, consider if these relationships should be linked with back_populates, or if viewonly=True should be applied to one or more if they are read-only. For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the columns that should be written towards.   To silence this warning, add the parameter 'overlaps="posts,user"' to the 'Post.users' relationship. (Background on this error at: https://sqlalche.me/e/14/qzyx). 

So I refactored the code from:

<img width="608" alt="image" src="https://user-images.githubusercontent.com/56838325/182046927-21051f12-ab55-4d84-96f1-165f879d57ef.png">
to:

<img width="887" alt="image" src="https://user-images.githubusercontent.com/56838325/182046945-d9697c4f-35d5-4b79-8137-421e223adee8.png">

### - Refactoring nginx for the container that was not running despite the SUCCESS shown in the Jenkins pipeline

<img width="1250" alt="image" src="https://user-images.githubusercontent.com/56838325/181735538-ca3412f3-7293-4ead-9410-fc03df9af05e.png">

### - Refactoring tests for higher unit testing coverage
* from 
<img width="829" alt="image" src="https://user-images.githubusercontent.com/56838325/181736150-63606910-6fdd-4594-98ed-01964581236b.png">

* to
<img width="1107" alt="image" src="https://user-images.githubusercontent.com/56838325/181736004-392e5c83-c48c-4ade-80b4-11527102a33e.png">

### - Refactoring Jenkins Pipeline from docker compose to adding  docker swarm
* from having the docker compose stage
<img width="535" alt="image" src="https://user-images.githubusercontent.com/56838325/181734231-3067cfdb-6678-430c-ba4e-f44ab2146729.png">

* to making a single step for swarm 
<img width="755" alt="image" src="https://user-images.githubusercontent.com/56838325/181747797-2d5aae31-c022-4d24-a9dd-53eb4c067985.png">

The pipeline therefore ensures that the application setup is done including the configurations and necessariry installations from requirements.txt . The final step is to build the docker-compose, push the image on dockerhub and deploy the docker stack. The video includes more discussion and demonstration of the pipeline, among other things. 

### - Refactoring Dockerfile, docker-compose and Jenkinsfile after adding Jenkins credentials for implementing an Azure database

<img width="309" alt="image" src="https://user-images.githubusercontent.com/56838325/181735353-6d72aa05-597d-4ff0-83b0-510773b81d4e.png">
<img width="381" alt="image" src="https://user-images.githubusercontent.com/56838325/181735044-32cf4c2a-132b-44f0-84f9-5b999047b2c2.png">
<img width="319" alt="image" src="https://user-images.githubusercontent.com/56838325/181735246-74704776-9269-416e-8ded-41069036bb99.png">

### - Refactoring dashabord with search bar working and by adding the functionality to view the posts by each user
* in feature-2
<img width="1398" alt="image" src="https://user-images.githubusercontent.com/56838325/182073935-1f506a3c-8c2b-4e0f-851e-7b6afe12f11f.png">

* in feature-3
<img width="1434" alt="image" src="https://user-images.githubusercontent.com/56838325/182947897-8123ddcf-bedd-4811-8f43-bd108e205ade.png">
<img width="1418" alt="image" src="https://user-images.githubusercontent.com/56838325/182071143-29eb5421-ddeb-435a-845d-99f973fcb090.png">

### - Refactoring for hashing password, added now during registration, to ease the login functionality:
<img width="1027" alt="image" src="https://user-images.githubusercontent.com/56838325/182071249-9fc4fe8e-f157-4434-bd86-5760b2162ab8.png">
<img width="925" alt="image" src="https://user-images.githubusercontent.com/56838325/182071346-6f8e969a-013b-47b4-a154-592cb5c25396.png">

# Acknowledgements
I would like to express my most sincere appreciation to Earl Gray - DevOps specialisation trainer - for pushing the boundaries of my capabilities, positively contributing to the project's growth since the idea's inception.

I would also like to mention that the beautiful teal coloured html templates have been adopted from Gurupreeth Singh. 

I had the fortune of learning how to use opensource technologies such as Bootstrap to complete the rest of the application and creating UI templates with Flask-WTF by following lessons from Earl and from John from Codecademy.com 

I would finally like to point out that the reddit flask community r/flask is a great platform to intereact with other Flask developers.
