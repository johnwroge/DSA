# Meeting rooms/min halls
def minHalls(start, end) :
    # tasks_list = [[s,e] for s,e in zip(start, end)]
    prefix_sum = [0] * MAX
    n = len(start)

    for i in range(n) :
        prefix_sum[start[i]] += 1
        prefix_sum[end[i] + 1] -= 1
         
    ans = prefix_sum[0]

    for i in range(1, MAX) :
        prefix_sum[i] += prefix_sum[i - 1]
        ans = max(ans, prefix_sum[i])
    
    return ans; 

def minHalls2(lectures: List[List[int]], n: int) -> int:
    Time = []
    for i in range(n):
        Time.append((lectures[i][0], 1))
        Time.append((lectures[i][1], -1))
    Time.sort(key=lambda x: x[0])
    answer = 0
    sum = 0
    for i in range(len(Time)):
        sum += Time[i][1]
        answer = max(answer, sum)
    return answer


