ans = []
n = 0

while n != 1:
    nums = input().split()
    nums = sorted(map(int, nums))
    if nums[0] == 0 and nums[1] == 0 and nums[2]==0:
        n = 1   # 0 0 0 이 들어온 것을 판별하기 위한 임의의 상수
    else:
        if nums[0]**2 + nums[1]**2 == nums[2]**2:
            ans.append("right")
        else:
            ans.append("wrong")
    
# 결과 출력
for i in ans:
    print(i)