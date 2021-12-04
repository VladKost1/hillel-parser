from flask import Flask, request
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect("chinook.db", check_same_thread=False)
cursor = connection.cursor()


@app.route("/names")
def names():
    customers = cursor.execute("SELECT DISTINCT FirstName FROM customers")
    res = customers.fetchall()
    return str(res)


@app.route("/tracks")
def tracks():
    return str(cursor.execute('SELECT COUNT (*) FROM tracks').fetchall())


@app.route("/tracks-sec")
def tracks_sec():
    tracks = cursor.execute("SELECT Milliseconds, Name FROM tracks").fetchall()
    res = []
    for rec in tracks:
        rec = list(rec)
        rec[0] *= 0.001
        res.append(rec)
    return str(res)


@app.route('/customers/')
def customers():
    if not request.args:
        return str(cursor.execute('SELECT FirstName, LastName From customers').fetchall())
    params = request.args.keys()
    query = 'SELECT FirstName, LastName FROM customers WHERE'
    if 'fax' in params:
        result = request.args.get('fax').replace('_', ' ').upper()
        query += f' Fax {result} OR'
    if 'id' in params:
        result_list = request.args.getlist('id')
        sign = '=' if len(result_list) == 1 else 'IN'
        result = result_list[0] if len(result_list) == 1 else tuple(result_list)
        query += f' CustomerId {sign} {result} OR'
    if 'country' in params:
        result_list = request.args.getlist('country')
        sign = '=' if len(result_list) == 1 else 'IN'
        result = result_list[0] if len(result_list) == 1 else tuple(result_list)
        query += f' Country {sign} {result} OR'

    customer = cursor.execute(query[:-3])
    res = customer.fetchall()
    return str(res)


if __name__ == '__main__':
    app.run()




