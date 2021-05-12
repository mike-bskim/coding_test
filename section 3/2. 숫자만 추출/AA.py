import sys
# sys.stdin = open('in1.txt', 'rt')

cnt = (input())
# print(cnt)
result = 0
result_cnt=0

for i in range(len(cnt)):
    # print(cnt[i], ord(cnt[i]))
    if(ord(cnt[i]) >= 48) and (ord(cnt[i]) <= 57):
        result = result*10 + int(cnt[i])

# print(result)

for i in range(1, result+1):
    if result%i == 0:
        result_cnt += 1
        # print('약수는:', i, result_cnt)

print(result)
print(result_cnt)