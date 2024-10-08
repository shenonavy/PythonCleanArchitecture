
from flask import Flask
from app.controllers.user_controller import get_user
from app.controllers.admin_controller import get_admin

app = Flask(__name__)

@app.route('/user/<int:user_id>', methods=['GET'])
def getUser(user_id):
    return get_user(user_id)

@app.route('/admin/<int:user_id>', methods=['GET'])
def getAdmin(user_id):
    return get_admin(user_id)

if __name__ == 'main':
    app.run(debug=True)