# Knuth Morris Pratt

# AABAACAABAAA
# [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5, 2]
# A AA AAB AABA AABAA
# A BA BAA ABAA AABAA

def build_lps(pattern, p_len):
  lps = [0]
  i = 1
  j = 0
  while i < p_len:
    if pattern[j] == pattern[i]:
      j += 1
      lps.append(j)
      i += 1
    elif j > 0:
      j = lps[j-1]
    else:
      lps.append(0)
      i += 1
  return lps

def kmp(pattern, text):

  iterations = 0

  text_len = len(text)
  pattern_len = len(pattern)
  lps = build_lps(pattern, pattern_len)
  i = 0
  j = 0

  while i < text_len:
    iterations += 1
    if pattern[j] == text[i]:
      i += 1
      j += 1
    elif j > 0:
      j = lps[j - 1]
    else:
      i += 1

    if j == pattern_len:
      j = lps[j - 1]
      print 'match at ', i - pattern_len

  print iterations

# txt = "ABABDABACDABABCABAB"
# pat = "ABABCABAB"

# txt = "AABAACAADAABAAABAA"
# pat = "AABA"

txt = "BBBABABBBB"
pat = "BBBB"

txt = "HABHHHABCD"
pat = "ABCD"

txt = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
pat = 'AAAAAAAAB'

txt = "AABAACAADAABAAABAA"
pat =  "AABA"

# txt = "AAAAABAAABA"
# pat = "AAAA"
kmp(pat, txt)


print build_lps('AABAACAABAAA', len('AABAACAABAAA'))


# test_1 = 'AAAA'
# test_1_r = [0,1,2,3]

# test_2 = 'ABCD'
# test_2_r = [0,0,0,0]

# # prefixes A AA AAB AABA
# # Suffixes A AA AAB AABA

# test_3 = 'AABAACAABAA'
# test_3_r  = [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]

# test_4 = 'AAACAAAAAC'
# test_4_r  = [0, 1, 2, 0, 1, 2, 3, 3, 3, 4]

# test_5 = 'AAABAAA'
# test_5_r  = [0, 1, 2, 0, 1, 2, 3]

# def check(text, result):
#   answer = build_lps(text, len(text))
#   for x,y in zip(answer, result):
#     if x != y:
#       print 'Wrong', answer
#       return
#   print 'Correct'

# check(test_1, test_1_r)
# check(test_2, test_2_r)
# check(test_3, test_3_r)
# check(test_4, test_4_r)
# check(test_5, test_5_r)