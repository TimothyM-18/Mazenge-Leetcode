

def balls_remaining(strength, direction):

    stack  = []
    result = []
    for i in range(len(strength)):
        if stack:
            while stack and stack[-1][0] < strength[i] and direction[i] == -1:
                stack.pop()
            if not stack:
                result.append(i)
            
            if stack and stack[-1][0] == strength[i] and direction[i] == -1:
                stack.pop()
                continue
            
            if direction[i] == 1:
                stack.append([strength[i], direction[i], i])  
        else:
            if direction[i] == 1:
                stack.append([strength[i], direction[i], i])
            else:
                result.append(i)
    
    while stack:
        ball = stack.pop()
        result.append(ball[2])
        
    
    return result

print(balls_remaining([80, 70, 70, 100], [1, -1, -1, -1]))




