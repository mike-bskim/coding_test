import sys
# sys.stdin = open('in1.txt', 'rt')

cnt = int(input())
#tmp=[]
#tmp_reverse=[]
#
#for i in range(cnt):
#  tmp.append(input())
#  tmp[i]=tmp[i].upper()
#  tmp_list = list(tmp[i])
#  tmp_list.reverse()
#  tmp_str = ''.join(tmp_list)
#  tmp_reverse.append(tmp_str)
#
#for i in range(cnt):
#  if tmp[i] == tmp_reverse[i]:
#    print('#{} {}'.format(i+1, 'YES'))
#  else:
#    print('#{} {}'.format(i+1, 'NO'))
  
for i in range(cnt):
    s=input()
    s=s.upper()

    for j in range(len(s)//2):
        if s[j] != s[-j-1]:
            print('#{} {}'.format(i+1, 'NO'))
            break
    else:
        print('#{} {}'.format(i+1, 'YES'))

# for i in range(cnt):
#     s=input()
#     s=s.upper()
#     # print(s, s[::-1])

#     if s == s[::-1]:
#         print('#{} {}'.format(i+1, 'YES'))
#     else:
#         print('#{} {}'.format(i+1, 'NO'))

