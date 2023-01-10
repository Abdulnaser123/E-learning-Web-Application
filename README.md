# e-Learn web application:Edu4All:
Welcome to edu4All system, an online platform that allows students and teachers to connect and interact with each other through courses and learning materials.

This platform is built with
### frontend
ReactJS library, Bootstrap, SweetAlert styles, Css3, Html5
### backend
Django and MySQL

## System Features :

### Teachers
##### create teacher account
##### Create course
##### Create chapters to the course
##### Create course materials
##### Create assignments and assign them to students
##### Create multiple questions quiz and assign it to students
##### View student quiz result
##### Chatting with students


### Students
##### Create student account
##### Enroll in courses
##### Explore the course vedios
##### Download course materials
##### Rate the course
##### Receive assignment notifications from the teacher
##### Take quizz and submit it
##### Chatting with teacher
###### In the beginning, we will talk about the registration process in the system for the teacher. Here, the teacher enters all his data, including qualifications and skills.
![image](https://user-images.githubusercontent.com/108693961/211422578-94694b4e-6e49-4701-8293-9cd68050f7c6.png)
###### The teacher will receive the account verification code to ensure the authenticity of the registration process. Note here that I used a number that can be obtained not from the mail, but from the database to enter it.
![image](https://user-images.githubusercontent.com/108693961/211424064-ca07b371-ef82-4cb5-bb74-bb4ab4c895dd.png)
###### Here, the process of logging in for the teacher takes place in the same form for the student to access his control panel in the system
![image](https://user-images.githubusercontent.com/108693961/211425614-383485f8-75b0-4f49-9ed8-91a9a6e9ffdf.png)
###### teacher's dashboard, which is filled with his statistical cards, as shown
![image](https://user-images.githubusercontent.com/108693961/211425682-ac49e7a4-f631-4b7d-941f-9e5337e30b82.png)

###### Here the list of courses for the teacher appears and all the data related to it, such as the number of students in each course, modifying the course data, adding a chapter to the course, assign a quiz, adding the material to the course, and finally deleting it

![image](https://user-images.githubusercontent.com/108693961/211425647-6b195f72-e02a-4d32-ada3-28d9739a031b.png)


###### Here, the course list can be modified as shown, as initially all data related to the course is fetched from the database and the possibility of modification is made.


![image](https://user-images.githubusercontent.com/108693961/211425722-63007557-1d27-46fd-9780-a79c2c0cad1c.png)


###### teacher can add a chapter for a specific course
![image](https://user-images.githubusercontent.com/108693961/211425747-746ef667-4018-4231-b0cc-0f7f66d44d93.png)

###### In this list, all the assignments appear for all the courses, and whether they are assigned to the course or not. If they are not assigned, they can be assigned, and if they are assigned, the list of students who have solved this short exam can be shown

![image](https://user-images.githubusercontent.com/108693961/211425779-eed9bd50-2566-4a37-acb2-63587b39a971.png)

###### list of students who solved the quiz and show the result by the teacher. As shown, the student got a zero result because he neglected the study

![image](https://user-images.githubusercontent.com/108693961/211425844-37786c1b-f3a0-494d-8209-4bc5195a1727.png)

###### list of materials for a specific course appears, and it is possible to delete it. Here we used the SweetAlert as a warning before deletion.

![image](https://user-images.githubusercontent.com/108693961/211425884-b96d78b8-e41f-4ba2-9d13-bdc2e0f6a452.png)


###### the list of show quizzes, but to modify it, delete it, or add a question to it, as shown

![image](https://user-images.githubusercontent.com/108693961/211425954-f0f168b6-5483-4ea9-b981-eda30303328d.png)

###### Add a question to a specific quiz and confirm it
![image](https://user-images.githubusercontent.com/108693961/211425979-81f13533-70a8-4cf9-8d09-488256fafc69.png)


###### And here is the most interesting part of the project, where the possibility of correspondence between the teacher and the student

![image](https://user-images.githubusercontent.com/108693961/211426093-aac92d74-bd12-48e0-a824-0cc4e793cb95.png)

###### Here is the teacher's details page

![image](https://user-images.githubusercontent.com/108693961/211426144-f976d1d1-9b8f-4a7d-b855-f5a1212f190e.png)


###### the main page of the site appears, where all the courses uploaded to the system or the most popular courses can be shown, and this is according to the rating and the number of participants in the course, and also the list of teachers appears on the site

![image](https://user-images.githubusercontent.com/108693961/211426180-545b9098-4965-4a6f-800f-248e053d3744.png)

###### Searching for a specific course, is not required to complete the course name, perhaps part of its name, and it can also be searched for through the techniques used in this course.

![image](https://user-images.githubusercontent.com/108693961/211426220-583fc6d4-2bdd-47ba-b18c-4f34ad8fd3ba.png)

###### Course data page. If the student is logged into his account, he can enroll to the course as shown 

![image](https://user-images.githubusercontent.com/108693961/211426289-7a8f0d87-07c4-433f-b681-1bb45b84ca3e.png)

###### Here, the enrollment process has been completed in the course, pointing to this swetAlert shown at the top of the page on the right

![image](https://user-images.githubusercontent.com/108693961/211426340-30d8c337-63ed-4b9a-b68b-1f4ef4f09743.png)

###### After the enrollment process in the course, you will see the that you are now enrolling, and the course can be rated out of 5, and a text note will be sent from the student as shown.

![image](https://user-images.githubusercontent.com/108693961/211426463-a90ee2ab-bb50-4d4d-a6f0-3fee1bc56c6b.png)

###### Explore the course's videos, by clicking on the video icon, a popup will appear containing the video link from YouTube for the student to view

![image](https://user-images.githubusercontent.com/108693961/211427467-6e7276ed-53f8-4830-98b4-f9c379590664.png)

###### The teacher's data, all his courses, the total number of students enrolled in the courses, and the teacher's average rating

![image](https://user-images.githubusercontent.com/108693961/211426509-eddb1222-b627-430d-9e36-17c26e97ddbd.png)

###### Statistics cards for students
![image](https://user-images.githubusercontent.com/108693961/211426547-8859ab6f-0164-4825-b05d-d12aa21f3126.png)

###### List of courses in which the student is registered, the name of the instructor for each course appears, the quiz list related to the courses, and communication with the course instructor

![image](https://user-images.githubusercontent.com/108693961/211426757-90c6b5e2-0f41-4256-8b6c-435bec17e879.png)

###### All materials for a specific course and can be downloaded from the student

![image](https://user-images.githubusercontent.com/108693961/211426792-73ffa9c6-488f-4dcc-9280-d352041990a2.png)

###### List of quizzes related to a specific course and whether they are solved or not

![image](https://user-images.githubusercontent.com/108693961/211426584-cc3fcae1-278a-495a-bf5b-2398661dbaf5.png)


###### The FAQs page, as all the questions and answers presented here are taken from the database, and the person responsible for adding them is the system admin.
![image](https://user-images.githubusercontent.com/108693961/211426610-f0109149-fa99-4f14-9a30-5d39e46ca0ec.png)



