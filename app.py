from flask import Flask, render_template
import os

app = Flask(__name__)

# Configuração básica
app.config['SECRET_KEY'] = 'uma-chave-secreta-segura'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)