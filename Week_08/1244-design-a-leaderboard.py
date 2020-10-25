def __init__(self):
        self.table={}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.table:
            self.table[playerId]+=score
        else:
            self.table[playerId] = score



    def top(self, K: int) -> int:

        tmp= sorted(list(self.table.values()), reverse=True)
        return sum(tmp[:K])

    def reset(self, playerId: int) -> None:
        self.table[playerId]=0