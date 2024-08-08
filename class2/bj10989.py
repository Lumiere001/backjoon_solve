import sys

list_num = []
times = int(sys.stdin.readline())

for _ in range(times):
    nums = int(sys.stdin.readline())
    list_num.append(nums)

list_num = sorted(list_num)

for i in list_num:
    print(i)
    
# 메모리 초과 됨... 메모리 초과를 줄일 수 있는 방법을 알아야 함...