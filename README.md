# SPA_Project_2016_Data_Rep-Quering

<div class="container-fluid" >
    <title>Installation Guide</title>
     <h1 class="text-center" style="color: #72237D">List of libraries to Install</h1><br><br>

     <p> First of all, you need to install a python on your local machine: <a href = "https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe">Python v3.5.2</a></p>
     <br>
     <p> You need pip installation tool to install Python libraries. <a href = "https://pip.pypa.io/en/stable/installing/">Pip</a></p>
     <br>
     <p>Once that done, run command <mark>pip freeze</mark> in your command prompt. This will show what Python already has.</p>
     <p>Use pip to install following: </p>
     <ul>
         <li>Flask==0.11.1</li>
         <li>Flask-Login==0.4.0</li>
         <li>Flask-SQLAlchemy==2.1</li>
         <li>Flask-WTF==0.13.1</li>
         <li>SQLAlchemy==1.1.4</li>
         <li>sqlalchemy-migrate==0.10.0</li>
         <li>WTForms==2.1</li>
     </ul>

</div>


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




# 4) Bootstrap


# 5) Templates

1.1) Create templates folder in app directory.
     Inside the templates folder, Flask will look for Jinja2 templates.


1.2) Jinja2 syntaxis: 
            {{var}}
            {% logic %}
            {% endlogic %}

# 6) SQLAlchemy error handling helps:
http://stackoverflow.com/questions/24522290/cannot-catch-sqlalchemy-integrityerror














