from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            # Получаем числа из формы
            numbers = list(map(float, request.form['numbers'].split()))
            operation = request.form['operation']

            if operation == 'min':
                result = min(numbers)
            elif operation == 'max':
                result = max(numbers)
            elif operation == 'average':
                result = sum(numbers) / len(numbers)
        except ValueError:
            result = "Пожалуйста, введите корректные числа."

    return render_template('index2.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
