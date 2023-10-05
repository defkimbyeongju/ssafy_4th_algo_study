def clockwise(gear):
    save = gear[7]
    for i in range(7, 0, -1):
        gear[i] = gear[i-1]
    gear[0] = save


def counter_clockwise(gear):
    save = gear[0]
    for i in range(7):
        gear[i] = gear[i + 1]
    gear[7] = save


first = list(input())
second = list(input())
third = list(input())
fourth = list(input())
K = int(input())
for _ in range(K):
    n, d = map(int, input().split())
    f_s = bool(first[2] != second[6])
    s_t = bool(second[2] != third[6])
    t_f = bool(third[2] != fourth[6])
    if n == 1:
        if d == 1:
            clockwise(first)
        else:
            counter_clockwise(first)
        if f_s:
            if d == 1:
                counter_clockwise(second)
            else:
                clockwise(second)
            if s_t:
                if d == 1:
                    clockwise(third)
                else:
                    counter_clockwise(third)
                if t_f:
                    if d == 1:
                        counter_clockwise(fourth)
                    else:
                        clockwise(fourth)
    elif n == 2:
        if d == 1:
            clockwise(second)
        else:
            counter_clockwise(second)
        if f_s:
            if d == 1:
                counter_clockwise(first)
            else:
                clockwise(first)
        if s_t:
            if d == 1:
                counter_clockwise(third)
            else:
                clockwise(third)
            if t_f:
                if d == 1:
                    clockwise(fourth)
                else:
                    counter_clockwise(fourth)
    elif n == 3:
        if d == 1:
            clockwise(third)
        else:
            counter_clockwise(third)
        if s_t:
            if d == 1:
                counter_clockwise(second)
            else:
                clockwise(second)
            if f_s:
                if d == 1:
                    clockwise(first)
                else:
                    counter_clockwise(first)
        if t_f:
            if d == 1:
                counter_clockwise(fourth)
            else:
                clockwise(fourth)
    elif n == 4:
        if d == 1:
            clockwise(fourth)
        else:
            counter_clockwise(fourth)
        if t_f:
            if d == 1:
                counter_clockwise(third)
            else:
                clockwise(third)
            if s_t:
                if d == 1:
                    clockwise(second)
                else:
                    counter_clockwise(second)
                if f_s:
                    if d == 1:
                        counter_clockwise(first)
                    else:
                        clockwise(first)
point = 0
point += 1 if first[0] == '1' else 0
point += 2 if second[0] == '1' else 0
point += 4 if third[0] == '1' else 0
point += 8 if fourth[0] == '1' else 0
print(point)
