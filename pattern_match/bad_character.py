def build_lookup(pattern, pattern_len):
  my_dict = {}
  for i in range(pattern_len):
    letter = pattern[i]
    my_dict[letter] = i
  return my_dict

def search(text, pattern):
  text_len = len(text)
  pattern_len = len(pattern)

  lookup = build_lookup(pattern, pattern_len)

  i = 0

  iterations = 0

  while i < text_len - pattern_len + 1:

    j = i + pattern_len - 1
    k = pattern_len - 1

    while k > 0:
      iterations += 1
      if text[j] != pattern[k]:
        if text[j] in lookup:
          x = k - lookup[text[j]]
          i += x if x > 0 else 1
        else:
          i += pattern_len - 1
        break

      elif k == 1:
        print 'Found index at :', i
        i += 1
        break

      else:
        j -= 1
        k -= 1

  print iterations

txt = "AABAACAADAABAAAAABAAAABAW"
# pat = "AABAAAABAR"
pat = "wwwwwwww"

# txt = "ABAAABCD"
# pat = "ABC"
search(txt, pat)