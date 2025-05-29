
'''
Rules:
1. Only one disk may be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a disk that is smaller than it.
'''

a = [6,5,4,3,2,1]
b = []
c = []

def move(source : list[int], destination : list[int]):
    assert len(source) > 0, "Source must not be empty"
    assert len(destination) == 0 or destination[-1] > source[-1], "Rule 3, Cannot place bigger disk on smaller"
    destination.append(source.pop())

def is_success():
    return len(a) == 0 and (len(b) == 6 or len(c) == 6)


def solution(source : list[int], destination : list[int], extra : list[int], n):
    if n == 1:
        move(source, destination)
        return

    solution(source, extra, destination, n-1)
    move(source, destination)
    solution(extra, destination, source, n-1)

if __name__ == '__main__':
    solution(a, b, c, 6)
    assert is_success() == True, "Should be solved by now"
    print("a:", a, "b:", b, "c:", c)
