### This does not work!!! I dont think


NO_OF_CHARS = 256


def computeTF(pat, pattern_len):
    global NO_OF_CHARS

    TF = [[0 for _ in range(NO_OF_CHARS)] for _ in range(pattern_len+1)]
    TF[0][ord(pat[0])] = 1

    lps = 0

    for i in range(1, pattern_len):
      for j in range(NO_OF_CHARS):
        TF[i][j] = TF[lps][j]

      TF[i][ord(pat[i])] = i + 1

      if i < M:
        lps = TF[lps][ord(pat[i])]

    return TF

def search(pat, txt):
    global NO_OF_CHARS
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)
    state = 0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        if state == M:
            print("Pattern found at index: {}".format(i-M+1))

txt = "AABAACAADAABAAABAA"
pat = "AABA"

# pat = "ACACAGA"

search(pat, txt)

