# T2A2

## Problem identified and why needs to be solved:

---

I am trying to build a web application for the sticker shop. The aim of this app is to provide solutions for the sticker shop to manage the information of their customers, products and orders and reviews. And also allows customers to update their personal information and check their order histories.

### Reasons for building this web application:

* Store Information
  
  At the beginning, a sticker shop might only have a small number of customer, product, order and review. Owner could easily use traditional methods such as excel files or notebooks to store these information. As the shop grows, the number of customers, products, orders and reviews grows as well. These methods could still be used to store information, but the size of excel file will become really big or the owner needs to used lots of notebooks to store these information, which makes these methods inefficient and difficult to use. Therefore, the shop needs new methods to store these information.
 
* Manage Information

  As mentioned above, with small number of information, it is easy to find a particular piece of information and update it. As the number grows, it is hard to locate and update particular information.

* Link Information
  
  A sticker shop needs to link all information together. For example, a reivew needs to be linked to a particular customer and product. With the traditional methods mentioned above, if the owner wants to find the order of a customer, the owner needs to search the customer in the customer file and find out the related review ids. Then use ids to find out the corresponding reviews in the review file. This process is complicated and time consuming.

* Allow customer to manage their own information

  With the traditional methods, customers can not manage and upate their information on their own. They are also not able to check their personal order hisotry. Customers needs to contact the owner to perform these operations, which reduces the customer experiece of the sticker shop.

* Benefits of the app

  With the web app, all of the information are stored in the databse which allows owner to easily manage the information. Customers could also create their own account, update their personal information and check their order history by themselves.

## PostgreSQL and Why

---

I am going to use postgresql for this web application. PostgreSQL is a widely used object-relational database management system for flask applications. It supports both relational and non-relational queries.

### The advantages of the postgresql are:

---

* It supports various data types, such as integer, numeric, string, boolean, geometric types, and non-relational data like JSON and XML. PostgreSQL also supports lots of SQL syntaxes.
* It is highly extensible. Users could extend the database by adding features they need, defining own functions and adding own data types.
* It has good scalability. Developers can use it for either small projects or large applications. When business grows, the software of the company grows as well, which requies the databse extention. With high scalability, postgreSQL supports business growth better. Together with good extensibility, is results in low maintencance.
* It has good security. PostgreSQL not only have features but also have extentions that enhance its security.
* It provides transactional DDL and it is fully acid compliant. Both DDL( data definition language) and DML (data manipulation language) in postgresql are transactional. DDL includes operations such as creating a table, drop a table, etc. DML includes insert, update, etc. A transaction could contains serveral SQL statements(operations). ACID includes atomicity (if one operation within a transaction fails, this transaction fails. The transaction only succeeds if all operations succeed. Then it will apply the changes to the database.), consistency (ensure changes made via a transaction obey the database constraints.), isolation (ensure transactions run in the isolated enviroment. Users could run transactions concurrently without affecting each other.), durability (After the commit, the changes made by the transaction is persist.)
  
  This feature ensures that all data within the database is accurate and consistant with the constraints. It also makes the storage more reliable.
* It implements parallelisation processing of queries, multi-version concurrency control and indexing methods which boost and optimise the performance. This allows users to read and write concurrently.
* It has a high level of conformance with SQL standards. Everyone who familiarise with SQL could easily use it.
* It is compatible with multiple platforms and procedural languages.
* It is reliable and manages data integrity well by introducing constraints. All data within the database must follow the constraints.
* Well documented and has support from communities.
* It is open-source and free.
* It has all RDBMS's features and additional features such as table inheritance.
  
### The disadvantages of the postgresql are:

---

* Compared with non relational based database, users have to define schema, attributes in postgresql first. After this, a object could only store values for these defined attributes, a object could not have values for attributes that not define. All obejcts within the same table have same attributes. Users can not add new fields or attributes to a particular object. Adding new fields or attributes will apply to all objects. While noSQL database allows different objects haveing different attributes.
* Slower reading speed compared with MySQL. PostgreSQL has to read from the first row and then go through each row of the table in order to find the data. This results in relatively slow reading speed compared with other databases.
* It does not implement replication well. Users need to export or replicate data to the new version.
  
## Functionalities and benefits of ORM

---

## What is an ORM

---
Object-realtional mapping (ORM) works between the application and the relational database. ORM converts data between these two systems, which allows developers to devlop databse, query and manipulate data within dabase by using the object-oriented programming languages.

## Functionalities

---

* Link the application and the relational database
  Developers could use the ORM together with database adapter to connect the application and the relational database. For example, developers could user SQLalchemy(ORM) and psycopy2(PostgreSQL database adapter) to connect the flask application and postgresql databse. And then create a database object that allows developers to use build in methods of the ORM in the following code to create model and perform different operations.
* Create Models
  Once the connection established, developers could use the ORM to define models. Models are defined as class, it represents a table in the database. Each object of the model class represents a record or row in the database. The attributes within the model class represents fields in the database, each attributes provides the name, data type and constraints of each fields.
* CLI commands
  Once models are created, developers can use the CLI commands functions from the ORM to perform serveral operations which is similar to the DDL commands in the SQL term. 
  
  These operations includes creating tables via flask create, which create all tables based on the models defined in the application.

  Create object or rows in the database via flask seed. Developers create objects of the model class, then add and commit the changes to the databse. 

  Drop the table via flask drop.

* CRUD
  The ORM create SQL statements for the developers and allows the developers to create new records of the table, read selected records, update or delete particular records. It will convert the programming language that users wrote to the SQL commands. The ORM also need another package called Marshmallow, which serialize data to allow flask to be able to convert it into JSON format and deserialize objects from JSON format to a python dict. The ORM and marshmallow package works together to allow developers to manipulate databse by writing object oriented programming languages instead of plain SQL statement.

## Benefits

---

* ORM is independent of the database. Its high level implementation supports database connections and migrations. If change the databse from one to another, the code might be the same or only need a small number of changes.
* Developers could use familarised object-oriented programming languages to develop database, query and manipulate data. It is helpful for those who are not good at SQL.
* ORM will handle the CRUD operations. As developers do not need to write tedious and repetitive SQL, developers could focus on the logic of the application(model), and write cleaner, less number of code. This is also time consuming.
* Developers is able to develop a class library to create a standalone DLL, which can be used for other applications.
* ORM is simple to implement, it uses a visual modeling process for object-to-table and table-to-object, which makes it easy to maintain and simple to use.
* The code of ORM has been tested, no need to test again, allows developers to save time and focus on testing the code of business logic.
* ORM prevents SQL injection better because queires are sanitised.





Ref:

* https://circle.visual-paradigm.com/docs/code-engineering/object-relational-mapping/
* https://www.keboola.com/blog/acid-transactions

## ERD

![ERD](docs/ERD.png)

---

## Database relationships and descriptions

---
  
### Users table
  
This table contains basic information for all users.
Below are columns with their data types and constraints.

* id (PK, serial int, not null) Primary key
* first name (string(100), not null)
* last name (string(100), not null) 
* Password (text, not null), the password is used for user authentication
* Is admin (boolean, default value is false). This column is for user authorization. Users who have True value are allowed to edit products. Only admin users have true value for this column. Customer users all have the default value. 

---

### Customers table

This table contains specific information for customers.
Columns, data types, and constrains are listed below:

* Id (PK, serial int, not null) Primary key
* Email (string, not null)
* Phone (int, not null)
* User id (int, FK, not null). Links the users table and customers table
* Address(int, FK, not null). Links the customers table and addresses table

#### Relationship (users table and customers table)

The relationship between the users table and the customers table is a one-to-one relationship. A user could be created before the customer because the newly created user could be an admin instead of a customer. But a customer can only be created after the user. Therefore, a customer has one and only one user, while a user has 0 or 1 customer.

#### Relationship (addresses table and customers table)

The relationship between the addresses table and the customers table is a one-to-many relationship. A user typically lives in one place and uses this place for delivery. And many customers might live together and shop separately. So a user has one and only one address, while an address might accommodate one or many customers.

---

### Addresses table

This table contains customers' addresses.
Columns, data types, and constraints are listed below:

* Id (PK, serial int, not null) Primary key
* Street number (int, not null)
* Street name (string(100), not null)
* Suburb (string(100), not null)
* Postcode_id (int, FK, not null) Links the address table and postcode table. Each address has its own postcode.

#### Relationship (addresses table and postcodes table)

Because different customers might have the same postcode, it will become repetitive if I leave it in the address table. So I have created a new table for it. I have also removed the state column from the address table because it links to the postcode rather than the address. 
The relationship between the postcodes table and the addresses table is a one-to-many relationship. Customers might live in the same area and have the same postcode for their address. Or none of them living in this area. And an address must only have one postcode. So a postcode is included in zero or many addresses, and an address has one and only one postcode.

---

### Postcodes table

This table contains the postcode and corresponding state.
Columns, data types, and constraints are listed below:

* Postcode (PK, int, not null)
* State (string(100), not null)

The primary key has been used as a foreign key in the addresses table, which was already mentioned above.

---

### Payment accounts table

This table contains the payment information of the customer.
Columns, data types, and constraints are listed below:

* Id (PK, serial int, not null) Primary key
* Card number (int, not null)
* Card owner's name (string(100), not null)
* Expire date (string, not null)
* Security number (int, not null)
* Encrypted_card_no (string, not null)
* Customer id (int, FK, not null). Links the payment methods table to the customers table.

#### Relationship (payment accounts table and customers table)

The relationship between the payment account table and the customers table is a one-to-many relationship. A customer might use one or many cards for the payment. And one card only belongs to one person. So a customer has one or many payment accounts. A payment account belongs to one and only one customer. 

---

### Orders table

This table contains basic information for orders.
Columns, data types, and constraints are listed below:

* Id (PK, serial int, not null) Primary key
* Order date (date, not null)
* Ship date (date, not null)
* Status (FK, int, not null). Links the orders table and order status table.
* Customer id (FK, int, not null). Links the orders table and customers table.
* Shipping method (FK, int, not null). Links the orders table and shipping methods table.
* Payment account (FK, int, not null). Links the orders table and payment accounts table.

#### Relationship (order status table and orders table)

The relationship between the status table and the orders table is a one-to-many relationship. An order can only have one status, and it can not simultaneously have more than one status. The status could be used by many or not by any of the orders. So an order has one and only one status, and an order status has been used by zero or many orders.

#### Relationship (orders table and customers table)

The relationship between the customers table and the orders table is a one-to-many relationship. A customer can be created before the order. The customer might not order anything or order many times. An order can not be created before a customer. It is made by only one customer. So a customer place zero or many orders, and an order is made by one and only one customer.

#### Relationship (shipping methods table and orders table)

The relationship between the shipping methods table and the orders table is a one-to-many relationship. An order will be shipped by only one method, and a shipping method can be selected by many orders or none of them. So an order has one and only one shipping method. A shipping method could be selected by zero or many orders.

---

### Order status table

This table contains different types of order statuses.
Columns, data types, and constraints are listed below:

* Id (PK, serial int, not null) Primary key
* Description (string(50), not null)

The primary key of this table has been used as the foreign key in the orders table to link these two tables. The relationship has been mentioned above.

---

### Shipping methods table

This table contains different types of shipping methods.
Columns, data types, and constraints are listed below:

* Id (PK, serial int, not null) Primary key
* Type (text, not null)
* Price(int, not null)

The primary key of this table has been used as the foreign key in the orders table to link these two tables. The relationship has been mentioned above.

---

### Products table

This table contains information for products.
Columns, data types, and constraints are listed below:

* Id (PK, serial int, not null). Primary Key
* Name (string(100), not null)
* Description(text)
* Price(int, not null)
* Stock(int, not null)
* Create_date (date, not null)
* Category(int, FK, not null). Links the products table and the categories table

#### Creating join table

Initially, this table links to the orders table, and there is a many-to-many relationship between them. An order could contain only one or many products. A product might be included in many orders or none of them. So an order contains one or many products, a product might be included in zero or many orders.  
Because it is a many-to-many relationship, we need to create a join table for these two tables, which is the order details table. These two tables' primary key becomes the join table's foreign key.

---

### Order details table

Join table for orders and products.
Columns, data types, and constraints are listed below:

* Id (PK, serial int, not null)
* Price (int, not null). Creating a price column again is to ensure that if the price of the product changes later, the price here remains unchanged. Without this column, if we update the product's price, the price in the order details also changes, which results in inaccurate data in this table.
* Order id (int, FK, not null). Links the order details table and orders table
* Product id (int, FK, not null). Links the product table and order details table
  
These two columns link to the orders and products table.

Each order detail contains information about one product.

#### Relationship (order details table and orders table)

An order detail can not be created after an order. Once an order has been created, it has at least one order detail containing this order's information. It can not contains information for different orders. Each order has one or many products. Therefore, an order has one or many order details. So an order has one or many order details, and an order detail contains information for one and only one order.

#### Relationship (order details table and products table)

An order detail can only be created after the product as well. But the product can be created without order details because customers might not order it. Many customers might order the same product. Hence a product can be included in many order details. 
So an order detail contains one and only one product. A product might be included in zero or many order details.

---

### Categories table

This table contains different categories of products.
Columns, data types, and constraints are listed below:

* Id (PK, serial int, not null) Primary key
* Type (text, not null)

#### Relationship (categories table and products table)

The relationship between the categories and the products table is a one-to-many relationship. A sticker shop may have many products in one category, or none belongs to a particular category, and a product could only be categorized into one category. So a product has one and only one category, and a category has zero or many products.

---

### Reviews table

This table contains reviews of the product made by customers.
Columns, data types, and constraints are listed below:

* Id (PK, serial int, not null) Primary key
* Comment (text)
* Rating (int(0-5), not null)
* Customer id (int, FK, not null) Links to the customers table
* Product id (int, FK, not null). Links to the products table

#### Relationship (customers table and reviews table)

The relationship between the customers table and the reviews table is a one-to-many relationship. Some customers might not leave any reviews after their purchases. Some customers might order many times and leave a review every time after they purchases. A review could only be made by one customer. So a customer could leave zero or many reviews. Reviews belong to one and only one customer.

#### Relationship (products table and reviews table)

The relationship between the products table and the reviews table is also a one-to-many relationship. Many customers might purchase the same product and leave reviews for this product. A product might also not have been purchased by anyone and has no reviews. And each review only links to one particular product, and customers can not comment on two products in one review. They need to comment separately for different products as each has pros and cons. So a product might have zero or many reviews. A review relates to one and only one product.

---

## Project Management

---
I used trello to create a digital kanban board for this project.

Kanban is one of agile project management tool. The workflow is visualized for all team members, normally represent as kanban board. The components of kanban board includes cards, columns, work-in-progress limits, etc.

* Kanban Cards
  Each card represents a task(component) of the project
* Kanban Columns
  Each column represents a stage of the workflow. Developers could move cards into the corresponding columns. For example, when developers are working on a task, that task could be placed in the doing column. Once the task is finished, it should be moved to done column.
* Work-in-progress limits
  This limits the maximum number of tasks within each stage of the workflow

Kanban provides great planning flexibility of the project. Once a task finished, developers will take off the task that is on the top of the backlog and start working on it. This allows the product owner to reprioritize the tasks in the backlog while the team are working on the current tasks without affecting the team.
Kanban also allows team to continuously deliver their project to the skateholders. In addition, kanban increased the visibility of the flow and allows all team members on the same page.

Trello is one of tools used for creating kanban board. It is a visualised project management tool that allows users to organize their projects into cards, creating different stages or columns and set the work-in-progress limits. It also allows users to add timeline, label and checklist for each card. Users could arrange task based on the priority and timeline. During development, they can use the checklist to double check whether all requirements of this task has been achieved. Because it is a visualised tool, it is easy for developers and teams to understand what needs to be done and in what order.

### In order to use trello and kanban board for this project:

Firstly, I divided the project into small components and create cards for each of them. Each card has a checklist, includes requirements for each component. I had set different priorites and due date for each card, which helps me to make sure I am doing the tasks in the right order.
I have created cards for:

* README 
  This task does not have due date because I might need to adjust its contents during the development.
* main py file
* init file
  I have set the earlist due date for these two cards above. As they are the basic structure of the application and need to be finished first.
* files for enviroment variables
* create database
* all models
  Each model has its own card. I decided to finish them within two days and set same due date for all of them.
* cli command
  After creating one or two models, it is important to test it with database, to make sure it connects to the database successfully. So it has lower priority than models but higher priority than controllers.
* all controllers
  I have grouped routes together and create card for each controller. I would like to finish these cards after the models, therefore they have lower priority and later due date.
* authentication and authorization
  I will finish this together with controllers, so it has same due date with controllers.
* third-party services or pypi packages
* error handling
  Same as README document, I might encounter different errors during the development. So it is an ongoing task and does not have due date.

Secondly, I have created several columns or stages, includes backlog, to-do, doing, testing and done. Then I put cards into different columns based on their priority and due date. The doing column contains tasks that are currently working on, the to-do column contains tasks that haven't been worked on, but has the highest priority in the rest of tasks. The rest of tasks are in the backlog cloumn, these tasks have lowest priority.

Once a task in the doing column is finished, I will move the task into the done column.  Once all tasks in the doing column are finished, I will move task from the to-do column into the doing column and working on it. At the same time, I will move tasks from the backlog column to the to-do column.

If there is any additional requirements, I can easily create a new card in the backlog without affecting others.


## Third party services or Pypi packages

* flask
  
  Flask is a web app framework written in python for developing web applications. Flask has several dependencies, includes Werkzeug, Jinja2, MarkupSafe, itsdangerous and click.

  Flask use Werkzeug to implements WSGI.

  Jinja2 is a template engine used to render the pages.

  MarkupSafe prevents injection attacks by escaping untrusted input.

  itsdangerous protect data by cryptographically signing it.

  Click is used for creating cli command in flask.

  Developers have to import and create a object of Flask class. The object or instance of the Flask class is the main application for the project. Flask will run this instance each time.

  ---

* flask-sqlalchemy
  
  Flask-SQLALchemy is a flask extension that provides support for SQLALchemy to the project. It simplifies the use of SQLAlchemy by automatically handling the creation, use, and cleanup of commonly used SQLAlchemy objects.

  In order to use flask-sqlalchemy, it has to use configuration key to connect properly to the database. The key is SQLALCHEMY_DATABASE_URI key. The format is 'database type' + 'adaptor' + '://' + 'user name and password' + 'port number (default:5432)' + 'database'

  Developers could use this pypi package to define and create models and make queries for the database and manipulate data.

  ---

* psycopg2
  
  It is a commonly used PostgreSQL database adapter for python. It implements Python DB API2.0 and the thread safety. It is designed for multi-threaded applications and used to link a project with a PostgreSQL database and perform operation on the database. In this project, I have used it together with flask-sqlalchemy to connect and manipulate data. It can be put into the DATABASE_URI key to configure the flask-sqlalchemy, then use flask-sqlalchemy to perform operations.

  ---

* flask-marshmallow
  
  It is the integration layer for Flask and marshmallow. Marshmallow provides support for serializing and deserializing data. Serialize data converts app-level objects to particular python types such as dict, which allows flask to render and convert data to the JSON format and displayed in the HTTP response (With dump method). It could also deserialize JSON format data into python types such as dictionary which could be used within the python program(with load method). Another important part of it is schema which defines fields that will be dump and load, developers could also set up rules within the schema to sanitise and valite data input. Fields are defined with the model using flask-sqlalchemy.

  In addition to the function above, flask-marshmallow has additional features such as URL and Hyperlinks fiedls for HATEOAS ready APIs.

  Developers have to import and create an instance of marshamllow class. Define models and fields using flask-sqlalchemy and the define the HTTP response, data validation with marshamllow.

  ---

* flask-bcrypt

  Flask-bcrypt is a flask extension that hashes important information with bcrypt. Bcrypt is an hasing algorithm that hash and salt the information, it is designed to be slow for hashing. The more time it takes to hash the information, the longer time needed for hacker to brute-force the information. It is commonly used to encrypt password and other important information in flask project.

  In order to use it, developers have to import and create an instance of flask-bcrypt. Then use bcrypt to hash password. As hashing is a one-way operation, and even with same password, the result is different for different hashing. Developers can not hash the pasword again to check their identity. To do this, developers could use bcrypt method(check_password_hash) to check whether the password entered is correct and verify user identities.

  ---

* flask-jwt-extended

  It is a python package that allows flask project using JSON Web Tokens (JWT) to authenticate user and protect routes. Developers could create custom token and secret key, setting up different properties, such as the expiring time for the token.
  
  Users have to log in to verify their indentity. Once their identity has been verified successfully, the API will return a token. They have to include this token in the HTTP request for authentication purposes. Once the token expired, users could log in again to re-authenticate.

  In order to create a web token, developers have to import and create an instance of JWTManager first. Then create a custom secret key for the project and use JWT_SECRET_KEY to configure the token.   After this, developers could use jwt_required() function from flask_jwt_extended to protect routes and use get_jwt_identity() function to obtain the identity of a JWT. Developers could set the custom JWT identity. For example, within this project, I have set up user_id as the JWT identity, which can be used later in the project for creating other records.

  ---

* marshmallow-sqlalchemy
  
  It is a python package that helps to integrate SQLAlchemy and marshmallow. It is required in order for flask_sqlalchemy to work properly.

  ---

* pip-review

  This python package could list all available updates for all installed packages and allow developers to update all of them together.

  ---

* python-dotenv

  Developers could configure flask app in a separate environment file rather than in the main python file, such as which python file is the main python file, what is the flask environment and what is the port number for the app. Python-dotenv is used to link the environment file to flask and causes the flask app to load the environment variables from this environment file every time developers run the app.