import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS student(
            id Integer Primary Key,name text,rno text,std text, contact text,email text, gender text,dob text, address text,
            dist text, pin text,fname text, mname text,focc text, mocc text, fcno text, mcno text,pemail text )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, rno, std, contact, email, gender, dob, address, dist, pin, fname, mname, focc, mocc, fcno, mcno ,pemail ):
        self.cur.execute("insert into student values (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         (name, rno, std, contact, email, gender, dob, address, dist, pin, fname, mname, focc, mocc, fcno, mcno ,pemail ))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from student")
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from student where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, rno, std, contact, email, gender, dob, address, dist, pin, fname, mname, focc, mocc, fcno, mcno ,pemail ):
        self.cur.execute(
            "update student set name=?,rno=?, std=?, contact=?, email=?, gender=?, dob=?, address=?, dist=?, pin=?, fname=?, mname=?, focc=?, mocc=?, fcno=?, mcno=?,pemail=?  where id=?",
            (name, rno, std, contact, email, gender, dob, address, dist, pin, fname, mname, focc, mocc, fcno, mcno ,pemail, id))
        self.con.commit()
        
o=Database("Student.db")

