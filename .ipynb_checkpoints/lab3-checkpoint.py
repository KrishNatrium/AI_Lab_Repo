from collections import deque
def water_jug_bfs(A,B,c) :
    queue = deque([(0,0)])
    visited = set((0,0))
    path = {}

    actions = [
        lambda x,y : (A,y), # to fill A
        lambda x,y : (x,B), # to fill B
        lambda x,y : (0,y), # to empty A
        lambda x,y : (x,0), # to empty B
        lambda x,y : (x - min(x,B-y), y + min(x,B-y)), # pour from A to B, can only fill until full
        lambda x,y : (x + min(y,A-x), y - min(y,A-x)), # pour from B to A, same reason
        lambda x,y : (x // 2, y), # to half the jug
        lambda x,y : (x, y // 2), # t0 half the jug
    ]

    while queue :
        current = queue.popleft()

        if current[0] == c or current[1] == c :
            return construct(current,path)

        for action in actions :
            next = action(*current)

            if next not in visited :
                visited.add(next)
                queue.append(next)
                path[next] = current

    return None


def construct(goal, path) :
    result = []
    current = goal
    while current :
        result.append(current)
        current = path.get(current)

    result.reverse()
    return result



A = int(input("Enter value for Jug A: "))
B = int(input("Enter valur for Jug B: "))
c = int(input("Enter value for goal state Jug :"))

result = water_jug_bfs(A,B,c)
if result :
    print("The path is :")
    for i in range(len(result) - 1):
        print(f"{result[i]} -> {result[i+1]}")
else :
    print("No Solutions")