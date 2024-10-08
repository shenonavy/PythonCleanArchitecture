from flask import jsonify
from app.controllers import router
from app.repositories import user_repository
from app.services import user_service
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

user_repository = UserRepository()
user_service = UserService(user_repository)

@router.route('/api/admin/<int:user_id>', methods=['GET'])
def get_admin(user_id):
    user = user_service.get_user_by_id(user_id)
    # return jsonify({"user_id": user_id, "name": user['name']})
    return jsonify({"user_id": user_id, "name": 'abc', "role": 'Admin'})

