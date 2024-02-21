from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
#import mysql.connector

from flask_mysqldb import MySQL

app = Flask(__name__)
mydb = mysql.connector.connect(
    host="mysql-msprtop.alwaysdata.net",
    user="msprtop_admin",
    password="ePSI2023!",
    database="msprtop_crm"
)
app.config['MYSQL_HOST'] = 'mysql-msprtop.alwaysdata.net'
app.config['MYSQL_USER'] = 'msprtop_admin'
app.config['MYSQL_PASSWORD'] = 'ePSI2023!'
app.config['MYSQL_DB'] = 'msprtop_crm'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# Initialisation de l'extension MySQL
mysql = MySQL(app)


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions (à cacher par la suite)

# Fonction pour créer une entrée "authentifie" dans la session de l'utilisateur
def est_authentifie():
    return session.get('authentifie')

@app.route('/', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants
        if request.form['username'] == 'admin' and request.form['password'] == 'password': # password à cacher par la suite
            session['authentifie'] = True
            # Rediriger vers la route lecture après une authentification réussie
            return redirect(url_for('accueil'))
        else:
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)



@app.route('/accueil')
def accueil():
    return render_template('accueil.html')

if __name__ == "__main__":
  app.run(debug=True)
