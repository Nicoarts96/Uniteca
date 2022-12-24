# Uniteca

 Unimensa is a Progressive Web App made by **Nicola Cirillo**, **Filippo Spitaletta** and **Pasquale Ferrandino** for the project of Web Technologies (University of Naples Parthenope).
 
 
The purpose of the app is to The purpose of this app is the management of the university library, through the development of a Progressive Web App, which aims at the implementation of the management of the various books and their booking.

The app consists of a client side and a server side. In particular:

## The functionalities of the admin:
The admin will use the app to view reservations or various loaned and available books.


## The functionalities of the students:
Students will be able to access the app with the possibility of reserving a place in the library or even just reserving one or more books.

## How to install Uniteca?
1. Create a virtual environment(venv) by terminal: **> py -m venv venv**;
2. Move to the folder venv/Scripts: **> cd venv/Scripts**;
3. Now activate the virtual environment writing in the terminal "activate": **> activate**;
4. Go to project folder and install requirements by requirements.txt file: **> pip install -r requirements.txt**;
5. Make sure the python interpreter is configured correctly;
6. Install MongoDB for your operating system;
7. If you want to populate the database with users and dishes, you can execute the file "data_entry.py" located in the folder "script_DB", otherwise you can create users and upload dishes in the app;
8. To run the application you can use the command: **> flask run -h 0.0.0.0**
9. Now you can login, but if you don't have an account, you can create it on the registration page. **To simulate university emails you need to register with one of the following emails:**
* **Student: nomeutente @studenti.universita.it**
* **Admin: nomeutente @personale.universita.it**.
