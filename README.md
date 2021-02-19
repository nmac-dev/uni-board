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
 - Message Board
 - Quiz Completion/Creation
 - LeaderBoards

## TODO
- Main: Create framework [head,nav] (Neil) 
- Database: script for generating "dummy" data (George)
- Login System: Create a the Login & Signup pages (Will W)
- Message_Board: Basic functionality [post, reply] (Tu)

## Tools    
 - python-django
 - bootstrap  

## Operation  
### Github  
 - PLEASE: create a new branch for your development work  
 - DO NOT: push directly to the master branch  
### Server  
This is the CL argument for the server  
[ python manage.py < command > ] 
#### Commands
Run these commands when you add/remove/move any django files  
 - makemigrations  
 - migrate  
Starts the server in the current terminal
 - runserver  
Create a super user that can be access in the "/admin" page
 - createsuperuser 
 Creates a new "app" (kinda like a module) in the src directory
 - startapp < appname > 

