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
def admin_info():
    pass

#function to get reservation information from database
def get_reservations():
    pass

#function to get seat rows/columns to make chart to display in reservation page
def get_seating_chart():
    conn = get_db_connection()
    query = "SELECT seatRow, seatColumn from reservations"
    seats = conn.execute(query).fetchall()
    conn.close()

    rows = 12
    columns = 4

    chart = [['O' for _ in range(columns)] for _ in range(rows)]

    for seat in seats:
        row = seat['seatRow']
        column = seat['seatColumn']
        chart[row][column] = 'X'

    return chart

#function to get reservation code
def get_reservation_code(first_name):
    i = j = 0
    reservation_str = "infotc4320"
    reservation_code = ""

    while i < len(first_name) and j < len(reservation_str):
        reservation_code += first_name[i] + reservation_str[j]
        i += 1
        j += 1

    while i < len(first_name):
        reservation_code += first_name[i]
        i += 1

    while j < len(reservation_str):
        reservation_code += reservation_str[j]
        j += 1

    return reservation_code

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
@app.route('/reservation', methods=('GET', 'POST'))
def reservation():
    seating_chart = get_seating_chart()
    first_name = None
    last_name = None
    seat_row = None
    seat_column = None
    reservation_code = None

    if request.method == 'POST':
        #get first name from form
        first_name = request.form['first_name']
        if not first_name:
            flash('ERROR: Must enter first name')

        #get last name from form
        last_name = request.form['last_name']
        if not last_name:
            flash('ERROR: Must enter first name')

        #get seat row from form
        seat_row = request.form['seat_row']
        if not seat_row:
            flash('ERROR: Must select a row')
        
        #get seat column from form
        seat_column = request.form['seat_column']
        if not seat_column:
            flash('ERROR: Must select a seat')

        #make reservation code, combination of first name and infotc4320, alternating letters
        #****Fix this - if one string is longer, does not finish longer string
        reservation_code = get_reservation_code(first_name)        


        #add reservation to the database
        conn = get_db_connection()
        conn.execute('INSERT INTO reservations (passengerName, seatRow, seatColumn, eTicketNumber) VALUES (?, ?, ?, ?)', (first_name, seat_row , seat_column, reservation_code))
        conn.commit()
        conn.close()
        

    return render_template('reservation.html', seating_chart=seating_chart, first_name=first_name, reservation_code=reservation_code, seat_row=seat_row, seat_column=seat_column)

 
@app.route('/', methods=('GET', 'POST'))
def index():
    choice = request.form.get('user_choice')

    if request.method == "POST":
        if not choice:
            flash("ERROR: Must choose an option.")
            return(redirect(url_for('index')))
        
        if choice == "admin":
            return render_template('admin.html')
        if choice == "reservation":
            return render_template('reservation.html')
        else:
            return redirect((url_for('index')))
    return render_template('index.html')

app.run() 