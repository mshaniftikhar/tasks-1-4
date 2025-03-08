# DFS for Water Jug Problem
def waterJugProblemDFS(capacity1, capacity2, goal):
    stack = [(0, 0)] 
    visited = set()   
    visited.add((0, 0)) 
    actions = [] 
    rules = [
        (capacity1, 0),  
        (0, capacity2),  
        (0, 0),          
        (0, 0),         
    ]

    while stack:
        jug1, jug2 = stack.pop()
        actions.append((jug1, jug2))
        if jug1 == goal or jug2 == goal:
            print("Solution Found:")
            for action in actions:
                print(action)
            return True
        new_states = [
            (capacity1, jug2),  
            (jug1, capacity2),  
            (0, jug2),          
            (jug1, 0),         
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)), 
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1)),  
        ]
        for state in new_states:
            if state not in visited:
                visited.add(state)
                stack.append(state)
    print("No Solution found")
    return False
jug1Capacity = 4
jug2Capacity = 3
target = 2
waterJugProblemDFS(jug1Capacity, jug2Capacity, target)
