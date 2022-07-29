# DevOps project for QA


#### README.md under construction. Will be updated soon...


### Branch "feature-2" is the most recent branch.

## Use cases:
In the following section I present the use case diagram based on the initial requirements identified. The diagram has been used to get a bird's eye view of GF FLASK and provide a visualisation of the external and internal factors influencing the system, in addition to requirement gathering purposes of successive iterations and optimisations of GF FLASK, following A/B testing.
<img width="941" alt="image" src="https://user-images.githubusercontent.com/56838325/181687042-740ce418-b1e8-4938-8aec-57ed271a86dd.png">

<img width="961" alt="image" src="https://user-images.githubusercontent.com/56838325/181705304-d0eaeab0-9caa-4711-88d1-7787e28214e1.png">
<img width="1381" alt="image" src="https://user-images.githubusercontent.com/56838325/181705353-2b3dccbd-e021-4c9e-bfbb-c42278a48235.png">
<img width="968" alt="image" src="https://user-images.githubusercontent.com/56838325/181707021-e85648b5-c42d-4ba4-8641-2be8d708a97e.png">
<img width="1348" alt="image" src="https://user-images.githubusercontent.com/56838325/181705849-6f6f9c72-a995-49c5-99ad-aa2f502e9a91.png">
<img width="967" alt="image" src="https://user-images.githubusercontent.com/56838325/181707978-744fb8ab-a375-401d-a644-aaf0992513d9.png">
<img width="1315" alt="image" src="https://user-images.githubusercontent.com/56838325/181707720-184305fc-4475-4430-a8bb-5ed170aa6f7b.png">
<img width="959" alt="image" src="https://user-images.githubusercontent.com/56838325/181708931-a824e0fe-2dc7-4a5d-991b-19a595dd7825.png">
<img width="1267" alt="image" src="https://user-images.githubusercontent.com/56838325/181708491-76678db4-426e-4896-9144-3a0bf312e231.png">
<img width="966" alt="image" src="https://user-images.githubusercontent.com/56838325/181710190-f2c62d6b-c5ab-4881-872a-aa1be93f4536.png">
<img width="1255" alt="image" src="https://user-images.githubusercontent.com/56838325/181709937-46fc6dd1-c5e0-4d39-a082-708ad3a7448f.png">

# Application video
Below is the video describing the application till feature-2. It also includes mention about how the application has been deployed on the Jenkins pipeline and on Docker Swarm: 
https://drive.google.com/drive/folders/1gDfpDnDfW4baTHSugsVtHZDcIRwRToIk
I have included a document with the console output from Jenkins.
Docker images can be checked on hub:
<img width="980" alt="image" src="https://user-images.githubusercontent.com/56838325/181712053-6fea499a-7eba-44ca-addd-2468527ab57c.png">


## User stories 
I have worked in differnet iterations to implement product features, based on their values, for a better understanding of why users might want a certain functionality.

<img width="1416" alt="image" src="https://user-images.githubusercontent.com/56838325/181702730-5845e0b2-7e58-4c7f-a17a-1aab8f84004a.png">

## Project Management 
Ongoing for feature-3.
<img width="1131" alt="image" src="https://user-images.githubusercontent.com/56838325/181702622-1d8c9164-8e87-44c4-848c-5108d209a4a2.png">

## Risk management
In the risk assessment table I first identify risks and consider whether they are event driven, evolving, technical or non-technical, on top of examining the risk triggers in advance. In the second column I assess the impacts of the risks following the equation:
* Risk impact = risk likelihood x  risk consequences
<img width="454" alt="image" src="https://user-images.githubusercontent.com/56838325/181714482-26ea2c8f-9776-44a4-9910-ed13eabdec7c.png">
With the given numbers I derive a relative measure to be able to then rank the risks to focus on the ‘critical’ ones first, following RAG grading. The third column is a list of possible approaches to the risks: either by avoidance, by deflection (or transfer) or by contingency. 
<img width="1001" alt="image" src="https://user-images.githubusercontent.com/56838325/181717087-8dcf052f-7c0d-4ca7-94a3-985811687b15.png">


## Technology Readiness Levels (TRL)
Software projects are challenging due to the complexity of the product, nonlinear scaling of resources, measurement of project and product, initial uncertainty in project and product scope, and knowledge gained as a project evolves. Technology Readiness Levels (TRL) are a type of measurement system used to assess the maturity level of a particular technology.  By the completion of the project, STSTEM is at TRL 4, see table below:
<img width="1014" alt="image" src="https://user-images.githubusercontent.com/56838325/181717264-9f63e572-8380-4307-a049-5240f1646cf1.png">

## ORM relationship: many-to-many
<img width="815" alt="image" src="https://user-images.githubusercontent.com/56838325/181731961-7db85938-91c7-4a68-a4b7-ea6130b3613d.png">

## Refactoring
The code has been refactored in several occasions. Below are some of the examples:
