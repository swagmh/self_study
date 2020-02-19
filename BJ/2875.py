# 입력을 받음 (남학생, 여학생, 인턴쉽 참여 인원)
N, M, K = map(int, input().split())

# 여학생 + 남학생 - 인턴쉽 참여 인원의 값이 3 미만이면 정답은 0
if N+M-K < 3:
    answer = 0

# 정답을 남/녀별 팀 구성이 가능한 최대값 중 최소값으로 지정
# 위의 정답의 팀 구성원만큼 제외한 남은 인원은 K(인턴쉽 참여 인원)에서 빼줌
else:
    answer = min(N // 2, M)
    K -= (M - answer) + (N - answer * 2)
    # K가 0 미만이 될때까지, 팀을 하나 줄이고 K 값에 3을 빼줌
    while 0 < K:
        answer -= 1
        K -= 3

print(answer)
