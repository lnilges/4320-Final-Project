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
import sqlite3
 

app = flask.Flask(__name__) 
app.config["DEBUG"] = True 
app.config['SECRET_KEY'] = 'your secret key'

# Function to open a connection to the database.db file
def get_db_connection():
    # create connection to the database
    conn = sqlite3.connect('reservations.db')
    
    # allows us to have name-based access to columns
    # the database connection will return rows we can access like regular Python dictionaries
    conn.row_factory = sqlite3.Row

    #return the connection object
    return conn

#function to get admin login information from database


#function to get reservation information from database

#function to generate cost matrix for flights
#input: none
#output: returns a 12 x 4 matrix of prices
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix


#route to get to admin page 
#will display seating chart, total sales, and reservation list with delete button
@app.route('/admin', methods=('GET', 'POST'))
def admin():
   return render_template('admin.html')

#route to get to reservations page
#will have a form where users can enter first name, last name, seat row, and seat column
#will then display a reservation code one reservation is made
@app.route('/reservations', methods=('GET', 'POST'))
def reservations():
    return render_template('reservations.html')

 
@app.route('/', methods=('GET', 'POST'))
def index():
    choice = request.form.get('user_choice')

    if not choice:
        flash("ERROR: Must choose an option.")
        return(redirect(url_for('index')))
    
    if choice == "admin":
        return render_template('admin.html')
    if choice == "reservation":
        return render_template('reservation.html')
    else:
        return redirect((url_for('index')))

app.run() 