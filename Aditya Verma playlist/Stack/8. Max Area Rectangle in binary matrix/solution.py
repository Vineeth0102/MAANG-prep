
def maxArea(mat):
    
    def maxAreaHist(arr: list[int]) -> int:
        n = len(arr)
        stack = []
        right_small_index = [n] * n
        
        for i in range(n -1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right_small_index[i] = stack[-1]
            stack.append(i)
            
        stack = []
        left_small_index = [-1] * n
        area = 0
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left_small_index[i] = stack[-1]
            stack.append(i)  
            area = max(area, arr[i] * (right_small_index[i] - left_small_index[i] -1))
        return area
        
    
    num_rows = len(mat)
    num_col = len(mat[0])
    arr = [0] * num_col
    res = 0
    for i in range(num_rows):
        for j in range(num_col):
            if mat[i][j] == 1:
                arr[j] += 1
            else:
                arr[j] = 0
            
        res = max(maxAreaHist(arr), res)
    
    return res

rows = int(intput("Number of rows: "))
mat = []
for i in range(rows):
    new_row = list(map(int, input().split()))
    mat.append(new_row)
print(maxArea(mat))
