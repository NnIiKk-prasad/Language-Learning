# Creating a Rest API Using Flask and Jsonify
from logging import debug
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    order = len(str(n))
    copy_n = n
    sum = 0
    while n:
        digit = n % 10
        sum += digit ** order
        n //= 10
    if sum == copy_n:
        result = {
            "Number": copy_n,
            "Armstrong": True,
            "Server IP": "123.224.675.43"
        }
    else:
        result = {
            "Number": copy_n,
            "Armstrong": False,
            "Server IP": "123.224.675.43"
        }
    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)