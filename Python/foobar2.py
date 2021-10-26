def solution(pegs):
    #make a list called pegs and fill the list with the number of pegs
    for x in pegs:
        #sum of the radius of all pegs = lastPeg - firstPeg
        #make sure that lastGear = firstGear/2
        #contstraint = nextPeg - currentPeg
        #my two options are a while loop or an equation. After looking online I found someone who
        #had made an equation and I can see how they got part of it, but now how they simplified
        #Because there can only be 20 pegs, I think if I make something that basically says
        #while firstGear != lastGear * 2 and lengthWorks != True then increase firstGear by 1
        # eventually the fistGear will equal the lastGear * 2 and the lengthWorks will be True
        # and when that happens the loop will store the firstGear and then return its value
        #I just realized that the firstGear will not always be a whole number, so I think
        #I have to do the equation after all.
