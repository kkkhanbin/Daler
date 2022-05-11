from flask import render_template
from src.routes import routes_bp
from src.forms import SearchForm

TITLE = 'Daler Edition'


@routes_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template(
        'index.html', title=TITLE, search_form=SearchForm())
