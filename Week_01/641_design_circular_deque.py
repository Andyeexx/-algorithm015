class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.max_len=k
        self.cur_len=0
        self.queue=[0 for i in range(k)]
        self.front, self.end=0,0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if(self.cur_len==self.max_len):
            return False
        self.front= (self.front-1)%self.max_len
        self.queue[self.front]=value
        self.cur_len+=1
        return True
        
        
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if(self.cur_len==self.max_len):
            return False
        self.queue[self.end]=value
        self.end= (self.end+1)%self.max_len
        self.cur_len+=1
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.cur_len:
            return False
        self.front=(self.front+1)%self.max_len
        self.cur_len-=1
        return True


    
    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.cur_len:
            return False
        self.end=(self.end-1)%self.max_len
        self.cur_len-=1
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.cur_len:
            return -1
        return self.queue[self.front]
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.cur_len:
            return -1
        return self.queue[self.end-1]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not self.cur_len
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.cur_len==self.max_len)
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()