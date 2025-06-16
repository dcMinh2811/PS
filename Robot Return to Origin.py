class Solution(object):
    def judgeCircle(self, moves):
        x = 0
        y = 0
        for move in moves:
            if move == "R":
                x += 1
            elif move == "L":
                x -= 1
            elif move == "U":
                y += 1
            elif move == "D":
                y -= 1
        return True if x == y == 0 else False
