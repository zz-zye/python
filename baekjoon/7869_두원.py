from math import sqrt, pi

def solve(x1, y1, r1, x2, y2, r2):
    # 두 원 중심 사이 거리
    d = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    # 1-1. 두 원 안 만나는지 판정
    if r1 + r2 <= d:
        return 0
    # 1-2. 원 하나가 포함되는지 판정
    if d + r1 <= r2:
        return pi * r1 * r1
    if d + r2 <= r1:
        return pi * r2 * r2

    # 2. 피타고라스로 교점까지의 거리 구하기
    # 중심을 각각 A와 B, 교점 하나를 C라 하고, C에서 선분 AB에 내린 수선의 발을 H라 하자.
    # AH = x, BH = d-x
    # 피타고라스에 의해 r1**2 - x**2 == r2**2 - (d-x)**2
    # 2dx = r1**2 - r2**2 + d**2
    ah = sqrt((r1**2 - r2**2 + d**2) / (2*d))
    ch = sqrt(r1**2 - ah**2 )**(1/2)

    
    # 3. 원이 겹친 모양에 따라서 넓이 구하는게 달라질 것 같아요 ... -전제영-


x1, y1, r1, x2, y2, r2 = map(float, input().split())
answer = solve(x1, y1, r1, x2, y2, r2)
print('{.3f}'.format(answer))