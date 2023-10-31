from flask import Blueprint, render_template, request, session, redirect, url_for
from ..utils import search_livre_by_theme_categorie_parcours_niveau

import json

home_route = Blueprint('home_route', __name__)


# Home route
@home_route.route("/sh/home/", methods=["POST", "GET"])
def home():
    from ..models import Information, Error, Pagination
    from ..utils import dict_to_etudiant

    # Getting user in session
    user_json = session.get('user')

    user = None

    if user_json:
        user_dict = json.loads(user_json)
        user = dict_to_etudiant(user_dict)

        if request.method == "POST":
            # Get all form inputs
            form_data = {}
            for key, value in request.form.items():
                form_data[key] = value

            form_data = json.dumps(form_data)

            result_url = url_for('result_route.result',
                                 previous_form=form_data)
            return redirect(result_url)

        else:
            return render_template('home.html', user=user)
    else:
        return render_template('home.html')
