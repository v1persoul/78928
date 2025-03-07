from flask import Flask, render_template
from modelos import Producto

app = Flask(__name__)

@app.route('/')
def inicio():
    productos = [
        Producto('Laptop', 15000),
        Producto('Mouse', 300),
        Producto('Teclado', 1200)
    ]
    return render_template('index.html', productos=productos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)