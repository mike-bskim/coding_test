import sys
# sys.stdin = open('in2.txt', 'rt')

cnt = int(input())
# cnt = 10
# print(cnt)
r_list = [0]*(cnt+1)
# print(len(r_list))
r_cnt=0
r2_list = []

for i in range(2, cnt+1):
  if r_list[i]==0:
    r_cnt += 1
    for j in range(i+i, cnt+1, i):
      r_list[j] += 1
    # print(i, j, r_list, r_cnt)

# print(r_list, r_cnt)
for i in range(2, cnt+1):
  if r_list[i] == 0:
    r2_list.append(i)
# print(r2_list) # 소수 리스트.
print(r_cnt)


# print(len(r_list))

