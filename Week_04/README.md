学习笔记

经验总结：
	1.树的遍历，用stack模拟
		前序遍历：遇到root就加入结果，再依次把child从右往左加入stack
		后序遍历：基本上是前序遍历的翻版
			我们需要的结果是“左右根”，那么我们利用前序构造“根右左”，最后再颠倒结果就好了
			遇到root就加入结果，再依次把child从左往右加入stack，最后输出时颠倒结果
		中序遍历：比较我们需要在最开始一直遍历到最左的节点，然后开始循环，代码如下，需要多练习
			def inorderTraversal(self, root: TreeNode) -> List[int]:
	        if not root: return []
	        stack=[root]
	        ans=[]
	        while(stack or root):
	            stack.append(root)
	            while(root.left):
	                stack.append(root.left)
	            root=stack.pop()
	            ans.append(root.val)
	            if(root.right):
	                stack.append(root.right)
	        return ans
	2.recursion只是调用顺序的不同

	3.string.ascii_lowercase 返回小写a-z

	4.local variable 'xxx' referenced before assignment 报错
	原因，全局变量不能直接在function里改变，需要声明global
	 solution: 1. global 
	 		   2. class中可以直接定义self.variable_name，就不用担心这个问题了

	5.二叉搜索总结：
	while left<=right:循环内部查找元素
	mid=left+(right-left)/2, mid==target就返回，否则left=mid+1, 或right=mid-1
	---------------------------------------------------------------------------------
	while left<right:循环内部排除元素
	几个搭配：mid=left + (right-left)/2,      此方法为取目标值的下界，比如有3相同的个目标值，则返回最左边的那个
			if(num[mid]<target):
				left=mid+1, 				保留更多的左边
			else:
				right=mid
		--------------------------------------------
			mid=left + (right-left+1)/2, 	此方法为取目标值的上界，比如有3相同的个目标值，则返回最右边的那个
			if(num[mid]>target):
				right=mid-1					保留更多的右边
			else:
				left=mid

#4 寻找两个正序数组的中位数
	1.我自己的算法，算好合并后的中位数位置，利用双指针来填入，填满中位数的位置的长度就停止。但时间复杂度为O((m+n)/2)
	2.此题若想达到O(log（m+n)), 需要二分查找找到第K大的数。即每次只看list中对应的k/2位置,删去小的那k/2部分，所以我们做后之用计算log(k)次，k=m+n/2
	此题有个计算中位数的小技巧，代码如下
		def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k1=(len(nums1)+len(nums2)+1)//2
        k2=(len(nums1)+len(nums2)+2)//2
        def helper(n1,n2,k):
            if(len(n1)>len(n2)):    #确保n1长度最小
                n1,n2=n2,n1
            if(len(n1)==0):         #当一个list删空了
                return n2[k-1]
            if(k==1):               #计算结束，返回当前最小的那个数
                return min(n1[0],n2[0])
            mid=min(k//2,len(n1))      #递归部分，删除小的那部分，每次删k/2
            if(n1[mid-1]<n2[mid-1]):
                return helper(n1[mid:],n2,k-mid)
            else:
                return helper(n1,n2[mid:],k-mid)
        return ( helper(nums1,nums2,k1)+ helper(nums1,nums2,k2) )/2

#5 最长回文子串
	1.我用的双向扩展法，分奇数和偶数的中间值来向两边扩展
	2.此题应当应用动态规划，创建一个2维的空间，里面存储i位置到j位置的string是否为回文，即dp[i][j]=dp[i+1][j-1] and s[i]==s[j]
	def longestPalindrome(self, s: str) -> str:
        dp=[[False]*len(s) for _ in range(len(s))]
        ans=""
        for l in range(len(s)):
            for i in range(len(s)):
                j=l+i
                if(j>=len(s)):
                    break
                if(l==0):
                    dp[i][j]=True
                elif(l==1):
                    dp[i][j]= (s[i]==s[j])
                else:
                    dp[i][j]= (dp[i+1][j-1] and s[i]==s[j])
                if(dp[i][j] and l+1>len(ans)):
                    ans=s[i:j+1]
        return ans


#433 最小基因变化
	1.此题最好的方法就是BFS
	把可更换的选项放在一起存好，然后利用queue模拟BFS，BFS过程中假如得到结果，那就是最少步骤。

#200 岛屿数量
	1.使用DFS，遍历每个位置，每次遇到1，就开始进行dfs，把与其相连的其他1都变为0
	2.BFS与DFS本质一样，同样是遇到1后，把周围其他1存入queue，然后把周围变成0

#127 单词接龙
	1.此题和433相似，需要利用BFS,但是区别是可替换的字母没有规定，只能自己建立替换表.
	总体分为四个模块：
	for 找head
    while queue：
        for 找邻居
            if 没有重复：处理，标记，入队

#126 单词接龙2
	1.和单词接龙1相似，需要记录最短的路径，确保弹出时再把单词加入visited。
	收藏一个简洁代码：
	def findLadders(self, beginWord, endWord, wordList):  
        wordList = set(wordList)
        dic = collections.defaultdict(list)
        n = len(beginWord)
        for w in wordList:
            for i in range(n):
                dic[w[:i] + '*' + w[i+1:]].append(w)
        q, s = collections.deque([(beginWord, [beginWord])]), collections.deque()
        seen, res = set(), []
        while q:
            while q:
                w, path = q.popleft()
                if w == endWord: res.append(path)
                seen.add(w)
                for i in range(n):
                    for v in dic[w[:i] + '*' + w[i+1:]]:
                        if v not in seen:
                            s.append((v, path + [v]))
            if res: return res
            q, s = s, q
        return []

#529 扫雷游戏
	1. 典型dfs应用，检测周围一圈的node，假如没出界，并且没有炸弹，那就将周围的node进行dfs

#455 分发饼干
	1.使用贪心算法，局部最优解即整体最优解

#122 买卖股票的最佳时机2
	1.使用贪心算法，只需要在意今天与明天的价格，假如要涨就买，假如会跌就卖

#55 跳跃游戏
	1.使用贪心算法
	如果能到达某个位置，那一定能到达它前面的所有位置。
	初始化最远位置为 0，然后遍历数组，如果当前位置能到达，并且当前位置+跳数>最远位置，就更新最远位置。最后比较最远位置和数组长度。

# 跳跃游戏2
	1.使用贪心算法，此题需要设置一个边界，边界里的所有点，都属于同一个步数，当遍历指针遇上边界时，把边界重新设定为当前能到达的最远距离

#860 柠檬水找零
	1.使用贪心算法，收到5元直接存入，遇到10元找回5元，遇到20元优先找回10+5，之后才是5+5+5，假如无法找回return false

#874 模拟行走机器人
	1.使用贪心算法，完全模拟他所描述的要求，只不过代码实施起来需要一些技巧，有两个很好的操作：
		a.把方向相关的操作存到一个dict
		directions={"north":[0,1,"west","east"],
                    "east":[1,0,"north","south"],
                    "south":[0,-1,"east","west"],
                    "west":[-1,0,"south","north"]}
        b.因为需要反复检查，把obstacle 转换为 set，将in这个function的时间复杂度从list的O(n)降为O(1)
        	obstacles=set(map(tuple,obstacles))，tuple在此处是function，意味把obstacles存储为tuple放入map，最后将这个map转换为set

#6 Z字形变换
	1.使用行排序，外加一个指针，当遇到0或最后一行是改变指针方向，下一行是当前行加上指针

#322 零钱兑换
	1.使用动态规划，此题是经典的完全背包问题
	完全背包：给定不同面额的硬币 coins 和总金额 m。每个硬币可以选择无数次。计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
		def coinChange(self, coins, m):
	        f = [float('inf')]*(m+1)
	        f[0] = 0
	        for c in coins:  # 枚举硬币种数
	            for j in range(c, m+1):  # 从小到大枚举金额，确保j-c >= 0.
	                    f[j] = min(f[j], f[j - c] + 1)
	        return f[m] if f[m] != float('inf') else -1  # 如果为inf说明状态不可达，返回-1即可。

   	01背包：给定不同面额的硬币 coins 和总金额 m。每个硬币最多选择一次。计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
	   	def func_2(coins, m):
		    f = [float('inf')] * (m + 1)
		    f[0] = 0
		    for c in coins:  # 枚举硬币总数
		        for j in range(m, c-1, -1):  # 从大到小枚举金额，确保j-c >= 0.
		            f[j] = min(f[j], f[j - c] + 1)
		    return f[m] if f[m] != float('inf') else -1  # 如果为inf说明状态不可达，返回-1即可。

	多重背包：给定不同面额的硬币 coins 和总金额 m。每个硬币选择的次数有限制为s。计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
		def func_3(coins, m, s):
		    f = [float('inf')] * (m + 1)
		    f[0] = 0
		    for i in range(len(coins)):
		        for j in range(m, coins[i]-1, -1):
		            for k in range(1, s[i]+1):  # 枚举每个硬币的个数 [1, s[i]]
		                if j >= k*coins[i]:  # 确保不超过金额 j
		                    f[j] = min(f[j], f[j - k*coins[i]] + k)
		    print(f)
		    return -1 if f[m] > m else f[m]

#404 左叶子之和
	1.使用recursion就行，判断左子树是否为左叶子，即没有子节点的节点

#面试题 16.05 阶乘尾数
	1.此题计算一个数的阶乘有多少个0结尾，其实n!中的零全部是5和2的倍数贡献的，由于因子为2的个数大于5的，所以，只需计算其中有多少个5的倍数即可。

#69 x的平方根
	1.经典二分搜索，设好左右边界然后去靠近，有一点需注意，取mid值时为了防止整数溢出：mid=left+(right-left)//2,其他比较麻烦的地方			

	2.牛顿迭代法：在迭代过程中，以直线代替曲线，用一阶泰勒展式（即在当前点的切线）代替原曲线，求直线与 x 轴的交点，重复这个过程直到收敛。
	对于平方根公式来说，这个交点的公式为(x0+a/x0)/2，代码如下

	def mySqrt(self, x):
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        # 起始的时候在 1 ，这可以比较随意设置
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)

#367 有效的完全平方数
	1.二叉搜索，我将num 除以2作为right以缩短运行时间，因为（2之后的完全平方数的一半）**2>数本身
	2.牛顿迭代法：
	def isPerfectSquare(self, num: int) -> bool:
        if(num<2):return True
        x=num//2
        while(x*x>num):
            x=(x+num/x)//2
        return (x*x==num)

#33 搜索旋转排序数组
	1. 可以将数组转换为两个升序数组，再进行二叉搜索
	2.依旧可以直接进行二叉搜索，先判断哪边单调递增，接着再细分target在哪里

#74 搜索二维矩阵
	1.我的方法：使用两次二次查找，第一次先找到具体在哪一行，接着再单独一行里二次查找，时间复杂度O(log(m)+log(n))
	2.因为整体依旧是升序，所以进行一次二位查找即可，
		只不过left=0, right=m*n-1,mid的表达改为 mid_num=matrix[mid//n][mid%n]

#153 寻找旋转排序数组中的最小值
	1.使用二叉搜索，当中间值大于左边界时，证明左边是单调递增，那么旋转点应该在右侧，设置左边界为mid+1，右边同理

	