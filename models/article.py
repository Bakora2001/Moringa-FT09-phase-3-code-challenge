from database.connection import get_db_connection

class Article:
    def __init__(self, title, content, author_id, magazine_id):
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)', 
                       (self.title, self.content, self.author_id, self.magazine_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles')
        articles = cursor.fetchall()
        conn.close()
        return [Article(a['title'], a['content'], a['author_id'], a['magazine_id']) for a in articles]

    def __repr__(self):
        return f'Article(title={self.title}, content={self.content}, author_id={self.author_id}, magazine_id={self.magazine_id})'
