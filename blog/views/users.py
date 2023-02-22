from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')
USERS = {
    1: 'Alex',
    2: 'Piter',
    3: 'Jon',
    4: 'Ken',
}


@user.route('/', endpoint='list')
def users_list():
    return render_template('users/user_list.html', users=USERS)


@user.route('/<int:user_id>', endpoint='details')
def user_detail(user_id: int):
    try:
        user_name = USERS[user_id]
    except KeyError:
        raise NotFound(f"User {user_id} does not exist!")
    return render_template('users/details.html', user_id=user_id, user_name=user_name)
