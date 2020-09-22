学习笔记


python queue源码分析：
	put(self, item, block=True, timeout=None):  #填入
		put由helper function完成，原理是使用queue.append(item)， 所以时间复杂度为O(1)
	def get(self, block=True, timeout=None):    #取出
		get由也helper function完成，原理是使用queue.popleft()，所以时间复杂度是O(1)

python priority queue源码分析：
	python的优先级队列是由heapq来写的，往一个长度为n的优先级队列中插入一个元素时间复杂度是O(logn)。那么把n个元素插入一个空的优先级队列中时间复杂度就为O(nlogn)。如果把n个元素插入一个空的优先级队列中，但是优先级队列的最大长度为k，那么时间复杂度就为O(nlogk)。
	push为heappush时间复杂度为O(logn)， pop为heappop时间复杂度为O(logn)


#1（简单） 两数之和
	1.暴力解法，挨个试，不可取
	2.hashmap存下来，key为数字本身，value为index，直接用hashmap去找是否存在target与num之差，时间复杂度为O(n)

#21（简单） 合并两个有序链表
	1.自己写出来的解法：利用一个额外指针，遍历两个head指针，时间复杂度为O(n)，空间复杂度为O(1)，
	2.recursion: 
    	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
	        if not l1: return l2  # 终止条件，直到两个链表都空
	        if not l2: return l1
	        if l1.val <= l2.val:  # 递归调用
	            l1.next = self.mergeTwoLists(l1.next,l2)
	            return l1
	        else:
	            l2.next = self.mergeTwoLists(l1,l2.next)
	            return l2

#42（困难）接雨水
	1.自己写出来的算法：暴力解法，时间复杂度O(n^3)
	2.大佬算法：动态规划，两边for loop先找到属于每个位置的max_left与max_right, 最后直接计算
	3.大佬算法：双指针，左右各一个。因为每个位置的水量由两边最小的max height决定，所以当max_left<max_right时，当前水位为max_height-height[i]。max_right大时同理

#66（简单） 加一
	1.自己写出来的算法：使用双flag，判断进位和结束
	2.从后往前依次判断末尾是否为9 如果是 则去除，见一个空的array往里面加0
    def plusOne(self, digits: List[int]) -> List[int]:
        newlst = []
        while digits and digits[-1] == 9:
            digits.pop()
            newlst.append(0)
        if not digits:
            return [1] + newlst
        else:
            digits[-1] += 1
            return digits + newlst

#88（简单） 合并两个有序数组
	1.自己写出来的算法：利用额外数组外加双指针，存储数组1与2，然后比大小放入 时间复杂度 : O(n + m)O(n+m) 空间复杂度 : O(m)O(m)
	2.双指针 / 从后往前：利用三个指针，其中两个p1,p2分别指向数组1与2的最后一位有效数字，第三个指针p3（指向将要填入的位置）从数组1最后一位开始遍历.p1与p2比大小，大的放入p，然后p向前移一位。p1,p2进行相对应移动

#189（简单） 旋转数组：
	1.自己写出来的解法：利用两个额外数组，空间复杂度为O(n)
	
	2.环状替换:思路很新颖，但整个过程还需要多温习，要不然肯定会忘记
	also, python中没有do while，取而代之的是 
	while true：
		if(...):
			break
	3.三次反转：整体反转，前半段反转，后半段反转
		更好理解，必须掌握

#283（简单） 移动0
	1.自己写出来的解法：双指针，本质是快慢指针，但用了while loop，很繁琐
	2.快慢指针，for loop 即可，一个pos，一个cur,遇到非0，双方交换，slow+1
	3.python写法，遇到非零直接调换nums[i],nums[pos] = nums[pos],nums[i]，pos+1

#641（中等） 设计循环双端队列 
	1.利用双指针，记录前与后
	要点：计算前指针(加入)：(front-1)%max，先变位置再加入
		 计算后指针(加入)：(end+1 ) %max 先填入再变位置
		 计算前指针(删除)：(front+1)%max
		 计算后指针(删除)：(end-1 ) %max

