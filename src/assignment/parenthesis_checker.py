def bracket_pair_checker(brackets: str) -> bool:
    stack: list[str] = []
    for bracket in brackets:
        if bracket in '{[(':
            stack.append(bracket)
        if bracket in ']})':
            peek = stack[-1]
            if bracket == ')' and peek == '(':
                stack.pop()
            elif bracket == ']' and peek == '[':
                stack.pop()
            elif bracket == '}' and peek == '{':
                stack.pop()
            else:
                return False
    return len(stack) == 0
    # if len(stack) == 0:
    #     return True
    # print('True')
    # else:
    # return False
    # print('False')


print(bracket_pair_checker('[{()}]'))
print(bracket_pair_checker('[{()}}'))
print(bracket_pair_checker('{())[]()}'))


def add(a: int = 2, b: str = 'color') -> tuple[int, str]:
    return a, b


print(add(3, '3'))
print(add(3))
print(add())
print(add(a=5, b='you'))


def mutable_ish(a=None):
    if a is None:
        a = []
    a.append('python')
    return a


print(mutable_ish())
print(mutable_ish([1, 2, 3, 4]))


# tuple packing
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


lst = [7, 9, 3, 10, 56]
print(add(*[1, 2, 3, 4, 5]))
print(add(*lst))


def true_false(age):
    if age >= 18:
        return True
    return False


def dict_pack_unpack(*args, **kwargs):
    print("kwargs", kwargs)
    print("Args", args)


dict_pack_unpack(4, 5, "goal", name="shola", age=45, sex="male")


def sub(a, b, /, c):
    print(a, b, c)


sub(1, 3, c=4)

d = dict(a=1, b=2, c=4)
print(d)
dict_pack_unpack(**d)
