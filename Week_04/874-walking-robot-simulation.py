def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions={"north":[0,1,"west","east"],
                    "east":[1,0,"north","south"],
                    "south":[0,-1,"east","west"],
                    "west":[-1,0,"south","north"]}
        direction="north"
        x,y=0,0
        ans=0
        obstacles=set(map(tuple,obstacles))
        for com in commands:
            if (com==-1):
                direction=directions[direction][3]
            elif(com==-2):
                direction=directions[direction][2]
            else:
                for step in range(1,com+1):
                    next_step=(x+directions[direction][0],y+directions[direction][1])
                    if(next_step not in obstacles):
                        x,y=next_step[0],next_step[1]
                        ans=max(ans,x**2+y**2)
                    else:
                        break
        return ans