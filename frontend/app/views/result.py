from flask import Blueprint, render_template, redirect, url_for, request, session

import json

result_route = Blueprint('result_route', __name__)


# Result route
@result_route.route('/sh/search/livre/', methods=["GET", "POST"])
def result():
    from ..models import Information, Error, Pagination
    from ..utils import dict_to_etudiant, dict_to_encadreur

    # Getting user in session
    user_json = session.get('user')

    user = None

    # The user has logged in
    if user_json:
        user_dict = json.loads(user_json)
        
        
        # What kind of user is logged in
        if "MatEtud" in user_dict:
            user = dict_to_etudiant(user_dict)
            
        elif 'MatEncad' in user_dict:
            user = dict_to_encadreur(user_dict)
        else:
            pass
        

        if request.method == "POST":
            # Get all form inputs
            form_data = {}
            for key, value in request.form.items():
                form_data[key] = value

            result = process(form_data)

            if isinstance(result, Information):
                return render_template("result.html", user=user, previous_form=form_data, alert_info=result)

            elif isinstance(result, Error):
                return render_template("result.html", user=user, previous_form=form_data, alert_error=result)

            # At least one livre found
            else:
                pagination = Pagination(items=result)
                return render_template("result.html", user=user, previous_form=form_data, pagination=pagination)

        else:
            previous_form = request.args.get('previous_form')

            # If there was a research before getting this page
            if previous_form:
                form_data = json.loads(previous_form)

                page = request.args.get('page', 1, type=int)

                result = process(form_data)

                if isinstance(result, Information):
                    return render_template("result.html", user=user, previous_form=form_data, alert_info=result)

                elif isinstance(result, Error):
                    return render_template("result.html", user=user, previous_form=form_data, alert_error=result)

                # At least one livre found
                else:
                    pagination = Pagination(items=result, page=page)

                    return render_template("result.html", user=user, previous_form=form_data, pagination=pagination)

            # If there was no research before
            else:
                home_url = url_for('home_route.home')
                return redirect(home_url)

    # The user didn't log in
    else:
        return render_template("result.html")


def process(form_data):
    from ..utils import search_livre_by_theme_categorie_parcours_niveau

    # All possibles criterion
    cat_list = [None, "Rapport de projet", "Rapport de stage", "Memoire"]
    parc_list = [None, "Génie logiciel et base de données",
                 "Administrateur système et réseau", "Informatique général"]
    niv_list = [None, "L1", "L2", "L3", "M1", "M2"]

    # Get selected categorie, parcours, niveau
    theme = form_data.get("search")
    selected_cat = cat_list[int(form_data.get('categorie'))]
    selected_parc = parc_list[int(form_data.get('parcours'))]
    selected_niv = niv_list[int(form_data.get('niveau'))]

    return search_livre_by_theme_categorie_parcours_niveau(
        theme, selected_cat, selected_parc, selected_niv)
