N, K = map(int, input().split())
order = list(map(int, input().split()))
plugged = []
answer = 0

for i in range(K):
    item = order[i]

    if item not in plugged:

        if len(plugged) < N:
            plugged.append(item)

        else:
            farthest = 0
            farthest_idx = 0
            remains = order[i + 1:]
            for plg_item in plugged:
                if plg_item not in remains:
                    farthest = plg_item
                    break
                else:
                    index = remains.index(plg_item) + i
                    if index > farthest_idx:
                        farthest_idx = index
                        farthest = plg_item

            if farthest:
                plugged.remove(farthest)
            else:
                plugged.pop()
                
            plugged.append(item)

            answer += 1
print(answer)