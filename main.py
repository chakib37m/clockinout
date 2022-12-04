from cs50 import SQL

db = SQL("sqlite:///app.db")



def newemp(id, firstname, lastname):
    db.execute("INSERT INTO employees(id, firstname, lastname) VALUES(?, ?, ?)", id, firstname, lastname )

def clockin(id):
    db.execute("INSERT INTO times(date, id, clockin) VALUES(CONVERT(varchar, getdate(), 23), ?, CURRENT_TIMESTAMP)", id)

def clockout(id):
    db.execute("INSERT INTO times(date, id, clockout) VALUES(CONVERT(varchar, getdate(), 23), ?, CURRENT_TIMESTAMP)", id)
