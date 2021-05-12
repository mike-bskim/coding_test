import random
# 병합정렬
def Dsort(lt, rt):
  if lt<rt:
    mid = (lt + rt) // 2
    Dsort(lt,mid)
    Dsort(mid+1, rt)
    p1=lt
    p2=mid+1
    tmp=[]
    while p1<=mid and p2<=rt:
      if arr[p1]<arr[p2]:
        tmp.append(arr[p1])
        p1+=1
      else:
        tmp.append(arr[p2])
        p2+=1
    if p1<=mid:
      tmp = tmp + arr[p1:mid+1]
    if p2<=rt:
      tmp = tmp + arr[p2:rt+1]
    for i in range(len(tmp)):
      arr[lt+i] = tmp[i]




def DDsort(lt, rt):
  if lt<rt:
    mid=(lt+rt)//2
    DDsort(lt, mid)
    DDsort(mid+1, rt)
    p1=lt
    p2=mid+1
    tmp=[]
    while p1<=mid and p2<=rt:
      if arr[p1]<arr[p2]:
        tmp.append(arr[p1])
        print('arr[{}]:{}, arr[{}]:{}, tmp:{}'.format(p1, arr[p1], p2, arr[p2], tmp))
        p1+=1
      else:
        tmp.append(arr[p2])
        print('arr[{}]:{}, arr[{}]:{}, tmp:{}'.format(p1, arr[p1], p2, arr[p2], tmp))
        p2+=1
    if p1<=mid:
      tmp = tmp + arr[p1:mid+1]
    if p2<=rt:
      tmp = tmp + arr[p2:rt+1]
    for i in range(len(tmp)):
      arr[lt+i] = tmp[i]
    print('>>>arr:', arr)


if __name__ == "__main__":
  # arr=[random.randint(1,1000) for _ in range(8)]
  arr=[23,11,45,36,15,67,33,21]
  print('Before sort : ', end=' ')
  print(arr)

  DDsort(0,len(arr)-1)
  print()

  print('After sort : ', end=' ')
  print(arr)
