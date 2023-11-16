from flask import Blueprint, render_template, url_for, redirect, request, session

import json

print_route = Blueprint('print_route', __name__)


# Route to print a book
@print_route.route("/sh/print/", methods=["GET", "POST"])
def print_book():
    from ..models import LivrePlus
    from ..utils import dict_to_etudiant, get_livre, dict_to_encadreur

    # Getting user in session
    user_json = session.get('user')

    user = None

    alert = None

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

            form_data = json.dumps(form_data)
            result_url = url_for('result_route.result',
                                 previous_form=form_data)

            return redirect(result_url)

        else:
            # Getting some data from url String
            previous_form = request.args.get('previous_form')
            livre_ref = request.args.get('livre_ref')

            if previous_form and livre_ref:
                form_data = json.loads(previous_form)

                # To return back to result Livre list
                page = request.args.get('page')

                livre = get_livre(livre_ref)

                if isinstance(livre, LivrePlus):
                    return render_template('print.html', user=user, previous_form=form_data, livre=livre, page=page)

                else:
                    return render_template('print.html', user=user, previous_form=form_data, alert_error=livre, page=page)
            else:
                result_url = url_for('result_route.result')
                return redirect(result_url)

    # The user didn't log in
    else:
        return render_template("print.html")
