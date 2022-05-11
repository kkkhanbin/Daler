from flask import render_template
from src.routes import routes_bp
from src.forms import SearchForm

TITLE = 'Daler Edition'


@routes_bp.route('/interview', methods=['GET', 'POST'])
def interview():
    return render_template(
        'interview/interview.html', title=TITLE, search_form=SearchForm())
