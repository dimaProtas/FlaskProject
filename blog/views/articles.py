from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

articles = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {1: {'name_article': "Flask",
                'author_article': {'id': 1, 'name': 'Alex'},
                'text': 'Flask article text...'},

            2: {'name_article': "Django",
                'author_article': {'id': 2, 'name': 'Piter'},
                'text': 'Django article text...'},

            3: {'name_article': "JSON:API",
                'author_article': {'id': 3, 'name': 'Jon'},
                'text': 'JSON:API article text...'}
            }



@articles.route('/', endpoint='list')
def article_list():
    return render_template('articls/list.html', articles=ARTICLES)


@articles.route('/<int:title_id>', endpoint='detail')
def article_detail(title_id: int):
    try:
        title_name = ARTICLES[title_id]
    except KeyError:
        raise NotFound(f"No such article {title_id}")
    return render_template('articls/detail.html', title_name=title_name, title_id=title_id)
