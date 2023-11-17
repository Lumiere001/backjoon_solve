import sys

times = int(input())
num_list = []

for i in range(times):
    num = int(sys.stdin.readline().strip())
    num_list.append(num)

print("\n".join(map(str, sorted(num_list))))