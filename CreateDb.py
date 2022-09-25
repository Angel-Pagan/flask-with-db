import sqlite3 # note, sqlite3 comes with python3

##### Note, this is just an example script, to create a database, you need to do this manually.
## otherwise you just need to run this once and then you can use the database in your flask app

### For a brief tutorial on sqlite using pythong, please visit: https://www.tutorialspoint.com/sqlite/sqlite_python.htm 
### You can scroll down to where it says 'Connect To Database' 
### For an additional tutorial that goes through the basics, please see: https://www.sqlitetutorial.net/sqlite-python/ 

# Connecting to sqlite
# connection object
connect = sqlite3.connect('./patients.db')
 
# db object
db = connect.cursor()

# delete table patient_table if it exists
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

# // commit () --> This method commits the current transaction. If you don't call this method, 
# anything you did since the last call to commit() is not visible from other database connections.

# Creating table, 
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            zipcode tinyint(9) NOT NULL,
            phone_number tinyint(10) NOT NULL,
            gender CHAR(1) NOT NULL,
            cms_patient BOOLEAN
        ); """

db.execute(table)
connect.commit() # commit the changes, this is annoying but necessary


## note, you may see a .db-journal file, that is a temporary file that is created when you create a database.
## insert data into the table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob,zipcode,phone_number,gender,cms_patient) values('12345', 'Frank', 'Jones', '01/01/2000','10454','9122229212','M','Y')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob,zipcode,phone_number,gender,cms_patient) values('23456', 'Janet', 'Monroe', '02/02/2001','10457','5555553292','F','Y')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob,zipcode,phone_number,gender,cms_patient) values('34567', 'Michelle', 'Smith', '03/03/2002','11324','5555551234','F','N')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob,zipcode,phone_number,gender,cms_patient) values('45678', 'Lucus', 'Garcia', '04/04/2003','14454','5555552142','M','Y')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob,zipcode,phone_number,gender,cms_patient) values('56789', 'Sam', 'Lopez', '05/05/2004','12454','5555553212','F','N')")

connect.commit()

# close the connection
connect.close()