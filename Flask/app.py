from flask import Flask
from flask import render_template

app = Flask(__name__) # Создание сайта...

UID = {'1':'Фильм',
       '2':'Игра',
       '3':'Картинка',
       '4':'File Word',
       '5':'Project1',
       '6':'Расписание'
       }

@app.route('/') # Создаем декоратор и указываем его адрес
def index():    # Создаем функцию, которая будет вызваватся в декораторе
    return render_template('page.html')  # подключить html страницу

@app.route('/download/<id>')
def download(id):
    if not id in UID:
        return "Файл ненайден"
    else:
        return f'Загрузека файла: {UID[id]}...'


if __name__ == "__main__":
    app.run(debug=True)