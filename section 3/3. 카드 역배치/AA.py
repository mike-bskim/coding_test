import sys
# sys.stdin = open('in1.txt', 'rt')
card = [str(i) for i in range(1,21)]
# print(card)

for i in range(10):
    a, b = map(int, input().split())
    size = b-a+1
    for j in range(size//2):
        card[a-1+j], card[b-1-j] = card[b-1-j], card[a-1+j]

print(*card)
# print(' '.join(card))

# print()
# card1 = list(range(1,21))
# print(*card1)
# # print(' '.join(card1))
