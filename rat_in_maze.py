

def isSafe(arr,x,y):
    if 0 <=x < len(arr) and 0 <=y <len(arr) and arr[x][y] == 1:
        return True
    return False
    
def solution(arr):
    N = len(arr)
    solutionarr = [[0 for _ in range(N)] for _ in range(N)]
    if solve_maze(arr,0,0,solutionarr) == False:
        print("No solution available")
        return False
    print_solution(solutionarr)
    return True

def solve_maze(arr,x,y,solutionarr):

    if x==len(arr)-1 and y==len(arr)-1:
        solutionarr[x][y] = 1
        return True
    
    if isSafe(arr,x,y):

        solutionarr[x][y] = 1

        if solve_maze(arr,x+1,y,solutionarr):
            return True
        
        if solve_maze(arr,x,y+1,solutionarr):
            return True
        
        solutionarr[x][y] = 0
        return False
    
    return False

def print_solution(solution):
     for row in solution:
        print(" ".join(str(cell) for cell in row))

arr = [
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0]
]

# Solve the maze
solution(arr)

