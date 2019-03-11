from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/<person_name>')
def my_service(person_name):
    print(request)
    return jsonify({'Hello': person_name})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
