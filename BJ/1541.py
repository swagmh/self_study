# 식을 입력받음
exp = input()

# 식에 - 가 없는 경우, '+' 기준으로 split 후 int 로 type 변경해 모두 더한 값을 answer 로 지정
if '-' not in exp:
    answer = sum(map(int, exp.split('+')))

# 식에 - 가 있는경우, 가장 첫번째 '-'의 index 를 찾아 전까지를 +, 뒤에는 모두 - 로 answer 값에 추가.
# split 시 '-' 로만 구성되어 있을 수 있으므로 '-'를 '+'로 replace 후 '+' 로 split
else:
    split_num = exp.index('-')
    answer = sum(map(int, exp[:split_num].split('+'))) - sum(map(int, exp[split_num+1:].replace('-', '+').split('+')))
    
print(answer)


