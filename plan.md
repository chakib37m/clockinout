make a database of employees
make all needed informations
make a way to change informations in a database
easier updating
mistakes handling employee forgot to clock out
GUI
The program has a database of the following :
firstname, lastname, non null number, for every employee
roll out every two weeks
restarts hours
keep hours organized per day
new database per day?
relation between it and the main one on ID
autodelete databases 
check if an employee exists before clocking in/out incase of mistakes in numbers





    CREATE TABLE employees(
        id INT,
        firstname VARCHAR(255),
        lastname VARCHAR(255),
        PRIMARY KEY (id)
    );
        CREATE TABLE times(
        date DATE,
        id INT,
        clockin TIMESTAMP,
        clockout TIME STAMP
    );