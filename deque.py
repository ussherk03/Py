if __name__ == '__main__':
    N = int(input())

    from collections import deque

    d = deque([])

    for _ in range(N):
        line = input().split()
        getattr(d, line[0]) (*[line[1]] if len(line) > 1 else [])

    print(' '.join(d))

''''
----Test Cases ---------
6
append 1
append 2
append 3
appendleft 4
pop
popleft
'''

