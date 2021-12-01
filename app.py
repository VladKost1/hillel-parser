from flask import Flask
from faker import Faker
import requests

app = Flask(__name__)


@app.route('/requirements')
def requirements():
    with open('requirements.txt', 'r') as file:
        text = file.read()
    return text


@app.route('/generate-users/<int:n>')
def generate_users(n):
    f = Faker()
    result = []
    for i in range(n):
        result.append(f'{f.first_name()} {f.email()}')
    return str(result)


@app.route('/mean')
def mean():
    with open('hw.csv', 'r') as file:
        text = file.read()
    return text


@app.route('/space')
def space():
    result = requests.get('http://api.open-notify.org/astros.json')
    return str(result.json()['number'])


if __name__ == '__main__':
    app.run()

