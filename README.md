# Uni Board  

A messaging board for students and academics
## Contents  
 - [Features](#Features)
 - [TODO](#TODO)
 - [Tools](#Tools)
 - [Operation](#Operation)
   - [Github](##Github)
   - [Local Server](##Server)
     - [Commands](###Commands) 

## Features
 - Home Page (default)
 - Account/Profile System
 - Message Board
 - Quiz Completion/Creation
 - LeaderBoards

## TODO
- Main: Create framework [head,nav] (Neil) 
- Database: script for generating "dummy" data (George)
- Login System: Create a the Login & Signup pages (Will W)
- Message_Board: Basic functionality [post, reply] (Tu)

## Tools    
 - python-django | 3.1.7
 - bootstrap     | v5.0.0-beta2

## Operation  
### Github  
 - PLEASE: create a new branch for your development work  
 - DO NOT: push directly to the master branch  
### Server  
This is the CL argument for the server  
`python manage.py < command >`  
#### Commands
Run these commands when you add/remove/move any django files  
`makemigrations`  
`migrate`  

Starts the server in the current terminal  
`runserver`  

Create a super user that can be access in the "/admin" page  
`createsuperuser`  

Creates a new "app" (kinda like a module) in the src directory  
`startapp < appname >`  

Load an admin user with username and password "admin", and loads in example posts  
`loaddata test_data.json`  

Run unit tests  
`test`  
### IBM Cloud
Build container image with docker, upload to IBM cloud registry, then deploy container to Kubernetes.  
This can all be done in one step using the ibm_reimage bash script found under uni-board. Ensure you are logged in to IBM Cloud (`ibmcloud login`), then run `./ibm_reimage`. The external IP used to access the site will be displayed after the ./ibm_reimage script is run. To access the site, visit [external IP]:8080 in your browser.
