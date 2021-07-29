import random
import Structures.Stack as Stack

def gen_list(n, min_, max_):
    output = []

    for i in range(n):
        output.append(random.randint(min_, max_))

    return output


def gen_array(size):
    arr = [0]

    n = 0
    for i in range(size - 1):
        n += random.randint(1, 5)
        arr.append(n)

    return arr

# for the towers of hanoi problem
def gen_towers(disks):
    s1 = Stack.stack()
    s2 = Stack.stack()
    s3 = Stack.stack()
    stack_list = [s1, s2, s3]

    for i in range(disks, 0, -1):
        stack_list[0].push(i)

    return stack_list