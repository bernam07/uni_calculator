# Calculadora Média Ensino Superior

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![Status](https://img.shields.io/badge/Status-Active-success)

Uma aplicação web universal desenvolvida em **Python (Flask)** para ajudar estudantes universitários a calcular a sua média ponderada de curso. A ferramenta permite a inserção manual de notas, persistência de dados local e exportação de resultados, com uma arquitetura preparada para monetização via Google AdSense e funcionalidades Premium.

## Funcionalidades

* **Cálculo em Tempo Real:** A média ponderada e o total de ECTS atualizam-se automaticamente a cada alteração.
* **Persistência de Dados:** Usa `LocalStorage` para guardar as notas do estudante no browser.
* **Interface Dinâmica:** Adicionar e remover disciplinas facilmente.
* **Exportação:** Permite descarregar a pauta em formato `.csv` (compatível com Excel).
* **Monetização:** Espaços dedicados e configurados para Google AdSense.
* **Teaser Premium:** Modal de "Importação PDF" preparado para captar interesse.

## Tecnologias Usadas

* **Backend:** Python (Flask)
* **Frontend:** HTML5, Bootstrap 5, JavaScript
* **Deploy:** Configurado para Render (via Gunicorn)

## Estrutura do Projeto

```text
/
├── app.py                # Servidor Flask
├── requirements.txt      # Dependências
├── runtime.txt           # Versão do Python (opcional)
└── templates/
    └── index.html        # Interface do utilizador
```
