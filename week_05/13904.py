N = int(input())
assignment_list = [list(map(int, input().split())) for _ in range(N)]
assignment_list.sort()

assignment_dict = dict()
for d, w in assignment_list:
    if assignment_dict.get(d):
        assignment_dict[d].append(w)
    else:
        assignment_dict[d] = [w]

formal_day = assignment_list[0][0]
score_list = list()

for day in assignment_dict:
    if score_list:
        can_do = day - len(score_list)
        score_list.extend(assignment_dict[day][-1:-1 - can_do:-1])
        score_list.sort(reverse=True)

        for day_score in assignment_dict[day][-1 - can_do::-1]:
            if day_score >= min(score_list):
                score_list.pop()
                score_list.append(day_score)
                score_list.sort(reverse=True)
            else:
                break
    else:
        score_list.extend(assignment_dict[day][-1:-1 - day:-1])

print(sum(score_list))
