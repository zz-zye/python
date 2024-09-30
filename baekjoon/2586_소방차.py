n_pump, n_truck = map(int, input().split())
pumps = list(map(int, input().split()))
trucks = list(map(int, input().split()))

# 1. 리스트 합치기
# 펌프와 소방차가 같은 위치에 있으면 무시하기 (정답에 영향 없으므로)

INF = 1234567890
pumps.append(INF)
trucks.append(INF)

PUMP = 0
TRUCK = 1
pump_i = 0
truck_i = 0

merged = []
while pump_i <= n_pump and truck_i <= n_truck:
    if pumps[pump_i] == trucks[truck_i]: # 스킵
        truck_i += 1
        pump_i += 1
    elif pumps[pump_i] < trucks[truck_i]:
        merged.append((pumps[pump_i], PUMP))
        pump_i += 1
    else:
        merged.append((trucks[truck_i], TRUCK))
        truck_i += 1


# 2. 탐욕법으로 미리 짝짓고, 필요 없는 펌프 구하기

# 2-1. 미리 짝짓기
# 어떤 트럭의 '왼쪽에 있는 트럭의 개수' = x,
#             '왼쪽에 있는 펌프의 개수' = y일 때
# x >= y면 이 트럭은 무조건 오른쪽으로 연결됨.
# (왼쪽과 오른쪽을 반대로 해도 참)

# 2-2. 필요 없는 펌프 구하기
# 어떤 펌프를 기준으로 '왼쪽에 있는 트럭들을 모두 오른쪽으로 연결'하고,
#                      '오른쪽에 있는 트럭들을 모두 왼쪽으로 연결'했을 때
# 해당 펌프가 아무 트럭과도 짝지어지지 않으면 그 펌프는 지워도 됨

# 2-1과 2-2를 스택을 사용하여 한 번에 체크 가능

is_paired = [False] * len(merged) # 짝지어진 펌프와 소방차 체크
not_paired_left = [False] * len(merged) # 트럭에서 왼쪽으로 짝지어지지 않은 펌프 체크
not_paired_right = [False] * len(merged) # 트럭에서 오른쪽으로 짝지어지지 않은 펌프 체크

def pair_stack(from_right: bool):
    answer = 0
    stack = [] # (i, element) 꼴로 저장

    r = range(len(merged))
    if from_right:
        r = reversed(r)
    
    for i in r:
        elem = merged[i]
        if elem[1] == PUMP:
            if len(stack) > 0 and stack[-1][1][1] == TRUCK:
                stack.pop()
            else:
                stack.append((i, elem))
        else:
            if len(stack) > 0 and stack[-1][1][1] == PUMP:
                pump_i, pump = stack.pop()
                is_paired[pump_i] = True
                is_paired[i] = True
                answer += abs(pump[0] - elem[0])
            else:
                stack.append((i, elem))
    
    # 스택에 남아있는 것이 짝지어지지 않은 펌프들임
    for i, pump in stack:
        if from_right:
            not_paired_right[i] = True
        else:
            not_paired_left[i] = True
    
    return answer # 짝지어진 길이 합

# 왼쪽에서 한 번, 오른쪽에서 한 번 돌며 체크
answer = pair_stack(False) + pair_stack(True)

print(is_paired)
print(not_paired_left)

# 3. 