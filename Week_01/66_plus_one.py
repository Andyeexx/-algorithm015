class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pos=-1
        flag= True
        add_flag=False
        while flag and (not add_flag):
            if(digits[pos]+1)==10:
                digits[pos]=0
                pos-=1
                if(abs(pos)>len(digits)):
                    add_flag=True
            else:
                digits[pos]+=1
                flag=False
        if add_flag:
            return [1]+digits
        else:
            return digits