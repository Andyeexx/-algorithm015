def leastInterval(self, tasks: List[str], n: int) -> int:
        mp=collections.Counter(tasks)
        all_task=list(mp.values())
        all_task.sort()
        return max(len(tasks), (all_task[-1]-1)*(n+1)+all_task.count(all_task[-1]))