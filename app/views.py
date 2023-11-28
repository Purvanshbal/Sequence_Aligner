from flask import render_template, request
from app import app
import subprocess
from app.script import add

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    code1 = request.form['code1']
    code2 = request.form['code2']

    # You can modify this to run your specific code
    result = add(int(code1), int(code2))
    print(result)

    return render_template('index.html', result=result)
