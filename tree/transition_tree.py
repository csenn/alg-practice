
# art, atom
# {(0, 'a'):1, (1, 'r'):2, (2, 't'):3, (1, 't'):4, (4, 'o'):5, (5, 'm'):6 }

def build_tree(arr):

  result = {}
  new_state = 0

  for word in arr:
    state = 0

    for i in range(len(word)):
      next_node = result.get((state, word[i]), None)
      if next_node == None:
        break
      state = next_node

    for letter in word[i:]:
      new_state += 1
      result[(state, letter)] = new_state
      state = new_state

  return result

arr = ['art', 'atom', 'tree']
print build_tree(arr)


# 0 ['a'] 1
# 1 ['r'] 2
# 2 ['t'] 3

# 1 ['t'] 4
# 4 ['o'] 5
# 5 ['m'] 6

# 0 ['t'] 7
# 7 ['r'] 8
# 8 ['e'] 9
# 9 ['e'] 10

