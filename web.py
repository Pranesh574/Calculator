from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def display():
    answer = ''
    if request.method == 'POST':
        answer = int(request.form['a']) * int(request.form['b'])

    return """
        <form method="post">
            <input name="a" type="number">
            <input name="b" type="number">
            <button>Multiply</button>
        </form>
    """ + str(answer)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9845)