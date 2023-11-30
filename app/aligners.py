UP = (-1,0)
LEFT = (0, -1)
TOPLEFT = (-1, -1)
ORIGIN = (0, 0)

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

def argmax(a):
    return max(range(len(a)), key=lambda x : a[x])


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


def local_aligner(v, w, delta):
    return "OOPS! LA Not implemented yet"


def fitting_aligner(v, w, delta):
    return "OOPS! FA Not implemented yet"
