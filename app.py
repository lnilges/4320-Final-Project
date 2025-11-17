#Project: Trip Reservation System

#requirements 
    #A. Create a seating chart and load the initial reservations 
    #B. Display the main menu that asks the user whether they want to reserve a seat or log in as an administrator 
    #C. If the user selects the admin login option they are taken to a page with a form to login. Information the user provides: 
        #admin username 
        #admin password 
    #D. If the user successfully logs in, the following should content should then be displayed on the admin page 
        #A seating chart is displayed 
        #The total sales collected. 
        #A list of reservations made and a button to delete each reservation 
    #E. If the user selects the the reservation option they are taken to a page with a form to reserve a seat. Information the user provides 
        #first name 
        #last name 
        #seat row 
        #seat column 
    #F. Display a flight chart 
    #G. Calculate and get the total sales for the flight when the user successfully logs in as an admin 
    #H. Create and print a reservation code for the user when the user successfully makes a reservation 
    #I. Insert the reservation into the reservations table in the reservations SQLite database 
    #J. Each page should have a link to the main option page. 

 

import flask 
from flask import Flask, render_template, request, url_for, flash, redirect 
 

app = flask.Flask(__name__) 
app.config["DEBUF"] = True 
app.config['SECRET_KEY'] = 'your secret key' 

 

 


app.run() 