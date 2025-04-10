# VD05
# Создайте свой HTML-шаблон (файл base.html).
# Создайте страницы home.html и about.html, которые будут расширять шаблон и заполнять его контентом.

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def app_cards():
    context = {
        "active_home": "active",
        "active_about": "",
        "active_contact": ""
    }
    return render_template("home.html", **context)

@app.route('/blog/')
def blog():
    context = {
        "active_home": "",
        "active_about": "active",
        "active_contact": ""
    }
    return render_template('about.html', **context)

@app.route('/contact/')
def contacts():
    context = {
        "active_home": "",
        "active_about": "",
        "active_contact": "active"
    }
    return render_template('contact.html', **context)

if __name__ == "__main__":
    app.run(debug=True)