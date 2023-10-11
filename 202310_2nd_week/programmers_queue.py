import heapq


def solution(operations):
    heap = []
    for operation in operations:
        num = int(operation[2:-1] + operation[-1])
        # 숫자 삽입
        if operation[0] == 'I':
            heapq.heappush(heap, num)

        else:
            # 최소값 삭제
            if heap and num == -1:
                heapq.heappop(heap)

            # 최대값 삭제
            elif heap and num == 1:
                l = len(heap)
                for i in range(l):
                    heap[i] = -heap[i]
                heapq.heapify(heap)
                heapq.heappop(heap)
                if heap:
                    for j in range(l - 1):
                        heap[j] = -heap[j]
                    heapq.heapify(heap)
    if not heap:
        answer = [0, 0]
    else:
        heap.sort()
        answer = [heap[-1], heap[0]]
    return answer