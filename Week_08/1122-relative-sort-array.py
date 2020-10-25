def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if not arr1: return []
        if not arr2: return arr1
        ans=[]
        counter=collections.Counter(arr1)
        visited=set()
        for num in arr2:
            visited.add(num)
            n=counter[num]
            ans+=[num]*n
        
        a=list(counter.items())
        a.sort(key=lambda x: x[0])
        for key, value in a:
            if key not in visited:
                ans+=[key]*value

        return ans