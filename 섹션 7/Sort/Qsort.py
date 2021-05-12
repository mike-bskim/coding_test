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




def QQsort(lt, rt):
  if lt<rt:
    pos=lt
    pivot=arr[rt]
    # print('****', pos, pivot, arr[lt:rt+1])
    for i in range(lt, rt):
      if arr[i]<pivot:
        # print(arr[pos], arr[i])
        arr[pos], arr[i] = arr[i], arr[pos]
        pos+=1
    arr[pos], arr[rt] = arr[rt], arr[pos]
    # print('>>>', lt, pos, rt, arr[lt:rt+1])
    QQsort(lt, pos-1)
    QQsort(pos+1, rt)
    


if __name__ == "__main__":
  arr=[random.randint(1,1000) for _ in range(10)]
  # arr=[45,21,23,36,15,67,11,60,20,33]
  print('Before sort : ', end=' ')
  print(arr)

  QQsort(0,len(arr)-1)
  # QQsort(0,4)
  # QQsort(6,9)
  print()

  print('After sort : ', end=' ')
  print(arr)
