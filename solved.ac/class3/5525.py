from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())
S = stdin.readline().rstrip()

answer = 0
count = 0
i = 1
while i < M - 1:
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":
        count += 1
        if count == N:
            count -= 1
            answer += 1
        i += 1
    else:
        count = 0
    i += 1

print(answer)