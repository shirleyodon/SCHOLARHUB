from flask import Blueprint, redirect, url_for, session

logout_route = Blueprint('logout_route', __name__)


@logout_route.route("/sh/logout/")
def logout():
    session.pop('user', None)
    login_url = url_for('login_route.login')

    return redirect(login_url)
