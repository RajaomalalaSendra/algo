class Solution:
    def getSum(self, nums, target):
        results = list()
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    results.append(i)
                    results.append(j)
        return results

    def getSumSecond(self, nums, target):
        dictResults = dict()
        result = list()
        for i in range(0, len(nums)):
            dictResults[nums[i]] = i

        for i in range(0, len(nums)):
            complement = target - nums[i]
            if (complement in dictResults.keys())  and (dictResults[complement] != i):
                result.append(i)
                result.append(dictResults[complement])
                return result

    def getSumThird(self, nums, target):
        dictResults = dict()

        for i in range(0, len(nums)):
            temps = target - nums[i]
            result = list()
            if(temps in dictResults):
                    result.append(dictResults[temps])
                    result.append(i)
                    return result
            dictResults[nums[i]] = i