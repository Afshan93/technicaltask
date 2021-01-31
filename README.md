# Development of Project 
This project is a simple employee user story for application of job.
The Project is developed using python,django as frontend while Postgresql as backend.
Intially it is developed and deployed  on windows platform while at end of this document proces is explained to deploy this project on Linux Server.
Resource: https://www.c-sharpcorner.com/article/django-crud-createretriveupdatedelete-record-using-django-class-based-view2/

## Minimum Requirements
You need   Os installed (windows, ubuntu, Debian)
Python 3.8  , it will work for any version above 3
Django 3.0,    
Postgresql, refer to https://www.postgresql.org/

## Django Introduction 
Django is a python web framework for developers looking for a faster way to build web applications and with less code. Refer https://www.djangoproject.com/ for more help

## Commands for installations 
D:\Python>python --version       
D:\Python>python -m venv venv     
D:\Python>venv\scripts\activate      
(venv) D:\Python>pip install django==3.0     
## Creating Project in Django
(venv) D:\Python>django-admin startproject employee_project        
(venv) D:\Python>cd employee_project       
## Installing Psycopg2  to use Postgresql with Django    
(venv) D:\Python\employee_project>pip install Psycopg2     Refer to https://www.psycopg.org/
## Aditional apps
(venv) D:\Python\employee_project>pip install pyautogui   refer to https://pyautogui.readthedocs.io/en/latest/
(venv) D:\Python\employee_project>pip install Pillow
## Run Server 
After seeting the database stting in settings .py
(venv) D:\Python\employee_project>python manage.py runserver    


## Database 
  Go to pgadmin, click on the server, right click on databases and create database , runscript given in createdatabase.txt and follow the steps given. As a shortcur db script is also provided to copy directly. Refer to  https://www.youtube.com/watch?v=e1MwsT5FJRQ 
  
##  Starting  Project
(venv) D:\Python\employee_project>python manage.py startapp employee_register    
##  Migrating the database
(venv) D:\Python\employee_project>python manage.py sqlmigrate employee_register
(venv) D:\Python\employee_project>python manage.py migrate

##  Installed Forms 
(venv) D:\Python\employee_project>pip install django-crispy-forms      

## Creating Models, Views and Urls
As django is framework which utilizes models, views and controllers , hence i  created the models by introducing two  different classes of employee and German language.
3 different html templates were used under forms. Urls were updated for every single path we need to redirect.

## Final Results     
visit http://127.0.0.1:8000/employee/4/ to see required form.     



## If local installtion is required for linux, Step by step details are mentioned below

## Install Ubuntu
Ubunto or Debian is recommended . Refer to https://ubuntu.com/tutorials/install-ubuntu-desktop#2-requirements  for ubuntu installation step by step. This project is tested on windows.

## Installation  commands
 $ sudo apt-get install python3.8  
 python --version

### Setting up Virtual Environment
$ sudo pip install virtualenv   
$  virtualenv -p python3 venv   
$  cd venv   
 $ source bin/activate   
 $ pip install django   
 django-admin startproject employee_project   
 
 employee_project/  
    manage.py   
    employee_django/    
        __init__.py    
        settings.py     
        urls.py     
        wsgi.py     
 cd employee_project       
 
 Now by defaultdjangi as db.sqlite as database  but a  to use postgresql as database we will go to settings .py and change the database settings and insert our username abnd password , settings can be checked from settings.py.       
 
 After setting the database use following commands    
 $ python manage.py makemigrations    
 $ python manage.py migrate      
 Rund the below command to check the server from browser    
 $ python manage.py runserver        
  
  You must see a screen saying congratulation , Django has been installed      
  Pressc ctrl-c to stop serve anytime.        
  For other configuration settings refer to https://dev.to/achiengcindy/-how-to-set-up-django-environment-in-linux-for-beginners-35am       
  
 After this  create the database , installing postgreql is required  refer to  https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04
  Go to pgadmin, click on the server, right click on databases and create database , runscript given in createdatabase.txt and follow the steps given.
  As a shortcur db script is also provided to copy directly.      
  
  Copy all the script files to employee_project      
  and then visit http://127.0.0.1:8000/employee/4/  to see required form.      
  
  
 
  
  
  
  
  
