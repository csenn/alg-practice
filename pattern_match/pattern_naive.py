
def search(pat, txt):
  t_len = len(txt)
  p_len = len(pat)
  iterations = 0

  for i in xrange(t_len - p_len + 1):
    match = False
    for j in xrange(p_len):
      iterations += 1
      match = txt[i+j] == pat[j]
      if not match:
        break
    if match and j == p_len - 1:
      print "Found at index: " + str(i)

  print iterations

# txt = "AABAACAADAABAAABAA"
# pat = "AABA"

txt = "AAAAABAAABA"
pat = "AAAA"

# txt = "BBBABABBBB"
# pat = "BBBB"

txt = "HABHHHABCD"
pat = "ABCD"

txt = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
pat = 'AAAAAAAAB'

txt = "AABAACAADAABAAABAA"
pat =  "AABA"

search (pat, txt)