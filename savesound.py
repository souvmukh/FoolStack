import sqlite3

class SaveSound():
    def __init__(self, valuesfordb):
        self.valuesfordb = valuesfordb
        self.id = valuesfordb[0]

    def insertSound(self):
        conn = sqlite3.connect('newsound.db')
        conn.execute("INSERT INTO SOUND (ID, SCALE) VALUES (?,?)", self.valuesfordb)
        conn.commit()
        print('************************DATA Read*************************')
        conn.close()

    def selectSound(self):
        conn = sqlite3.connect('newsound.db')
        conn.execute("SELECT SCALE from SOUND where ID = ?",self.id)
        conn.commit()
        print('************************DATA Read*************************')
        conn.close()


    def deleteSound(self):
        conn = sqlite3.connect('newsound.db')
        conn.execute("DELETE from SOUND where ID = ?",self.id)
        conn.commit()
        print('************************DATA Deleted***********************')
        conn.close()


    def buildTable(self):
        conn = sqlite3.connect('newsound.db')
        conn.execute('''CREATE TABLE SOUND
                        (ID INT PRIMARY KEY NOT NULL,
                        SCALE TEXT NOT NULL);''')
        print('************************TABLE Created***********************')
        conn.close()


