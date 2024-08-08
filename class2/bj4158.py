answer_list = []
num_list = []
i = 1

while i:
    nums = list(input().split(" "))
    num_sort=sorted(nums)
    num_list.append(num_sort)
    
    if nums == [0,0,0]:
        i = 0
    
if (int(num_list[0][]))*(int(num_sort[0])) + (int(num_sort[1]))*(int(num_sort[1])) == (int(num_sort[2]))*(int(num_sort[2])):
    answer_list.append("right")
else:
    answer_list.append("wrong")

for i in answer_list:
    print(i)