# Задание 1
#
# Создайте новое приложение Flask, которое будет отображать
# текущие дату и время на главной странице.

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def show_datetime():
    # Получаем текущее время и форматируем его
    now = datetime.now()

    return render_template("index1.html", current_time=now)
@app.route('/current-time')
def get_current_time():
    now = datetime.now()
    return now.strftime('%A, %d %B %Y, %H:%M')

if __name__ == "__main__":
    app.run(debug=True)