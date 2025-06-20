#I'm sorry I couldn't think of the idea of how to make it faster
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        count = 0
        if k < len(tickets):
            while tickets[k] > 0:
                for i in range(len(tickets)):
                    if tickets[i] != 0:
                        tickets[i] -= 1
                        count += 1
                    if tickets[k] == 0:
                        return count
