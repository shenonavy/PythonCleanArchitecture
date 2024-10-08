
from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id):
        # Business logic for retriving a user
        return self.user_repository.get_usr_by_id(user_id)