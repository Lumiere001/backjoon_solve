nums = []

for i in range(3):
    num = input()
    nums.append(num)
    
T_num = int(nums[0]) + int(nums[1]) - int(nums[2])
T_char = int(nums[0] + nums[1]) - int(nums[2])

print(T_num)
print(T_char)