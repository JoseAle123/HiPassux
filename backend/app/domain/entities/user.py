from app.extensions import db

class User(db.Model):
    __tablename__ = 'USERS'  # Ensure this matches your table name

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(15))
    gender = db.Column(db.String(1))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            'id': self.user_id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date.isoformat() if self.birth_date else None,
            'phone_number': self.phone_number,
            'gender': self.gender,
            'email': self.email,
            'password': self.password
        }    