def solution(pegs):
    r0 = 0
    coefficient = 0
    sign = -1
    distances = (len(pegs))-1
    if (distances) % 2 == 0:
        coefficient = 2/3
    else:
        coefficient = 2
    for i in range (distances):
        print (i)
        distance = pegs[i + 1] - pegs[i]
        r0 = r0 + (coefficient * (sign * distance))
        sign = -1 * sign
        
solution([4, 30, 50])
