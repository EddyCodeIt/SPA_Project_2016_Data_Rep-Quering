# SPA_Project_2016_Data_Rep-Quering

# 1) App Source Code Installation Instructions

- Follow this steps to install server on local machine

    1) Install Python on your machine
            https://www.python.org/downloads/
            
            For Windows: 
            After installing python, call it in your terminal by typing "python" or "py".
            You should enter python console.
            If Windows does not recognize python, you have to specify path to a python.exe file in OS enviromental variables settings.
            
    2) Install Flask micro-framework 
            http://flask.pocoo.org/docs/0.11/installation/
            
            For Windows: 
            In some cases, you have to specify path to Script folder in your python directory in OS enviromental variables settings.
            
    3) Clone git repository or unzip folder with a source. CD to project folder in your console. 
       Run command: py server.py
       Copy the address provided by python and use it as URL in browser.

# 2) App Organisation

- It is a good practice to use multiple python modules to construct backend of an app, i.e, server.
  By breaking one complex module, with many differant functionalities, into smaller modules, we achive:
  
    * Easier Readability for yourself and other developers
    * Reusability of modules in differant context
    * Standard practices
    * Each module do it's own stuff
    
_________________
|  Modules List | 
-----------------


1) server.py 
        Content: module connection to an App directory that contains other modules
                 and run method that starts your application
    

2) __init__.py 
        Content: creates instace of Flask and connection to views

3) views.py
        Content: routing of an app and certain functionalities (methods) for each route



# 3) SPA - Single Page Application

- Application has initial document file called index.html
- Once the initial page is loaded subsequent navigations are handled without a full page load. 
  
To connect index.html file to server:
    1) Inside views.py - define root() function 
                       - function returns index.html 
    2) index.html file must be located inside 'static' directory
       and static must be located inside App directory

























