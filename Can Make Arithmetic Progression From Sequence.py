class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr = sorted(arr)

        for i, n in enumerate(arr):
            try:
                if arr[i] - arr[i+1] == arr[i+1] - arr[i+2]:
                    continue
                else:
                    return False
            except IndexError:
                break
        return True
