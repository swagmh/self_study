# 숫자를 입력받음
N = int(input())

# 초기 answer 의 값을 -1로 설정
answer = -1

# N킬로그램을 5로 나눈 몫의 값을 five_cnt 로 저장
# N은 5로 나눈 나머지 값으로 변경
five_cnt = N // 5
N = N % 5

# 최대 5킬로그램 봉지 수 에서부터 1봉지 씩 감소시켜가면서 0봉지때까지 반복
for add in range(five_cnt, -1, -1):
    # 현재 남은 설탕 킬로그램이 3으로 나누어 떨어질때 break
    if N % 3 == 0:
    # 5킬로그램의 봉지 수 + 3킬로그램의 봉지 수
    answer = add + N // 3
    break
    # 5킬로그램 봉지 수를 하나 줄이고 남은 설탕 킬로그램에 5킬로그램을 더해준다.
    N += 5

print(answer)