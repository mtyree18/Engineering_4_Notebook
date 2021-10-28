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
    for x in range (len(distance)):
        print (x)
        #r0 = (distance[i] + (sign * distance[i+1]))
        #print (r0)
        sign = sign * -1
    
solution([4, 30, 50])
