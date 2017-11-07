def match(a, b):
  return 0 if a == b else 1

# hello
# heleo

# hellor
# heleo

def get_match(text, pattern, i, j):

  if i == 0: return j
  if j == 0: return i

  tries = [
    get_match(text, pattern, i - 1, j - 1) + match(text[i], pattern[j]), # match
    get_match(text, pattern, i, j - 1) + 1, # insertion
    get_match(text, pattern, i - 1, j) + 1  # deletion
  ]

  return min(tries)

els = [
  ('vv', 'bb'),
  ('heyae', 'heyar'),
  ('zbcdefghij', 'abcdefghij'),
]

for el in els:
  print get_match(el[0], el[1], len(el[0]) - 1, len(el[1]) - 1)
