total = 0   # 총 점수를 저장할 변수
frame = 0   # 프레임 수
strike = 0  # 스트라이크를 친 횟수
spare = 0   # 스페어를 친 횟수
p_frame = []    # 프레임마다 결과를 출력할 리스트
while True:
    frame += 1
    first, second = map(int, input().split())
    if frame == 10:        # 10 프레임의 경우
        if first == 10:     # 10 프레임에서 스트라이크를 친 경우
            if strike == 2:    # 8 프레임에서 스트라이크를 친 경우
                total += 30
                strike -= 1
                p_frame[7] = (10, 0, 'X', 30)
            elif spare == 1:  # 9 프레임에서 스페어를 친 경우
                total += 10 + first
                spare = 0
                p_frame[8] = (p_frame[8][0], p_frame[8][1], '/', 10 + first)   # 9 프레임의 점수
            b_first, b_second = map(int, input().split())
            if strike == 1:   # 9 프레임에서 스트라이크를 친 경우
                total += 20 + b_first
                p_frame[8] = (10, 0, 'X', 20 + b_first)   # 9 프레임의 점수
                strike = 0
                print(p_frame)
            total += 10 + b_first + b_second
            p_frame.append((10, 0, 'X', 10 + b_first + b_second))
            p_frame.append((b_first, b_second))
        # 10 프레임에서 스트라이크를 치지 않은 경우
        if strike == 2:  # 8 프레임에서 스트라이크를 친 경우
            total += 20 + first
            strike -= 1
            p_frame[7] = (10, 0, 'X', 20 + first)
        if strike == 1:  # 9 프레임에서 스트라이크를 친 경우
            total += 10 + first + second
            p_frame[8]  = (10, 0, 'X', 10 + first + second)
        elif spare == 1:  # 9 프레임에서 스페어를 친 경우
            total += 10 + first
            spare = 0
            p_frame[8] = (p_frame[8][0], p_frame[8][1], '/', 10 + first)
        print(p_frame)

        if first + second == 10 and second != 0:  # 10 프레임에서 스페어를 친 경우
            p_frame.append((first, second, '/', ' '))
            print(p_frame)
            b_first = int(input())
            total += 10 + b_first    # 10 프레임에서 스페어를 친 점수
            p_frame[-1] = (first, second, '/', 10 + b_first)
            print(p_frame)
            p_frame.append(b_first, 0)
        elif first + second != 10:
            total += first + second   # 10 프레임에서 아무것도 치지 못 한 점수
            p_frame.append((first, second, '-', first+second))
            print(p_frame)
        break

    # 10 프레임이 되기 전 계산
    if strike == 2 and first != 10:   # 스트라이크를 2번 쳤던 경우
        total += 20 + first
        strike = -1
        p_frame[-2] = (10, 0, 'X', 20 + first)

    if strike == 1 and first != 10:     # 직전에 스트라이크를 친 경우
        total += 10 + first + second
        strike = 0
        p_frame[-1] = (10, 0, 'X', 10 + first + second)

    if spare == 1:    # 직전에 스페어를 친 경우
        total += 10 + first
        spare = 0
        p_frame[-1] = (p_frame[-1][0], p_frame[-1][1], '/', 10 + first)

    if first == 10:     # 스트라이크를 친 경우
        strike += 1
        p_frame.append((10, 0, 'X', ' '))
    elif first + second == 10:  # 스페어를 친 경우
        spare = 1
        strike = 0
        p_frame.append((first, second, '/', ' '))
    else:
        strike = 0
        spare = 0
        total += first + second
        p_frame.append((first, second, '-', first+second))

    if strike == 3:       # 스트라이크를 3번 친 경우
        strike -= 1
        total += 30
        p_frame[-3] = (10, 0, 'X', 30)
    print(p_frame)

print("Total = %d" % (total))