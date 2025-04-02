def solution(bridge_length, weight, truck_weights):
    timer = 0
    buffer = [0 for _ in range(bridge_length)]
    
    while len(truck_weights) > 0 or sum(buffer) > 0:
        buffer.pop(0)
        buffer.append(0)
        
        if len(truck_weights) > 0:
            if sum(buffer) + truck_weights[0] <= weight:
                buffer[-1] = truck_weights.pop(0)
        
        timer += 1
    
    return timer