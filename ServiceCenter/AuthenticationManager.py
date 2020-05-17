import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash

from ServiceCenter.DatabaseManager import get_db

bp = Blueprint('authentication', __name__, url_prefix='/authentication')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()

        user = db.execute(
            'SELECT * FROM Users WHERE Username = ?', (username,)
        ).fetchone()

        if user is None or not check_password_hash(user['password'], password):
            flash('Incorrect username and/or password provided.', 'danger')
        else:
            session.clear()
            session['UserId'] = user['UserId']
            return redirect(url_for('dashboard'))

    return render_template('AuthenticationManager/Login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('UserId')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM Users WHERE UserId = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('dashboard'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('authentication.login'))

        return view(**kwargs)

    return wrapped_view
