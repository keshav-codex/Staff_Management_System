# Staff Management System

A beginner-friendly Django CRUD application developed to understand the basics of Django framework, database operations, URL routing, views, templates, and model handling.

This project was created as a learning project while exploring Django MVT architecture and connecting a Django application with PostgreSQL database.

## Project Overview

The Staff Management System allows users to manage staff records.

The application provides basic CRUD operations:
- Create new staff records
- View all staff records
- Update existing staff information
- Delete staff records

The main purpose of this project is to understand how Django handles data from frontend forms to the database.

  ***** Live Application Link:*****
  
    https://staff-management-system-prfu.onrender.com/


## Technologies Used

Backend:
- Python
- Django
- PostgreSQL

Frontend:
- HTML
- CSS
- Bootstrap

Development Tools:
- VS Code
- Git and GitHub


## Django Concepts Learned

During the development of this project, I learned and practiced:
- Django project and app structure
- MVT (Model View Template) architecture
- Creating Django models
- Database migration
- URL routing
- Creating views
- Working with Django templates
- Passing data from views to templates
- Handling HTML forms
- CRUD operations
- Connecting Django with PostgreSQL

## Application Flow

The basic working flow of this application is:

User
|
HTML Template
|
URL Mapping
|
View Function
|
Model
|
PostgreSQL Database

## Project Modules

### Staff Model

The Staff model stores employee information:
- Name
- Email
- Phone Number
- Department
- Designation
- Joining Date
- Salary
- Created Date

The model automatically generates:
- Primary Key ID
- Created timestamp
- Updated timestamp

## Views

### Add Staff
Function:
add_staff()

Purpose:
- Displays an empty form
- Accepts user input
- Saves staff information into database

### View Staff

Function:
view_staff()
Purpose:
- Fetches all staff records from database
- Displays data in a table format

### Edit Staff

Function:
edit_staff()
Purpose:
- Loads existing staff information
- Allows modification
- Updates database record

### Delete Staff

Function:
delete_staff()
Purpose:
- Deletes selected staff record from database

## Templates

The project contains different HTML templates:

templates/
|
└── staff/
|
├── home.html
├── add_staff.html
├── edit_staff.html
└── view_staff.html

Each template is responsible for displaying a particular page.

## Database

This project uses PostgreSQL database.
Database operations are handled by Django ORM, so direct SQL queries are not required for basic operations.
Example:

Creating a staff object:
Staff.objects.create()

Fetching records:
Staff.objects.all()

## Frontend Development

The frontend structure and Bootstrap styling were developed with the help of AI assistance using ChatGPT.

AI assistance was used for:
- Improving HTML structure
- Creating clean Bootstrap layouts
- Organizing page design
- Improving user interface appearance

The main purpose was to understand how frontend templates connect with Django backend logic.

## Learning Outcome

After completing this project, I gained practical understanding of:
- How Django applications are structured
- How requests move through Django
- How models interact with databases
- How templates display dynamic data
- How CRUD applications are developed in Django

## Future Improvements

Possible improvements:
- User authentication
- Role-based access
- Search functionality
- Pagination
- Staff profile image upload
- Better form validation
- Deployment on cloud platform

## Author

Keshav

Learning Django by building practical projects.