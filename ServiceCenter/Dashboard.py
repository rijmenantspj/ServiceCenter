from flask import (
    Blueprint, render_template
)

bp = Blueprint('dashboard', __name__)


@bp.route('/')
def dashboard():
    return render_template('Dashboard/Dashboard.html')
