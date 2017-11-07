 stack = [root]
 stack_next = []
 direction = 'left'
 
 while len(stack) or len(next_stack):
    if len(stack) == 0 and len(next_stack) > 0:
        stack = next_stack
        next_stack = []
        direction = 'left' if direction == 'right' else 'right'
     
    curr = stack.pop()
     
    if direction == 'left':
         stack_next.append(curr.left)
         stack_next.append(curr.right)
    else:
        stack_next.append(curr.right)
        stack_next.append(curr.left)