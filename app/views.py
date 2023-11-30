from flask import render_template, request
from app import app
import subprocess
from app.script import add, check_input, make_score_matrix
from app.aligners import global_aligner, local_aligner, fitting_aligner


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    seq1 = request.form['code1']
    seq2 = request.form['code2']
    
    if not check_input(seq1) or not check_input(seq2):
        result = "ERRRORRRRRR. Check your input strings"
    else:
        type_of_alignment = request.form['alignmentType']
        positions = ['a','b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o', 'p']
        gap_penalty = int(request.form['gap_penalty'])
        array = []

        for c in positions:
            array.append(int(request.form[c]))

        
        score_matrix = make_score_matrix(array, gap_penalty)


        if type_of_alignment == "global":
            score, result = global_aligner(seq1, seq2, score_matrix)
        
        elif type_of_alignment == "local":
            score, result = local_aligner(seq1, seq2, score_matrix)
        
        else:
            score, result = fitting_aligner(seq1, seq2, score_matrix)


    return render_template('index.html', result=result, score=score)
