from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.models import User

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('/', endpoint='list')
def users_list():
    users = User.query.all()
    return render_template('users/user_list.html', users=users)


@user.route('/<int:user_id>', endpoint='details')
def user_detail(user_id: int):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        return NotFound(f"User {user_id} does not exist!")
    return render_template('users/details.html', user=user)
