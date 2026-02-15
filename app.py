from flask import Flask, render_template, request
import pdfplumber
import re
import os

app = Flask(__name__)

# Configuração para upload de ficheiros
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def extrair_notas_do_pdf(caminho):
    notas = []
    with pdfplumber.open(caminho) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text: continue
            for linha in text.split('\n'):
                if "Aprovado" in linha:
                    try:
                        # A MESMA LÓGICA QUE JÁ TINHAS
                        match_nota = re.search(r'(\d{2}\.\d{2})', linha) or re.search(r'\s(\d{2})\s', linha)
                        match_ects = re.search(r'\s(6|12|18|30)\s', linha)
                        nome = re.sub(r'\[.*?\]|\d{4,}-\d{2}|Aprovado.*', '', linha).strip()
                        nome = re.sub(r'^\d+\s*\]*', '', nome).strip()

                        if match_nota and match_ects:
                            notas.append({
                                'disciplina': nome,
                                'nota': float(match_nota.group(1)),
                                'ects': float(match_ects.group(1))
                            })
                    except: continue
    return notas

@app.route('/', methods=['GET', 'POST'])
def index():
    media = None
    disciplinas = []
    
    if request.method == 'POST':
        if 'pdf_file' in request.files:
            ficheiro = request.files['pdf_file']
            if ficheiro.filename != '':
                caminho = os.path.join(app.config['UPLOAD_FOLDER'], ficheiro.filename)
                ficheiro.save(caminho)
                
                disciplinas = extrair_notas_do_pdf(caminho)
                
                # Cálculo da média
                total_pontos = sum(d['nota'] * d['ects'] for d in disciplinas)
                total_ects = sum(d['ects'] for d in disciplinas)
                
                if total_ects > 0:
                    media = round(total_pontos / total_ects, 2)
                
                # Limpeza (opcional, apagar o ficheiro depois)
                os.remove(caminho)

    return render_template('index.html', media=media, disciplinas=disciplinas)

if __name__ == '__main__':
    app.run(debug=True)