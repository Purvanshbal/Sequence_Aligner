from flask import render_template, request
from app import app
import subprocess
from app.script import add, check_input, make_score_matrix
from app.aligners import global_aligner, local_aligner, fitting_aligner, multiple_sequence_alignment, gap_affine_penalty_alignment


# Code for home page
@app.route('/')
def index():
    return render_template('index.html')



# Code for MSA
@app.route('/msa.html')
def msa():
    return render_template('msa.html')


@app.route('/run_msa_code', methods=['POST'])
def run_msa_code():
    seq1 = request.form['code1']
    seq2 = request.form['code2']
    seq3 = request.form['code3']

    if not check_input(seq1) or not check_input(seq2) or not check_input(seq3):
        result = "ERRRORRRRRR. Check your input strings"
        score = "ERRRR"
    else:

        match_score = int(request.form['match_score'])
        mismatch_penalty = int(request.form['mismatch_penalty'])
        gap_penalty = int(request.form['gap_penalty'])
        
        one, two, three, score = multiple_sequence_alignment(seq1, seq2, seq3, match_score, mismatch_penalty, gap_penalty)

        result = (one + '\n' + two + '\n' + three)

    return render_template('msa.html', result=result, score=score)


@app.route('/run_gap_code', methods=['POST'])
def run_gap_code():

    seq1 = request.form['code1']
    seq2 = request.form['code2']

    if not check_input(seq1) or not check_input(seq2):
        result = "ERRRORRRRRR. Check your input strings"
        score = "ERRRR"
    else:
        match_score = int(request.form['match_score'])
        mismatch_penalty = int(request.form['mismatch_penalty'])
        open_penalty = int(request.form['open_penalty'])
        extension_penalty = int(request.form['ext_penalty']) 

        one, two, score = gap_affine_penalty_alignment(seq1, seq2, match_score, mismatch_penalty, open_penalty, extension_penalty)   
        result = (one + '\n' + two)

    return render_template('gap.html', result=result, score=score)


# Code for gap penalty
@app.route('/gap.html')
def gap():
    return render_template('gap.html')



# Code for Sequence Aligner
@app.route('/seq_align.html')
def seq_align():
    return render_template('seq_align.html')



@app.route('/run_code', methods=['POST'])
def run_code():
    seq1 = request.form['code1']
    seq2 = request.form['code2']
    
    if not check_input(seq1) or not check_input(seq2):
        result = "ERRRORRRRRR. Check your input strings"
        score = "ERRRR"
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


    return render_template('seq_align.html', result=result, score=score)
