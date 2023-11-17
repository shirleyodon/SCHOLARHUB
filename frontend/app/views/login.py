from flask import Blueprint, render_template, request, redirect, url_for, session
from ..utils import search_etudiant_by_email, search_encadreur_by_email
from ..models import Etudiant, EncadreurPedagogique, Error

import json


login_route = Blueprint('login_route', __name__)


@login_route.route("/", methods=["GET", "POST"])
@login_route.route("/sh/login/", methods=["GET", "POST"])
def login():
    # To log in
    if request.method == "POST":
        email = request.form["email"]
        user_type = request.form["account-type-option"]
        alert = None

        # Log as Etudiant
        if user_type == "student-option":

            user = search_etudiant_by_email(email)

            if isinstance(user, Etudiant):
                password = request.form["password"]

                if user.motPasseEtud == password:
                    session['user'] = json.dumps(user.to_dict())
                    home_url = url_for('home_route.home')
                    return redirect(home_url)
                else:
                    alert = Error("Mot de passe incorrect")

            else:
                # user is an Error object
                alert = user

            return render_template("login.html", alert=alert, previous_email=email)

        # Log as Encadreur
        # elif user_type == "teacher-option":
        #     user = search_encadreur_by_email(email)

        #     if isinstance(user, EncadreurPedagogique):
        #         password = request.form["password"]

        #         if user.motPasseEtud == password:
        #             session['user'] = json.dumps(user.to_dict())
        #             home_url = url_for('home_route.home')
        #             return redirect(home_url)
        #         else:
        #             alert = Error("Mot de passe incorrect")

        #     else:
        #         # user is an Error object
        #         alert = user

        #     return render_template("login.html", alert=alert, previous_email=email)
            
            
        # Log as Admin
        else:
            # Not available yet
            return render_template("login.html")

    # To get login form
    else:
        return render_template("login.html")
