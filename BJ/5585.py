# 거스름돈 = 1000원 - 입력받은 값(지불할 돈)
N = 1000 - int(input())
answer = 0

# 내림차순된 잔돈 리스트를 반복해 수행
for ex in [500, 100, 50, 10, 5, 1]:
    # 거스름돈이 잔돈(ex)보다 작으면 continue
    if N < ex:
        continue

    # 거스름돈을 잔돈으로 나눈 몫을 정답에 더해주고, 나머지를 잔돈으로 바꿈
    answer += N // ex
    N %= ex
    # 거스름돈이 0이면 반복문 종료
    if N == 0:
        break

print(answer)