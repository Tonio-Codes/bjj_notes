import sqlite3

class notes:
    __db_path = ""

    def __init__(self):
        self.connection = sqlite3.connect("bjj_notes.db")
        self.cursor = self.connection.cursor()
        self.create_db()
    
    def create_db(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS notes(
                             name TEXT NOT NULL,
                             date TEXT NOT NULL,
                             note TEXT NOT NULL
                            )
                             """)
        self.connection.commit()
    
    def insert(self, name:str, date:str, note:str):
        try:
            self.cursor.execute("""INSERT INTO notes (name,date,note)
                                VALUES (?,?,?)""",(name,date,note))
            self.connection.commit()
            print('entry added')

        except sqlite3.IntegrityError as e:
            print("error adding entry",e)
    
    def delete(self, name:str, date:str):
        try:
            self.cursor.execute("""DELTE FROM notes
                                WHERE
                                name = ? AND date = ?""",(name,date))
        except sqlite3.IntegrityError as e:
            print("error deleting entry", e)
    
    def get_notes(self, name:str, date:str = None):
        try:
            if date:
                notes = self.cursor.execute("""SELECT name, date, note
                                FROM notes 
                                WHERE
                                name = ? AND date = ?""",(name,date))
            else:
                notes = self.cursor.execute("""SELECT name, date, note
                                FROM notes 
                                WHERE
                                name = ?""", name)
            return notes.fetchall()
        except sqlite3.IntegrityError as e:
            print("error getting notes for that user ", e)
            return None

    def close(self):
        self.connection.close()


def main():
    notes_db = notes()

if __name__ == "__main__":
    main()
