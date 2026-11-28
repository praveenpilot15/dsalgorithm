class Solution(object):
    def findRightInterval(self, intervals):
        arr = []  # to store the start value and original index
        for i in range(len(intervals)):
            arr.append((intervals[i][0], i))
        arr.sort(key=lambda x: x[0])  # sorting the start values to perform binary search
        result = []  # to store output index
        for interval in intervals:
            target = interval[1]
            lb = 0
            ub = len(arr) - 1
            ans = -1
            while lb <= ub:
                mid = (lb + ub) // 2
                if arr[mid][0] >= target:
                    # right interval condition
                    ans = arr[mid][1]  # stored original index
                    ub = mid - 1  # to search in the left side for an start index larger then target, there can be a value greater than target 
                else:
                    lb = mid + 1  # start value is small so check on right side
            result.append(ans)
        return result
