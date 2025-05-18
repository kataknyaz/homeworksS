from flask import Flask, render_template, request


app = Flask(__name__) 

@app.route('/', methods=['GET'])  
def form():
    return render_template('index.html')
    
@app.route('/submit', methods=["GET"])
def submit(): 
    data = request.args.to_dict()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True) # запускаем Flask



