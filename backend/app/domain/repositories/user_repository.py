from app.domain.entities.user import db, User

class UserRepository:

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update_user(user):
        db.session.commit()

    @staticmethod
    def remove(user):
        try:
            # Delete the user object from the session
            db.session.delete(user)
            # Commit the transaction to save the changes to the database
            db.session.commit()
        except Exception as e:
            # Rollback the transaction in case of an error
            db.session.rollback()
            return {'error': f'Ocurrió un error al eliminar el usuario: {str(e)}'}
        return {'message': 'Usuario eliminado con éxito'}

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_user_by_username(username):
        return db.session.query(User).filter_by(username=username).first()

    @staticmethod
    def verify_user(username, password):
        user = UserRepository.get_user_by_username(username)
        if user and user.password == password:
            return user
        return None