def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort(key=lambda x:x[0])
        ans=[intervals[0]]
        for each in intervals[1:]:
            if each[0]>ans[-1][1]:
                ans.append(each)
            else:
                ans[-1][1]=max(ans[-1][1], each[1])
        return ans