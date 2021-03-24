# Lottery_Project
## Application Overview
> Lottery is a web application for use by [NAMEHERE] for [PURPOSEHERE]. It is designed for [CONTEXTHERE]. 

> Para

> Para

> Para

## Setup
> The source code for the Lottery web application can be cloned from [this Github repository](https://github.com/RobLewisQA/Lottery_Project). In order to run the application on Linux Ubuntu 18.04 on your localhost port, ensure that you have Python 3.6 or higher installed, as well as the python installer package, pip3. The following commands should be input in order into your Linux terminal:
1. 
2. 
3. 
4. 
5. 

## Technologies
#### Cloud Server Host:
> *This web application was designed using the Google Cloud Platform as the host for both the compute virtual machine instance and MySQL database virtual machine instance. The GCP compute machine was developed on a Linux Ubuntu 18.04 bootdisk.*
#### Database format:
> *The database is a MySQL relational database integrated with SQLalchemy for reading from and writing to the database using python commands. The python Pandas library is also used to read and clean data from the MySQL database for output to HTML; the tables' HTML is generated using pandas methods for DataFrames.*
#### Frontend script:
> *The application uses the Flask web-development framework to allow python statements to manage HTML output for the URI routes specified in the routes file...* 
#### Testing software:
> *This application was tested using the flask-testing, pytest and pytest-cov python libraries. The unit and configuration testing thoughouly interrogates the read, create, update and delete functions...*
> To replicate the testing, simply run...
#### Deployment software:
> The application was designed and tested for deployment... 
#### Continous Integration and Version Control:
> The source code for this application is maintained in a Github repository accessible [here](https://github.com/RobLewisQA/TuckShop_Project), and can be conncted to Jenkins for automatic continuous integration and deployment.

## Database Entity Relationship Diagram
> The database ... 

> Colloquially, the tables are related such that... A visualisation of this information is show below:
![chart](Tuckshop_ERD.PNG)

## Risk Assessment
Description | Evaluation | Likelihood | Impact Level | Responsibility | Response | Control Mearues
| --- | --- | --- | --- | --- | --- | --- |
(Application's virtual compute machine goes down) | (Application goes offline) | (Low) | (High) | (GCP) | (Spin up a new vm instance either in GCP or an alternative cloud provider and clone the Github repo to integrate with Jenkins) | (Keep an up-to-date source code on Github
Application's virtual MySQL machine goes down) | (Application becomes unusable) | (Low) | (High) | (GCP) | (Spin up a new vm instance in GCP and update the configurations with SQLAlchemy and the virtual compute machine) | (Keep a backup database
The Python language is updated to a new version) | (The application may not run if Flask and SQLAlchemy are not updated for compatibility) | (Medium) | (Medium) | (Developers) | (Run the application on Python 3 and phase in an updated version in CI) | (Keep a robust Github repo so that the source code can be continuously improved and use Jenkins to manage the integration and deployment
Versions of libraries are updated and compatability issues are not mitigated) | (Some aspects of the application may fail) | (Medium) | (High) | (Developers) | (Update the requirements.txt to specify the exact versions required) | (Keep track of planned updates to key libraries, and specify the versions of some of the key libraries required for function)
(The port that the application run on changes) | (The app stops working) | (Low) | (High) | (CI Engineers/Operators) | (Update the firewall settings in the cloud provider to allow a different port access) | (Use Jenkins to manage continuous integration in the app, and notify when there are launch issues)

## Development workflow:
>To see a kanban Trello board of the development process workflow, click [here](https://trello.com/b/h1v0LX39/lottery)

## References:
##### H
##### H