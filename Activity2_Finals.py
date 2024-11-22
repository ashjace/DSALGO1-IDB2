from PositionalList import PositionalList
from LinkedStack import LinkedStack
def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
        else:
            stack.append(float(token))

    return stack[0]


def insertion_sort(numbers, descending=False):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        if descending:
            while j >= 0 and numbers[j] < key:
                numbers[j + 1] = numbers[j]
                j -= 1
        else:
            while j >= 0 and numbers[j] > key:
                numbers[j + 1] = numbers[j]
                j -= 1

        numbers[j + 1] = key

    return numbers


if __name__ == "__main__":

    postfix_expr = "5 2 + 8 3 - * 4 /"
    result = evaluate_postfix(postfix_expr)
    print(f"Postfix evaluation result: {result}")

    numbers = [1, 72, 81, 25, 65, 91, 11]
    print("Original list:", numbers)

    sorted_ascending = insertion_sort(numbers.copy())
    print("Ascending order:", sorted_ascending)

    sorted_descending = insertion_sort(numbers.copy(), descending=True)
    print("Descending order:", sorted_descending)