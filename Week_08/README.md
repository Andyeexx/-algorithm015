学习笔记

#位运算总结
	位运算操作：
		1.<< 左移	0011 => 0110     乘以二
		2.>> 右移	0110 => 0011	 除以二

		3.|  按位或  0011
					------- => 1011
					1011

		4.&  按位与	0011
					------- => 0011
					1011

		5.~  按位取反 0011 => 1100
		6.^  按位异或 0011			 相同为0，不同为1， 也可理解为不进位加法
					------- => 1000
					1011
		7.-  补码	正整数的补码是其二进制表示，与原码相同
					求负整数的补码，将其原码除符号位外的所有位取反（0变1，1变0，符号位为1不变）后加1

		异或相关的操作：
		x^0=x
		x^1s=~x //注意 1s = ~0
		x^(~x)=1s
		x^x=0
		c=a^b => a^c=b,b^c=a //交换两个数 
		a^b^c=a^(b^c)=(a^b)^c //associative

		指定位置的位运算：
		1. 将x最右边的n位清零:x&(~0<<n)
		2. 获取x的第n位值(0或者1):(x>>n)&1
		3. 获取x的第n位的幂值:x&(1<<n)
		4. 仅将第n位置为1:x|(1<<n)
		5. 仅将第n位置为0:x&(~(1<<n))
		6. 将x最高位至第n位(含)清零:x&((1<<n)-1)

		实战位运算要点
			判断奇偶：
				x%2==1 —>(x&1)==1 
				x%2==0 —>(x&1)==0
			乘2：
				x>>1—>x/2
			X=X&(X-1)清零最低位的1
			X&-X=>得到最低位的1
			X&~X=>0

# 布隆过滤器
	from bitarray import bitarray 
	import mmh3 
	class BloomFilter: 
		def __init__(self, size, hash_num): 
			self.size = size 
			self.hash_num = hash_num 
			self.bit_array = bitarray(size) 
			self.bit_array.setall(0) 
		def add(self, s): 
			for seed in range(self.hash_num): 
				result = mmh3.hash(s, seed) % self.size 
				self.bit_array[result] = 1 
		def lookup(self, s): 
			for seed in range(self.hash_num): 
				result = mmh3.hash(s, seed) % self.size 
				if self.bit_array[result] == 0: 
					return "Nope" 
			return "Probably" 

# LRU Cache
	class LRUCache(object):
		def __init__(self, capacity):
			self.dic = collections.OrderedDict() 
			self.remain = capacity
		
		def get(self, key):
			if key not in self.dic:
				return -1
			v = self.dic.pop(key)
			self.dic[key] = v # key as the newest one 
			return v

		def put(self, key, 	): 
			if key in self.dic:
				self.dic.pop(key) 
			else:
				if self.remain > 0: 
					self.remain -= 1
				else: # self.dic is full 
					self.dic.popitem(last=False) #默认last=true删除最后一个键值（最新加入的），当last=false，删除第一个加入的
			self.dic[key] = value

#快速排序quickSort
	def quick_sort(begin, end, nums):
	    if begin >= end:
	        return
	    pivot_index = partition(begin, end, nums)
	    quick_sort(begin, pivot_index-1, nums)
	    quick_sort(pivot_index+1, end, nums)
    
	def partition(begin, end, nums):
	    pivot = nums[begin]
	    mark = begin
	    for i in range(begin+1, end+1):
	        if nums[i] < pivot:
	            mark +=1
	            nums[mark], nums[i] = nums[i], nums[mark]
	    nums[begin], nums[mark] = nums[mark], nums[begin]
	    return mark

#归并排序 mergesort
	def mergesort(nums, left, right):
	    if right <= left:
	        return
	    mid = (left+right) >> 1
	    mergesort(nums, left, mid)
	    mergesort(nums, mid+1, right)
	    merge(nums, left, mid, right)

	def merge(nums, left, mid, right):
	    temp = []
	    i = left
	    j = mid+1
	    while i <= mid and j <= right:
	        if nums[i] <= nums[j]:
	            temp.append(nums[i])
	            i +=1
	        else:
	            temp.append(nums[j])
	            j +=1
	    while i<=mid:
	        temp.append(nums[i])
	        i +=1
	    while j<=right:
	        temp.append(nums[j])
	        j +=1
	    nums[left:right+1] = temp

#堆排序
	def heapify(parent_index, length, nums):
	    temp = nums[parent_index]
	    child_index = 2*parent_index+1
	    while child_index < length:
	        if child_index+1 < length and nums[child_index+1] > nums[child_index]:
	            child_index = child_index+1
	        if temp > nums[child_index]:
	            break
	        nums[parent_index] = nums[child_index]
	        parent_index = child_index
	        child_index = 2*parent_index + 1
	    nums[parent_index] = temp

	def heapsort(nums):
	    for i in range((len(nums)-2)//2, -1, -1):
	        heapify(i, len(nums), nums)
	    for j in range(len(nums)-1, 0, -1):
	        nums[j], nums[0] = nums[0], nums[j]
	        heapify(0, j, nums)


# 191 位1的个数
	1.使用位运算
		每次都清零最低位的1，直到不行位置 使用 n& (n-1)

#190 颠倒二进制位
	1.使用位运算
		从后往前，每次都判断当前位是否是1，是的话加入输出结果中，并且右移n
		def reverseBits(self, n: int) -> int:
        ans=0
        for _ in range(32):
            ans = ans<<1 | (n&1)
            n>>=1
        return ans

#338 比特位技术
	1.写一个循环遍历每个数，然后用 n&(n-1)来算每个数需要多少1
	2.动态规划，写一个循环遍历每个数，dp[i]=dp[i&(i-1)]+1

#132 分割回文串2
	1.使用一遍dp判断每段i-j时候是回文，再结合bfs，输出最短的切割方式
	2.一遍dp，再用数组min_s记录到字符串到i位置需要分割次数
		if j == 0:
	        min_s[i] = 0
	    else:
	        min_s[i] = min(min_s[i], min_s[j - 1] + 1)

#1122 数组的相对排序
	1.使用计数排序，所有东西先存到counter里，按要求拿出

