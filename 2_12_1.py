score1 = []
score2 = []

score_list = [score1, score2]
for score in score_list:
    i = total = 0
    frame = []          # (프레임 점수, 결과)
    for first, second in score:     # 1회, 2회 쓰러뜨린 핀의 수
        f_total = first + second
        next_first, next_second = score[i+1]
        if first == 10:
            result = 'STRIKE'
            f_total += next_first + next_second
            if i != 9 and next_first == 10:     # 더블을 친 경우
                next_next_first, next_next_second = score[i+2]
                f_total += next_next_first
        elif (first + second) == 10:
            result = 'SPARE'
        else:
            result = 'NONE'

        total += f_total
        frame.append((f_total, result))
        i += 1
        if i == 10:
            break

    print(frame)
    print("Total = ", total)
    print()