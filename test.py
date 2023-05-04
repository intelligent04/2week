s = input()  # 문자열 S 입력받기
li = []  # 접미사를 담을 리스트 초기화

# 문자열 S의 모든 접미사를 구해서 li 리스트에 추가
for i in range(len(s)):
    li.append(s[i:])

# 접미사를 사전순으로 정렬하고 출력
li.sort()
for a in li:
    print(a)

