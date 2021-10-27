def solution(pegs):
    r0 = 0
    coefficient = 0
    distances = (len(pegs))-1
    if (distances) % 2 == 0:
        coefficient = 2/3
    else:
        coefficient = 2
    for i in pegs:
        print (i)
        r0 = r0 + (coefficient( pegs[i + 1] - pegs[i] ))
    
solution([4, 30, 50])
