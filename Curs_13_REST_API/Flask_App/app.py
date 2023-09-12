from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


# GET
@app.route('/')
def index():
    return 'Bine'


@app.route('/date')
def get_date():
    date = datetime.now().date().isoformat()
    return f'Data este : {date}'


@app.route('/time')
def get_time():
    time = datetime.now().time().isoformat()
    return f'Ora este : {time}'


@app.route('/hello/<name>')
def hello(name):
    return f'Hello {name}'


# POST
@app.route('/login', methods=['POST'])
def login():
    print(request.method)
    print(request.json)  # Se afiseaza datele trimise ca payload in request
    return 'OK'\
    '''
    Variabila request este o variabila globala sin pachetul flask care retine date 
    despre requestul curent
    '''



# PUT
@app.route('/login', methods=['PUT'])
def login_put():
    data = request.json
    return jsonify(data)


if __name__ == '__main__':
    ''' codul din acest if va fi rulat doar cand aplicatia porneste din
    fisierul curent atribur=tul __name__ ia valoarea __main__ doar cand aplicatia este rulata
    din fisierul curent
    '''
    app.run(debug=True)  # debug = restart aplicatie la fiecare modificare
