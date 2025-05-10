from flask import Flask, render_template, request

# Flask для создания приложения
# render_template для  рендеринка HTML-шаблонов(процесс, при котором к шаблону(обычно текстовому, например HTML) добавляются данные
# и на выходе получается готовый контент, например, веб-страница)
# request - объект, который содержит данные от клиента, например, данные формы

app = Flask(__name__, static_folder="static") # Создаем экземпляр приложения Flask
                                              # static указывает, что статические файлы будут находиться в папке static(CSS)


@app.route('/', methods=['GET', 'POST'])  # @app.route- маршрут (URL)
def home(): # функция будет обрабатывать запрос по указанному маршруту
    # если запрос методом POST
    if request.method == 'POST':
        favorite_language = request.form.get('language') # request.form - словарб с данными формы
                                                         # get('language') - возвращает значение поля с именем language

        # рендерим шаблон с благодарностью и передаем в него переменную language,что отображает информацию на странице "спасибо"                                                
        return render_template('thanks.html', language=favorite_language)
    # если метод запроса GET, рендерим 'index.html', где форма для выбора любимого языка
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True) # запускаем Flask
