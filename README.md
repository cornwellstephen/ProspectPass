# ProspectPass
## Team
* Olivia Johnston: oliviaj@princeton.edu
* Samuel Arnesen: sarnesen@princeton.edu
* Stephen Cornwell: sjc4@princeton.edu (team leader)
* Yijia Liang: yijial@princeton.edu 
## Overview
We proposing an electronic pass system to manage entrance into the Princeton eating clubs. This application, which we are calling “ProspectPass,” will enable students to easily transfer their passes to their friends while also allowing clubs to gather accurate statistics about club attendance.  ProspectPass will therefore not only be more convenient than the existing paper pass system is for students, but also an important tool for clubs seeking to create a safe and enjoyable experience. 
## Requirements and Target Audience
### Problem
Currently, students use paper passes (printed on small business cards) to enter clubs. Students typically contact a friend who is the member of the club to inquire about a pass, and then meet in person to receive the pass. On a typical night out, students will present the physical pass, which should have the student’s name as well as the club member’s name written, as well as their student identification card. The bouncers check the pass with the student’s ID, and then allow entry.

We identify several problems with the current pass method. 

First, the use of a physical pass unnecessarily wastes resources - clubs spend thousands of dollars per year printing out color-coded paper passes which end up being discarded around campus if a student decides not to use it.

Second, physical distribution of passes has been criticized by students as tedious and occasionally awkward. This is especially the case if a non-member student is securing a pass from a mutual friend, or a friend of a friend. Even for members, the existing system can also be problematic if they are unable to pick up physical passes during the specific distribution hours.

Third, under the existing paper pass system, clubs have no means of tracking who or how many people enter the club. After the bouncer collects the pass, they do not record any additional information, making it difficult for the club to precisely manage how many people enter the club on a given night. 

Fourth, students tend to secure multiple passes for one night out, which can lead to lost passes. Given that most (it not all) students have a smartphone that can access the internet, it makes more sense to have a centralized solution for passes.
### Existing Solutions
There are no existing solutions to the problems of the paper pass system. With the paper pass system being in use for at least a decade, institutional inertia rather than any inherent benefit explains why the system is still in place despite its flaws. 
### Intended Users
We intend for Princeton students to use the application, specifically when they want to go to eating clubs that require passes on nights out.

We expect the platform to be used extensively if adopted by clubs needing passes, especially on nights out with heavy traffic (Thursdays, Saturdays).
### Key Benefits
The main benefit of ProspectPass is the electronic centralization of the pass system.

For students:
Access all of their passes in one place
Transfer and receive passes immediately

For bouncers:
View passes and IDs without need for collection

For clubs:
Keep track of how many students have activated and entered a club
Know exactly who has a pass to enter the club
Prevent re-entry since passes will expire at a designated time after activation
Reduce costs of printing physical passes and environmental pollution
Easier management of pass distribution
## Functionality
When students are transferring passes or receiving passes, we anticipate this will likely be done on a desktop app.

In general, when deciding to use electronic passes, users will likely consider several factors:
Ease of use - the current paper system is already quite intuitive and easy to use. ProspectPass therefore will need to be at least as easy to use in order to be competitive.
Reliability - the paper system, unless you lose the paper pass, is quite reliable. You give the pass to the bouncer and proceed with your night. Clubs and students are unlikely to adopt our system unless these same standards are met.

At a minimum then, ProspectPass’s functionality must meet those conditions.

In particular, we anticipate that most usage, on a night out, will come from mobile devices meaning that the mobile experience must be seamless. Accessing and transferring passes must also be fast and intuitive for students and so we intend on designing the system to require as few clicks as possible. From the bouncer's point of view, a successful implementation is one that allows a bouncer to quickly verify the validity of the pass so the pass must be clear to read and easily distinguishable from a screenshot. 

We thus aim to develop a webapp that will service the following use cases:

Example Use Cases

Club Member:
* Receives however many allotted passes clubs distribute
* Transfers passes to whomever they would like

Generic Student:
* Receives passes from club member
* Transfers pass to whomever they would like
* Has a centralized location for all their passes on their phone, organized by date and club
* Activates passes with the click of a button before heading to the eating club
* Shows pass to bouncer along with ID

Club Officer:
* Sets pass color and how long a pass remains activated
* Distributes passes to club members
* Tracks number of activated passes as a metric for how many students have entered (or are planning on entering) the club
