num = 1
num_list = []
answer_list = []

while num != 0:
    num = int(input())
    num_list.append(num)

num_list.remove(0)

for i in num_list:
    num_str = str(i)
    if num_str == num_str[::-1]: 
        answer_list.append("yes")
    else:
        answer_list.append("no")

for j in answer_list:
    print(j)