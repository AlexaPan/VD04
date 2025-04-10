# VD05
# Создайте свой HTML-шаблон (файл base.html).
# Создайте страницы home.html и about.html, которые будут расширять шаблон и заполнять его контентом.

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def app_cards():
    return render_template("home.html")

@app.route('/blog/')
def blog():
    return render_template('about.html')

@app.route('/contact/')
def contacts():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)