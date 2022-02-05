from cmath import inf


class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        minutes=targetSeconds//60
        seconds=targetSeconds%60
        minStr=str(minutes)
        secStr=str(seconds)
        cost1=0
        
        if minutes==0:
            if len(secStr)==1:
                if secStr==str(startAt):
                    return pushCost
                else: return pushCost+moveCost
            else:
                cost=0
                if secStr[0]!=str(startAt):
                    cost+=moveCost
                if secStr[1]!=secStr[0]:
                    cost+=moveCost
                cost+=pushCost*2
                return cost
        if minStr[0]!=str(startAt):
            cost1+=moveCost
        print(cost1)
        if len(minStr)==2:
            if minStr[0]!=minStr[1]:
                cost1+=moveCost
        print(cost1)
        cost1+=pushCost*len(minStr)
        print(cost1)
        if len(secStr)==1:
            secStr='0'+secStr
        if secStr[0]!=minStr[-1]:
            cost1+=moveCost
        print(cost1)
        if secStr[0]!=secStr[1]:
            cost1+=moveCost
        print(cost1)
        cost1+=pushCost*2
        print(cost1)
        print(minStr, secStr)
        if seconds>=40 and minutes<=99:
            return cost1
        else:
            minutes-=1
            seconds+=60
            minStr=str(minutes)
            secStr=str(seconds)
        cost2=0
        if minutes!=0:
            if minStr[0]!=str(startAt):
                cost2+=moveCost
            print(cost2)
            if len(minStr)==2:
                if minStr[0]!=minStr[1]:
                    cost2+=moveCost
            print(cost2)
            cost2+=pushCost*len(minStr)
            print(cost2)
            if secStr[0]!=minStr[-1]:
                cost2+=moveCost
            print(cost2)
            if secStr[0]!=secStr[1]:
                cost2+=moveCost
            print(cost2)
            cost2+=pushCost*2
            print(minStr, secStr)
            print(cost1, cost2)
        else:
            if secStr[0]!=str(startAt):
                cost2+=moveCost
            print(cost2)
            if secStr[0]!=secStr[1]:
                cost2+=moveCost
            print(cost2)
            cost2+=pushCost*2
        if minutes==99:
            cost1=float('inf')
        return min(cost1, cost2)


        