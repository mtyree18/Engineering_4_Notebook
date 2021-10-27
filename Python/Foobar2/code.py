def solution(pegs):
    r0 = 0
    coefficient = 0
    sign = -1
    distance = []
    distances = (len(pegs))-1
    if (distances) % 2 == 0:
        coefficient = 2/3
    else:
        coefficient = 2
    for i in range (distances):
        distance = distance + [pegs[i + 1] - pegs[i]]
    print (distance)
    for x in range (distances):
        #r1 = 2 (d1 - d2)
        r0 = (distance[i] - distance[i+1])
    
solution([4, 30, 50])
