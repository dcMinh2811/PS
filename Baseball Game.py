class Solution(object):
    def calPoints(self, operations):
        record = []
        for element in operations:
            try:
                record.append(int(element))
            except ValueError:
                if element == "+":
                    try:
                        record.append(record[-2] + record[-1])
                    except IndexError:
                        pass
                else:
                    if len(record) > 0:
                        if element == "C":
                            del record[-1]
                        elif element == "D":
                            record.append(record[-1]*2)

        score = 0
        for n in record:
            score += n
        return score       
