N, M = map(int, input().split())
knows = list(map(int, input().split()))
persons = [[False] for _ in range(N + 1)]
parties = []
for i in range(M):
    party = list(map(int, input().split()))
    parties.append(party[1:])
    for person in party[1:]:
        persons[person].append(i)

truth = []
if len(knows) == 1:
    print(M)
else:
    q = knows[1:]
    while q:
        p = q.pop(0)
        persons[p][0] = True
        for pt in persons[p][1:]:
            if pt not in truth:
                truth.append(pt)
                for ps in parties[pt]:
                    if not persons[ps][0]:
                        q.append(ps)
    print(M - len(truth))