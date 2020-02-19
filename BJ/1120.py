# 문자열 A, B를 입력받음
A, B = input().split()

# 문자열 A와 B의 길이 차이만큼 이동하면서 비교
mv_cnt = len(B) - len(A)

# 최소값을 찾기 위해 비교 과정이 들어가므로, 최대값인 len(A) 로 설정
answer = len(A)

# A의 문자열을 B 문자열의 한칸씩 오른쪽으로 이동하면서 비교
# min 은 문자열 비교 후 차이를 카운트
for idx in range(mv_cnt + 1):
    min = 0

    # A의 문자열 길이만큼 B_tmp 와 차이를 비교
    for i in range(len(A)):
        if A[i] != B[idx:len(A) + idx][i]:
            min += 1
        # min (현재차이) 의 값이 answer 보다 크거나 같으면 최소값이 아니므로 break
        if answer <= min:
            break

    # min 의 값이 answer 보다 작으면 answer 값을 min 값으로 변경
    if min < answer:
        answer = min
        # answer 가 0일 경우 가장 최소값이므로 break
        if answer == 0:
            break

print(answer)
