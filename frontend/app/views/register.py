from flask import Blueprint, render_template, url_for, redirect, request, session
from ..utils import search_etudiant_by_matricule, is_valid_email, enrol_etudiant, search_encadreur_by_matricule, is_valid_encadreur_email, enrol_encadreur
from ..models import Etudiant, EncadreurPedagogique, Error, Success

import json

register_route = Blueprint('register_route', __name__)


@register_route.route("/sh/register/", methods=["GET", "POST"])
def register():
    # To enrol
    if request.method == "POST":
        # Get all Etudiant input
        form_data = {}

        for key, value in request.form.items():
            form_data[key] = value

        alert = None

        # Enrol as Etudiant
        if form_data.get("account-type-option") == "student-option":
            etudiant = search_etudiant_by_matricule(form_data.get("matricule"))

            # All is alright
            if isinstance(etudiant, Etudiant):
                # To make sure it's not a fake account owner
                if form_data.get("name")[0:].lower() == etudiant.nomEtud[0:].lower():

                    # Account without an E-mail yet
                    if not etudiant.emailEtud:

                        # Make sure the E-mail didn't use yet
                        if is_valid_email(form_data.get("email")):
                            etudiant.emailEtud = form_data.get("email")
                            etudiant.motPasseEtud = form_data.get("password")
                            response = enrol_etudiant(etudiant.to_dict())

                            if isinstance(response, Success):
                                session['user'] = json.dumps(
                                    etudiant.to_dict())
                                home_url = url_for('home_route.home')
                                return redirect(home_url)

                            else:
                                # response is an Error object
                                alert = response

                        # E-mail was already used
                        else:
                            alert = Error(
                                "Cet E-mail est déjà rattaché à un autre compte")

                    # Account with an existing E-mail
                    else:
                        alert = Error(
                            "Ce compte utilisateur est déjà rattaché à un E-mail de connexion")

                # Fake account owner
                else:
                    alert = Error(
                        "Le N° matricule ne correspond pas au nom saisi")

            # Something wrong like server not running or resource not found
            else:
                # etudiant is an Error object
                alert = etudiant

            return render_template("register.html", alert=alert, previous_data=form_data)


        # Enrol as Enseignant
        else:
            encadreur = search_encadreur_by_matricule(form_data.get("matricule"))

            # All is alright
            if isinstance(encadreur, EncadreurPedagogique):
                # To make sure it's not a fake account owner
                if form_data.get("name")[0:].lower() == encadreur.nomEncad[0:].lower():

                    # Account without an E-mail yet
                    if not encadreur.emailEncad:

                        # Make sure the E-mail didn't use yet
                        if is_valid_encadreur_email(form_data.get("email")):
                            encadreur.emailEncad = form_data.get("email")
                            encadreur.motPasseEncad = form_data.get("password")
                            response = enrol_encadreur(encadreur.to_dict())

                            if isinstance(response, Success):
                                session['user'] = json.dumps(
                                    encadreur.to_dict())
                                home_url = url_for('home_route.home')
                                return redirect(home_url)

                            else:
                                # response is an Error object
                                alert = response

                        # E-mail was already used
                        else:
                            alert = Error(
                                "Cet E-mail est déjà rattaché à un autre compte")

                    # Account with an existing E-mail
                    else:
                        alert = Error(
                            "Ce compte utilisateur est déjà rattaché à un E-mail de connexion")

                # Fake account owner
                else:
                    alert = Error(
                        "Le N° matricule ne correspond pas au nom saisi")

            # Something wrong like server not running or resource not found
            else:
                # Encadreur is an Error object
                alert = encadreur

            return render_template("register.html", alert=alert, previous_data=form_data)
            #return render_template("register.html")

    # To get register form
    else:
        return render_template("register.html")
