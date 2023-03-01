from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.models import Articles

articles = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')


@articles.route('/', endpoint='list')
@login_required
def article_list():
    articles = Articles.query.all()
    return render_template('articls/list.html', articles=articles)


@articles.route('/<int:title_id>', endpoint='detail')
def article_detail(title_id: int):
    articles = Articles.query.filter_by(id=title_id).one_or_none()
    if not articles:
        raise NotFound(f"No such article {title_id}")
    return render_template('articls/detail.html', title=articles)
