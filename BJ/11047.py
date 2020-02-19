N, K = map(int, input().split())

answer = 0

# 동전 종류를 입력받을 리스트 생성
coins = []

# coins 에 입력받은 동전 종류를 append
for idx in range(N):
    coins.append(int(input()))

# 큰 수부터(뒤에서부터) K 값을 나눈 몫을 answer 에 더해주고 나머지는 K로 저장
for coin in coins[::-1]:
    if coin <= K:
        answer += K // coin
        K %= coin

        # K가 0이면 반복문 종료
        if K == 0:
            break

print(answer)