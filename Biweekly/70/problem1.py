class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost=sorted(cost)[::-1]
        if len(cost) == 1:
            return cost[0]
        if len(cost) in [2,3]:
            return cost[0]+cost[1]
        if len(cost)%3==0:
            return sum([cost[3*x] for x in range((len(cost)//3))]+[cost[3*x+1] for x in range((len(cost)//3))])
        if len(cost)%3==2:
            return sum([cost[3*x] for x in range((len(cost)//3)+1)]+[cost[3*x+1] for x in range((len(cost)//3)+1)])
        if len(cost)%3==1:
            return sum([cost[3*x] for x in range((len(cost)//3)+1)]+[cost[3*x+1] for x in range((len(cost)//3))])