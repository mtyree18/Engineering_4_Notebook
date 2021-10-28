def solution(pegs):
    r0 = []
    coefficient = 0
    sign = -1
    distance = []
    distances = (len(pegs))-1
    if (distances + 1) % 2 == 0:
        coefficient = 2/3
    else:
        coefficient = 2
    for i in range (distances):
        distance = distance + [pegs[i + 1] - pegs[i]]
    for x in range ((len(distance))-1):
        #print (x)
        r0 = (distance[x] + (sign * distance[x+1]))
        sign = sign * -1
    r0 = r0 * coefficient
    #if (r0 < 1):
        
    print (r0)
    
solution([4, 30, 50])
