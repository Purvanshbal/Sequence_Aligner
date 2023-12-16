
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


