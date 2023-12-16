
#The traceback functions for local, global, and fitting alignment were obtained from the template code provided for Homework1
# for CS 466 - Introduction to Bioinformatics. We would like to express our gratitude to the Professor and the course staff for letting us
# utilize their code.

# Ideas used from Homework 1 
UP = (-1,0)
LEFT = (0, -1)
TOPLEFT = (-1, -1)
ORIGIN = (0, 0)


# From Homework 1 for CS 466 - Intro to Bioinformatics
def traceback_global(v, w, pointers):
    i,j = len(v), len(w)
    new_v = []
    new_w = []
    while True:
        di, dj = pointers[i][j]
        if (di,dj) == LEFT:
            new_v.append('-')
            new_w.append(w[j-1])
        elif (di,dj) == UP:
            new_v.append(v[i-1])
            new_w.append('-')
        elif (di,dj) == TOPLEFT:
            new_v.append(v[i-1])
            new_w.append(w[j-1])
        i, j = i + di, j + dj
        if (i <= 0 and j <= 0):
            break
    return ''.join(new_v[::-1])+'\n'+''.join(new_w[::-1])


# From Homework 1 for CS 466 - Intro to Bioinformatics
def argmax(a):
    return max(range(len(a)), key=lambda x : a[x])





# From Homework 1 for CS 466 - Intro to Bioinformatics
def global_aligner(v, w, delta):
    M = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    pointers = [[ORIGIN for j in range(len(w)+1)] for i in range(len(v)+1)]
    score, alignment = None, None
    # YOUR CODE HERE
    for i in range(1, len(w) + 1):
      M[0][i] = -i
      pointers[0][i] = LEFT
    for i in range(1, len(v) + 1):
      M[i][0] = -i
      pointers[i][0] = UP


    for i in range(1, len(v) + 1):
      for j in range(1, len(w) + 1):

         arr = [M[i-1][j] + delta[v[i - 1]]['-'],
                      M[i][j - 1] + delta['-'][w[j - 1]],
                      M[i - 1][j - 1] + delta[v[i-1]][w[j-1]]]
         M[i][j] = max(arr)
         ind = argmax(arr)

         if ind == 2:
            pointers[i][j] = TOPLEFT
         elif ind == 1:
            pointers[i][j] = LEFT
         else:
            pointers[i][j] = UP

    score = M[len(v)][len(w)]
    alignment = traceback_global(v,w, pointers)
    return score, alignment


# from Homework1- CS 466 Intro to Bioinformatics
def traceback_local(v, w, M, init_i, init_j, pointers):
    i,j = init_i, init_j
    new_v = []
    new_w = []
    while True:
        di, dj = pointers[i][j]
        if (di,dj) == LEFT:
            new_v.append('-')
            new_w.append(w[j-1])
        elif (di,dj) == UP:
            new_v.append(v[i-1])
            new_w.append('-')
        elif (di,dj) == TOPLEFT:
            new_v.append(v[i-1])
            new_w.append(w[j-1])
        i, j = i + di, j + dj
        if (M[i][j] == 0):
            break
    return ''.join(new_v[::-1]) + '\n'+''.join(new_w[::-1])

# from Homework 1 - CS 466 Intro to Bioinformatics
def traceback_fitting(v, w, M, init_j, pointers):
    i, j = len(v), init_j
    new_v = []
    new_w = []
    while True:
        di, dj = pointers[i][j]
        if (di,dj) == LEFT:
            new_v.append('-')
            new_w.append(w[j-1])
        elif (di,dj) == UP:
            new_v.append(v[i-1])
            new_w.append('-')
        elif (di,dj) == TOPLEFT:
            new_v.append(v[i-1])
            new_w.append(w[j-1])
        i, j = i + di, j + dj
        if (i <= 0):
            break
    return ''.join(new_v[::-1]) + '\n'+''.join(new_w[::-1])


# This is Purvansh Bal (pbal3)'s implementation for the local sequence alignment algorithm 
# This was implemented as part of Homework 1 for CS 466 - Intro to BioInformatics
def local_aligner(v, w, delta):
    M = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    pointers = [[ORIGIN for j in range(len(w)+1)] for i in range(len(v)+1)]
    score = None
    init_i, init_j = 0,0
    # YOUR CODE HERE
    for i in range(1, len(v) + 1):
      for j in range(1, len(w) + 1):
         arr = [M[i-1][j] + delta[v[i - 1]]['-'],
                      M[i][j - 1] + delta['-'][w[j - 1]],
                      M[i - 1][j - 1] + delta[v[i-1]][w[j-1]], 0]
         M[i][j] = max(arr)
         ind = argmax(arr)

         if ind == 2:
            pointers[i][j] = TOPLEFT
         elif ind == 1:
            pointers[i][j] = LEFT
         elif ind == 0:
            pointers[i][j] = UP
         else:
            pointers[i][j] = ORIGIN


    max_ind  = (0, 0)
    max_M = M[0][0]
    for i in range(len(M)):
      for j in range(len(M[0])):
        if M[i][j] > max_M:
          max_M = M[i][j]
          max_ind = (i, j)

    score = max_M
    init_i, init_j = max_ind
    alignment = traceback_local(v, w, M, init_i, init_j , pointers)
    return score, alignment


# This is Purvansh Bal (pbal3)'s implementation for the local sequence alignment algorithm 
# This was implemented as part of Homework 1 for CS 466 - Intro to BioInformatics
def fitting_aligner(short, reference, delta):
    M = [[0 for j in range(len(reference)+1)] for i in range(len(short)+1)]
    pointers = [[ORIGIN for j in range(len(reference)+1)] for i in range(len(short)+1)]
    score = None
    init_j = 0
    # YOUR CODE HERE
    for i in range(1, len(short) + 1):
      M[i][0] = -i
      pointers[i][0] = UP

    for i in range(1, len(short) + 1):
      for j in range(1, len(reference) + 1):
        arr = [M[i-1][j] + delta[short[i - 1]]['-'],
                    M[i][j - 1] + delta['-'][reference[j - 1]],
                    M[i - 1][j - 1] + delta[short[i-1]][reference[j-1]]]
        M[i][j] = max(arr)
        ind = argmax(arr)

        if ind == 2:
          pointers[i][j] = TOPLEFT
        elif ind == 1:
          pointers[i][j] = LEFT
        else:
          if arr[0] == arr[2]:
            pointers[i][j] = TOPLEFT
          else:
            pointers[i][j] = UP

    init_j = argmax(M[len(short)])
    score = max(M[len(short)])
    alignment = traceback_fitting(short,reference,M, init_j,pointers)
    return score, alignment


'''
v,w == seq1, seq2: The 3 sequences to be aligned.
match_score: The score for a match between two characters in the sequences.
mismatch_penalty: The penalty for a mismatch.
gap_penalty: The penalty for one, two gaps.

'''

def initialize_matrix(dimensions, value=0):
    return [[[value] * dimensions[2] for _ in range(dimensions[1])] for _ in range(dimensions[0])]




def multiple_sequence_alignment(seq1, seq2, seq3, match_score, mismatch_penalty, gap_penalty):
    n = len(seq1)
    m = len(seq2)
    p = len(seq3)

    score_matrix = initialize_matrix((n + 1, m + 1, p + 1))

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, p + 1):
                match_score_value = match_score if seq1[i - 1] == seq2[j - 1] == seq3[k - 1] else mismatch_penalty

                diagonal_score = score_matrix[i - 1][j - 1][k - 1] + match_score_value
                vertical_score = score_matrix[i - 1][j][k] - (gap_penalty)
                horizontal_score = score_matrix[i][j - 1][k] - (gap_penalty)
                depth_score = score_matrix[i][j][k - 1] - (gap_penalty)

                score_matrix[i][j][k] = max(diagonal_score, vertical_score, horizontal_score, depth_score, 0)

    aligned_seq1, aligned_seq2, aligned_seq3 = "", "", ""
    i, j, k = n, m, p

    while i > 0 or j > 0 or k > 0:
        current_score = score_matrix[i][j][k]
        match_score_value = match_score if seq1[i - 1] == seq2[j - 1] == seq3[k - 1] else mismatch_penalty

        if i > 0 and j > 0 and k > 0 and score_matrix[i][j][k] == score_matrix[i - 1][j - 1][k - 1] + match_score_value:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            aligned_seq3 = seq3[k - 1] + aligned_seq3
            i -= 1
            j -= 1
            k -= 1
        elif i > 0 and score_matrix[i][j][k] == score_matrix[i - 1][j][k] - (gap_penalty):
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            aligned_seq3 = '-' + aligned_seq3
            i -= 1
        elif j > 0 and score_matrix[i][j][k] == score_matrix[i][j - 1][k] - (gap_penalty):
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            aligned_seq3 = '-' + aligned_seq3
            j -= 1
        elif k > 0 and score_matrix[i][j][k] == score_matrix[i][j][k - 1] - (gap_penalty):
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            aligned_seq3 = seq3[k - 1] + aligned_seq3
            k -= 1
        elif i > 0 and j > 0 and k > 0 and score_matrix[i][j][k] == 0:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            aligned_seq3 = seq3[k - 1] + aligned_seq3
            i -= 1
            j -= 1
            k -= 1
        else:
            break  

    return aligned_seq1, aligned_seq2, aligned_seq3, score_matrix[n][m][p]

def gap_affine_penalty_alignment(v, w, match_score, mis_pen, open_pen, ext_pen):
    n, m = len(v), len(w)
    
    # Initialize matrices
    mat = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    # For vertical gaps (in w)
    ext_v = [[0 for _ in range(m + 1)] for _ in range(n + 1)] 
    
    # For horizontal gaps (in v)
    ext_h = [[0 for _ in range(m + 1)] for _ in range(n + 1)]  

    # Fill matrices
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c1, c2 = v[i - 1], w[j - 1]
            score = match_score if c1 == c2 else -mis_pen

            # main matrix - choosing the best option: match/mismatch, vertical gap, or horizontal gap
            mat[i][j] = max(mat[i-1][j-1] + score, ext_v[i][j], ext_h[i][j])

            # Vertical gap matrix - extending or starting a new gap in w
            ext_v[i][j] = max(ext_v[i-1][j] - ext_pen, mat[i-1][j] - open_pen)

            # Horizontal gap matrix - extending or starting a new gap in v
            ext_h[i][j] = max(ext_h[i][j-1] - ext_pen, mat[i][j-1] - open_pen)

    # Traceback to find the optimal alignment and calculate the score
    v_aligned, w_aligned = "", ""
    i, j = n, m
    alignment_score = 0
    while i > 0 and j > 0:
        if mat[i][j] == mat[i-1][j-1] + (match_score if v[i-1] == w[j-1] else -mis_pen):
            v_aligned = v[i-1] + v_aligned
            w_aligned = w[j-1] + w_aligned
            alignment_score += match_score if v[i-1] == w[j-1] else -mis_pen
            i, j = i - 1, j - 1
        elif mat[i][j] == ext_v[i][j]:
            v_aligned = v[i-1] + v_aligned
            w_aligned = "-" + w_aligned
            alignment_score -= (open_pen if mat[i][j] == mat[i-1][j] - open_pen else ext_pen)
            i -= 1
        else:
            v_aligned = "-" + v_aligned
            w_aligned = w[j-1] + w_aligned
            alignment_score -= (open_pen if mat[i][j] == mat[i][j-1] - open_pen else ext_pen)
            j -= 1

    return v_aligned, w_aligned, alignment_score