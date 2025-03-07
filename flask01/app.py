from flask import Flask

app = Flask(__name__)
@app.route('/saludar')
def hola_mundo():
    return "Hola Mundo!"

@app.route('/despedir')
def adios_mundo():
    return "Adiós Mundo!"

@app.route('/comer')
def comer():
    return '<h1 style="color:green;">Estoy comiendo!</h1> <h2>Tengo muchisima hambre aaaaaaaaaaaaaaaaaaaaaaaaa</h2>'

@app.route('/json')
def json():
    return {
        'nombre': 'Felipe',
        'edad': 27,
        'ciudad': 'Emiliano Zapata'
    }

@app.route('/xml')
def xml():
    return '<?xml version="1.0"?><hola>Jelous</hola></xml>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)