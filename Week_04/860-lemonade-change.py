def lemonadeChange(self, bills: List[int]) -> bool:
        if not(bills or bills[0]!=5): return False
        change=collections.defaultdict(int)
        for num in bills:
            if(num==5):
                change["5"]+=1
            if(num==10):
                if(change["5"]==0):
                    return False
                else:
                    change["5"]-=1
                    change["10"]+=1
            if(num==20):
                if(change["10"]!=0 and change["5"]!=0):
                    change["10"]-=1
                    change["5"]-=1
                    change["20"]+=1
                elif(change["5"]>=3):
                    change["5"]-=3
                    change["20"]+=1
                else:
                    return False
        return True