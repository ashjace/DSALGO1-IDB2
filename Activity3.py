from Activity3Midterm_Cornejo import ArrayStack as Stack
def is_valid_expression(expression):
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            stack.pop()

    return not stack
expressions = ["( )(( )){([( )])}", "((( )(( )){([( )])}))", " )(( )){([( )])}", "({[])}", "("]
for exp in expressions:
    print(f"{exp}: {is_valid_expression(exp)}")

def reverse_file_lines(filename):
    stack = []
    with open(filename, 'r') as file:
        for line in file:
            stack.append(line.strip())
    with open(filename, 'w') as file:
        while stack:
            file.write(stack.pop() + '\n')
reverse_file_lines('output')