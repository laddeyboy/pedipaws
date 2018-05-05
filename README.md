# PEDIPAWS(r)

**Our mock business website is dedicated to providing your fur-baby with the pampering he/she deserves.**

To view our company website please click here: <a href="https://pedipaws.herokuapp.com/">PediPaws</a>

### **_Getting Started_**
We built the framework of our website using Python, HTML, and CSS.  
We wrote a database using Postgres with 4 tables for services, appointments, groomers, and reviews.


### **_Required Packages_**
```  
* tornado
* boto3
* os
* queries
* markdown2
```

### **_Required Libaries_**
```
* import tornado.ioloop
* import tornado.web
* import tornado.log
* import queries
* import markdown2
* import os
* import boto3
```

### **_Issues Encountered_**
```
* Heroku - Heroku was potentially the biggest issue, with running our .sql file
  and having it load directly into our Heroku database.
  After several formatting attempts we were able to get it to run in Heroku using 
  'heroku pg:psql'
  There were a number of deployment erros that required the removal of the pipfile.lock,
  the pip environment, and everything had to be reinstalled into the pip virtual environment.
  After deployment, the app wouldn't run and this was resolved by going through 
  each Heroku log line by line.  
  This resulted in lost get submission and code reviews from the team.
* CSS - Getting the CSS to work the way we needed and wanted it to work.
* GitHub - Being the first time to use the advanced features of GitHub and working 
  as a group caused a few dilemmmas getting everything to push, pull, and merge properly.
```

### **_Authors_**
```
* Katy Gibson
* Jessica Robinson
* Aaron Wilkinson
* Josh Ladwig
* Jared Stevens
```

### **_Acknowledgments_**
_PediPaws(r)_ wouldn't have been possible without _Paul_ and his unending love for _Mittens_ his beloved cat. 

### **_License_**
_PediPaws(r) is the intellectual property of Team Awesome Code, LLC (r)_
