# ProspectPass
ProspectPass is an electronic pass system to manage entrance into the Princeton eating clubs. It enables students to easily transfer their passes to their friends while also allowing clubs to gather accurate statistics about club attendance.  ProspectPass is not only be more convenient than the existing paper pass system is for students, but also an important tool for clubs seeking to create a safe and enjoyable experience. 

## Team
* Olivia Johnston: oliviaj@princeton.edu
* Samuel Arnesen: sarnesen@princeton.edu
* Stephen Cornwell: sjc4@princeton.edu **(team leader)**
* Yijia Liang: yijial@princeton.edu
### Advisor
* Lance Goodridge: lanceg@princeton.edu

## Major Milestones
### Project Prototype: April 1
* CAS login impelemented for all users.
* Pass interface done. This entails the design of the pass and should read from a set JSON object, not the backend of the site.
* Basic sending infrastructure done. This will not send pass data between users, but will allow for some data to be sent from one user to another.
* Setup of super-user functionality. We need to lay the groundwork for superusers who are able to distribute passes to club members.
* Front end views are working. While not fully fleshed out, the interface should be funcitonal, although not connected fully to a backend system.
* Backend fully fleshed out in Django.
### Alpha Test: Sunday April 22
* Flesh out some of the bugs from the project prototype.
* Wire in the frontend views to the backend. Frontend system should read pass data from the database.
* Sending functionality should be connected to the pass system, allowing for transfer of passes.
* Pass design should be completed. This should mainly entail details like blinking and color choices.
* Add superuser functionality. Superusers should be able to distribute passes, set pass colors, set an expiration time if they so desire, etc.
### Beta Test: Sunday April 29
* Mostly, our beta test has similar requirements as the Alpha Test.
* Refine pass design in light of feedback from bouncers.
* Refine student interface in light of feedback from student users.
* Fix bugs that emerge through the process of putting the system through small scale tests.
* Stretch: Allow club members to determine whether their pass should be transferable once given to a student.
### Submission: May 13
* Finalize code and fix bugs remaining after Beta Test.
