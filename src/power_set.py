def find_power_set(S, s, n):
    if n == 0:
        print(s)
        return

    s.append(S[n-1])
    find_power_set(S, s, n-1)
    s.pop()
    find_power_set(S, s, n - 1)


def find_power_set2(S):
    N = int(2 ** len(S))
    s = list()

    for i in range(N):
        for j in range(len(S)):
            if i & (1 << j):
                s.append(S[j])
        print(s)
        s.clear()


if __name__ == '__main__':
    S = [1, 2, 3]

    s = []
    find_power_set2(S)