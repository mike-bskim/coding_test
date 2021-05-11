import sys
# sys.stdin = open('input.txt', 'rt')

L=int(input())
arr=list(map(int, input().split()))
m=int(input())
cnt=[0]*101
maxH=float('-inf')
minH=float('inf')

# tmp = arr.sorted()
# print(tmp)

for x in arr:
    cnt[x]+=1
    if x>maxH: maxH=x
    if x<minH: minH=x


# print(minH, maxH)
# for i in range(len(cnt)):
#   # print(cnt[i], end=' ')
#   if i%10 == 0:
#     print()

for _ in range(m):
    # print('minH({}), maxH({})'.format(minH, maxH))
    if cnt[maxH]==1:     # 최대값이 1개일때.
        cnt[maxH]-=1     # 최대값이 1개이므로 최대값 삭제효과
        maxH-=1          # 최대값 인덱스 줄이기
        cnt[maxH]+=1     # 줄어든 인덱스로 최대값 이동함.
    else:                # 최대값이 1개 이상일때.
        cnt[maxH]-=1     # 최대값 개수 -1
        cnt[maxH-1]+=1   # 최대값 인덱스 줄이고 개수 추가. 다름 최대값 그룹에 추가하는 효과.

    if cnt[minH]==1:
        cnt[minH]-=1
        minH+=1
        cnt[minH]+=1
    else:
        cnt[minH]-=1
        cnt[minH+1]+=1
    
print(maxH-minH)