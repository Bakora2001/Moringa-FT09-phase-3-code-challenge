from database.connection import get_db_connection

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self.name, self.category))
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines')
        magazines = cursor.fetchall()
        conn.close()
        return [Magazine(m['name'], m['category']) for m in magazines]

    def __repr__(self):
        return f'Magazine(name={self.name}, category={self.category})'
