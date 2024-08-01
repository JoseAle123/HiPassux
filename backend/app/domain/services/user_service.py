from app.domain.repositories.user_repository import User,UserRepository
from werkzeug.security import generate_password_hash
from datetime import datetime

class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)

    @staticmethod
    def get_user_by_username(username):
        user = UserRepository.get_user_by_username(username)
        return user

    @staticmethod
    def get_user_by_email(email):
        user = UserRepository.get_user_by_email(email)
        return user

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            UserRepository.remove(user)
            return True
        return False

    @staticmethod
    def authenticate(username, password):
        user = UserRepository.get_user_by_username(username)
        if user and user.password == password:
            return user
        return None

    @staticmethod
    def authenticate_user(username, password):
        return UserRepository.verify_user(username, password)

    @staticmethod
    def create_user(username, first_name, last_name, birth_date, phone_number, gender, email, password):
        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            phone_number=phone_number,
            gender=gender,
            email=email,
            password=generate_password_hash(password, method='pbkdf2:sha256')  # Use pbkdf2:sha256
        )
        UserRepository.add(new_user)  # Usa el método add en lugar de add_user
        return new_user
    
    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)

    
    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            for key, value in data.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            UserRepository.update(user)  # Usa update para guardar cambios
            return user
        return None
    
    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            UserRepository.remove(user)
            return True
        return False


    @staticmethod
    def authenticate(username, password):
        user = UserRepository.get_user_by_username(username)
        if user and user.password == password:
            return user
        return None
