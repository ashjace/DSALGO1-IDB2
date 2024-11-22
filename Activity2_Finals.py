from PositionalList import PositionalList
from LinkedStack import LinkedStack
def evaluate_postfix(expression):

    stack = LinkedStack()
    tokens = expression.split()

    for token in tokens:
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
        else:
            stack.push(float(token))

    return stack.pop()


def insertion_sort(positional_list):

    if len(positional_list) <= 1:
        return

    marker = positional_list.after(positional_list.first())
    while marker is not None:
        pivot = marker.element()
        walk = marker


        while (walk != positional_list.first() and
               positional_list.before(walk).element() > pivot):

            walk._node._element = positional_list.before(walk).element()
            walk = positional_list.before(walk)


        walk._node._element = pivot
        marker = positional_list.after(marker)


def insertion_sort_descending(positional_list):

    if len(positional_list) <= 1:
        return

    marker = positional_list.after(positional_list.first())
    while marker is not None:
        pivot = marker.element()
        walk = marker

        while (walk != positional_list.first() and
               positional_list.before(walk).element() < pivot):
            walk._node._element = positional_list.before(walk).element()
            walk = positional_list.before(walk)

        walk._node._element = pivot
        marker = positional_list.after(marker)


def print_list(positional_list):

    current = positional_list.first()
    elements = []
    while current is not None:
        elements.append(str(current.element()))
        current = positional_list.after(current)
    print(" ".join(elements))


if __name__ == "__main__":
    postfix_expr = "5 2 + 8 3 - * 4 /"
    result = evaluate_postfix(postfix_expr)
    print(f"Postfix evaluation result: {result}")

    numbers = [1, 72, 81, 25, 65, 91, 11]


    pos_list = PositionalList()
    for num in numbers:
        pos_list.add_last(num)

    print("Original list:", end=" ")
    print_list(pos_list)


    insertion_sort(pos_list)
    print("Ascending order:", end=" ")
    print_list(pos_list)

    insertion_sort_descending(pos_list)
    print("Descending order:", end=" ")
    print_list(pos_list)


