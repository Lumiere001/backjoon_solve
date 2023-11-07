def facplus(n):
    if n <= 0:
        return 0
    else:
        sum = n + facplus(n-1)
        return sum

num = int(input())
total_sum = []

for k in range(num):
    letter = list(input())
    count = 0
    sum_list = []

    if letter[-1] == 'X':
        for i in letter:
            if i == 'O':
                count = count + 1
            else:
                result = facplus(count)
                count = 0
                if result > 0:
                    sum_list.append(result)
                
    elif letter[-1] == 'O':
        letter.append('X')
        for i in letter:
            if i == 'O':
                count = count + 1
            else:
                result = facplus(count)
                count = 0
                if result > 0:
                    sum_list.append(result)

    total_sum.append(sum(sum_list))

for j in total_sum:
    print(j)