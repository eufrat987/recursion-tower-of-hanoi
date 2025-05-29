
'''
Rules:
1. Only one disk may be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a disk that is smaller than it.
'''

# params:
N = 6
show_moves = True
step_count = 1

a = [i for i in range(N,0,-1)]
b = []
c = []

def move(source : list[int], destination : list[int]):
    assert len(source) > 0, "Source must not be empty"
    assert len(destination) == 0 or destination[-1] > source[-1], "Rule 3, Cannot place bigger disk on smaller"
    destination.append(source.pop())
    if show_moves:
        show_rodes(count_move=show_moves)

def is_success():
    return len(a) == 0 and (len(b) == N or len(c) == N)

def show_rodes(count_move = False):
    global step_count
    if count_move:
        print("step:", step_count, "| a:", a, "b:", b, "c:", c)
        step_count += 1
    else:
        print("a:", a, "b:", b, "c:", c)

def solution(source : list[int], destination : list[int], extra : list[int], n):
    if n == 1:
        move(source, destination)
        return

    solution(source, extra, destination, n-1)
    move(source, destination)
    solution(extra, destination, source, n-1)

if __name__ == '__main__':
    print("Tower of hanoi size:", N)
    show_rodes()

    solution(a, b, c, N)
    assert is_success() == True, "Should be solved by now"

    show_rodes()
