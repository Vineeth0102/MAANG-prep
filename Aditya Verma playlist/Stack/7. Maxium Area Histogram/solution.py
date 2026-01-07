# TC : O(3N) => becuase of 3 for loops 
def largestRectangleArea(heights: list[int]) -> int:
    stack = []
    n = len(heights)
    left_smallest_index = [-1] * n

    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            left_smallest_index[i] = stack[-1]
        stack.append(i) 

    stack = []
    right_smallest_index = [n] * n
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            right_smallest_index[i] = stack[-1]
        stack.append(i) 

    max_area = 0
    for i in range(n):
        size = heights[i] * (right_smallest_index[i] - left_smallest_index[i] - 1)
        max_area = max(max_area, size)

    return max_area

# TC : O(2N) => becuase of 2 for loops 

def largestRectangleAreaOpt(heights: List[int]) -> int:
    
    n = len(heights)
    stack = []
    right_smallest_index = [n] * n
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            right_smallest_index[i] = stack[-1]
        stack.append(i) 

    stack = []
    max_area = 0
    left_smallest_index = [-1] * n
    for i in range(n):

        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            left_smallest_index[i] = stack[-1]
        stack.append(i)

        size = heights[i] * (right_smallest_index[i] - left_smallest_index[i] - 1)
        max_area = max(max_area, size)

    return max_area


    
arr = list(map(int, input().split()))
print(largestRectangleAreaOpt(arr))