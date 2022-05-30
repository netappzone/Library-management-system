
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    isbn = db.Column(db.String(50))
    author = db.Column(db.String(50))
    year = db.Column(db.Integer)
    available = db.Column(db.String(3))

    def __init__(self, title, isbn, author, year):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.year = year
        self.available = 'Yes'


class Bookloans(db.Model):
    __tablename__ = 'bookloans'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    email = db.Column(db.String(50))
    issuedt = db.Column(db.Date)

    def __init__(self, title, email, issuedt):
        self.title = title
        self.email = email
        self.issuedt = issuedt

class Wishlist(db.Model):
    __tablename__ = 'wishlist'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, title, email):
        self.title = title
        self.email = email
      


class Members(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


# with open("static/data.csv") as f:
#     reader = csv.reader(f)
#     next(reader)
#     for i in reader:
#         new_entry = Books(
#             isbn=i[1],
#             author=i[2],
#             year=i[3],
#             title=i[4])
#         db.session.add(new_entry)
#         db.session.commit()
