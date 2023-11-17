# 문자열 입력 받고 리스트로 만들기
# 각 리스트의 값과 인덱스 값 매칭하기
# 아스킷 코드 이용해서 A-Z까지 아래 구문 반복문 돌리기
    # if를 이용해서 특정 알파벳이 있는가 판별
    # 알파벳이 없다면 -1 출력하고 다음으로 넘어가기
    # 알파벳이 있다면 해당 알파벳의 번호가 여러개인지 하나인지 판별
        # 알파벳이 하나라면 인덱스 번호 출력
        # 알파벳이 두 개 이상이라면 가장 작은 인덱스 번호 출력

letter = list(input())
index_value_dict = {value: index for index, value in enumerate(letter)}

for i in range(97, 123):
    if any(chr(i) in key for key in index_value_dict):
        if letter.count(chr(i)) == 1: # 1개 있는 것
            print(index_value_dict[chr(i)], end=" ")
        else: # 2개 이상 있는 것
            for j in letter:
                if j == chr(i):
                    print(letter.index(j), end=" ")
                else:
                    continue
                break
                    
    else:
        print("-1", end = " ")