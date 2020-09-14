学习笔记
Tips:
python 多重赋值：右边的值先确定，然后再开始向左赋值
python := 海象运算符用来把等号右边的值赋给左边，但是不能单独出现，作为表达式来使用，比如放在if中
python 位运算，n&1 检查是否为奇数，n>>=1来除以二
回溯本质是枚举，假如结果不符合要求，就摒弃

#15（中等） 三数之和
	1.可以利用hash table，把target存一遍，再分别遍历另外两个数，时间复杂度可变为O(n^2)
	2.利用排序+双指针，先排序，然后用一个指针遍历列表作为target，其余两个一个在target之后一位，一个在队尾。三数之和大的话，第二个指针右移一位。小的话，第三个指针左移一位。相等的话，加入结果，直到两个指针相遇。

#206 反转列表
	1. iteration方法，用指针记录前node，现node
	2.recursion,一直recursion到底，返回最后一个node，每返回一层，进行一次操作
	def reverseList(self, head: ListNode) -> ListNode:
        if(not head or not head.next):
            return head
        newhead= self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return newhead

#20 有效的括号
	1.最近相似性的问题用stack解决，遇到左括号加入stack，遇到右括号看是否与左括号匹配。
		匹配的话，弹出左括号。
		不匹配的话，return false
		看最后stack是否为空

#155 最小栈
	1.目的是获取最小数据的速度为O(1)
	做法是多造一个stack存储最小数，当新的元素加入stack时，min_stack也加入当前最小的数
	弹出时，两个stack也同时弹出顶部元素

#141 环形链表
	1.用hash存储经过的node，假如出现存过的，直接返回false，时间O(n),空间O(n)
	2.用快慢指针，假如有环形，快的总会追上慢的。时间O(n),空间O(1)

#142 环形链表2
	1.还是可以用hashtable，把出现过的存入hash table，假如再次出现，那这个node就是环形的入口，时间O(n),空间O(n)
	2.用快慢指针，推导过程见链接
		https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/

#11 盛最多水的容器
	1.枚举，O(n^2)
	2.双指针，夹逼定理。一个指头，一个指尾。哪边的边小，从哪边收敛。O(n)

#84(困难) 柱状图中最大的矩形
	1.双array存每个位置的左边界和右边界，其中掌握假如左边界的height[i-1]>height[i]，那么i的边界等于i-1时的边界，右边同理
	2.用stack，维护一个单调栈，最顶上最大。只有当新元素比顶部小时，开始弹出并计算最大值。其余时间，遇到比顶部大的元素就加入。

#25(困难) k个一组翻转链表
	1.recursion，递归的写法很短，大体分两步
		1.判断后面是否有k个node，没有的话返回head
		2.把当前k个node进行翻转
		3.把最后一个node的一下一个node传入下一个recursion
	2.iteration
		与recursion同理，只不过用wile loop

#06剑指 Offer 从尾到头打印链表
	1.recursion
	2.stack

#23 合并k个升序链表
	1.divide and conquer 分治需要多练习，熟能生巧，本身并不难
	2.stack

#22 括号生成
	1.recursion，找好停止条件和重复部分
		停止条件：左右括号数量都满了
		重复部分：左括号在满之前都可以放入
				右括号在小于左括号时可以放入

#98 验证二叉搜索树
	1.recursion，需要设置上下界 O(n)
		左子树中的所有节点都要比根节点小
		右子树中的所有节点都要比根节点大
		左右子树都是二叉搜素树
		所以需要上下界来判断每个节点的值是否合理
	2.中序遍历的二叉搜索树是单调递增的，这一过程可以用stack来模拟 O(n)
		遍历当前根的所有左节点，弹出一个，更新最小值，再把弹出的右节点设为新根节点

#226 翻转二叉树
	1.recursion，从最底部开始翻转 O(n)
	2. BFS，从上面开始翻转，每次都把下一层用queue存好O(n)

#104 二叉树的最大深度
	1.recursion
	2.BFS

#111 二叉树的最小深度
	1.BFS 
		用queue模拟，假如遇到没有子节点的根节点，直接返回
	2.recursion
		初始根节点没有子节点是特殊情况

#2 两数相加
	1.双指针，一直带着carry计算，最后退出循环时再考虑是否需要多一位

#297 二叉树的序列化与反序列化
	序列化：用deque，遇到节点，加入output,把两个子节点也加入deque
	反序列化：用deque。因为结构是前序，所以第i个的节点是i+2,i+3。假如不是null，就相连，否则跳过去。

#236 二叉树的最近公共祖先
	1.recursion: 
		结束条件为触底，或者遇到了目标1 或 目标2， 返回当前节点
		假如一个节点的左右两个节点都分别有值，证明该点为最近公共祖先
		def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
	        if(not root or root==p or root==q): return root
	        left=self.lowestCommonAncestor(root.left,p,q)
	        right=self.lowestCommonAncestor(root.right,p,q)
	        if(not left):return right
	        if(not right): return left
	        return root   
	2.存储父节点，用map

#3 无重复字符的最长字串
	1.用dictionay只保存合理的string，嵌套了两层，速度很慢
	2.只用一个循环，用dictionary，但不遍历，用两个指针更新头和尾的坐标
	def lengthOfLongestSubstring(self, s):
        st = {}
        i, ans = -1, 0
        for j in range(len(s)):
            if s[j] in st:  #s[j] 为char
                i = max(st[s[j]], i) #st[s[j]]为char的坐标
            ans = max(ans, j - i)
            st[s[j]] = j
        return ans;

#105 从前序与中序遍历序列构造二叉树
	1.recursion 
		前序：[ 根节点, [左子树的前序遍历结果], [右子树的前序遍历结果] ]
		中序：[ [左子树的中序遍历结果], 根节点, [右子树的中序遍历结果] ]
		所以，每次找到根节点的坐标，再按照左子树和右子树的位置传给下一层，时间复杂度O(n)

#77 组合
	1.recursion
		终止条件：当前list长度满了
		过程：添加当前数字
		递归：带着当前数字与新list传入下层

#46 全排列
	1.recursion
		终止条件：当前list满了
		过程：添加当前数字
		递归：把目前可用的数列传入下一层

#47 全排列2
	1.recursion
		创建一个check，记录上一层所使用的数字
		终止条件：当前list满了
		过程：先判断剪枝，添加当前数字
			剪枝：假如当前字母与前一个字母相同，且前一个字母未被使用，跳过这一个分支。因为我们只需要保留一个，我们选择保留最早出现该数字的那条分支
		递归：把当前check与输出传入下层
注：排列组合为题一定要先把list排序！！！！

#50 Pow(x,n)
	1.recursion 这种数字相乘可以用到分治法，divide and conquer,只用算一半，时间复杂度为O(logn)
	2.iteration 
	过于简洁，直接上代码
	def myPow(self, x: float, n: int) -> float:
        ans=1
        if(n<0):
            x,n=1/x,-n
        while(n!=0):
            if(n & 1):
                ans*=x
            x*=x
            n>>=1
        return ans

#78 子集
	1.recursion 回溯递归
	2.iteration 过程过于简洁，上代码
	def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for num in nums:
            ans+= [[num]+sub for sub in ans]
        return ans

#169 多数元素
	1.我的做法：
		先排序，再遍历，假如出现数量超过一半以上，直接reture
	2.巧妙的办法：
		因为出现超过一半以上，所以排序后，中点位置一定是该数
	def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

#17 电话号码的字母组合
	1.回溯法：
		在主function中设置一个存储电话号码和对英字母的map
		在helper function中：
			存入当前数字的位数，把对应的字母分别和上一层的output结合，传入下一层

#51 N皇后
	1.回溯法：
	本题需要了解一个核心概念，即皇后的进攻路线是两条对角线和横竖两条线，其余的算法和其他回溯并无太大差异，难点在于实现起来比较麻烦
	2.大神极简代码：
		def DFS(queens, xy_dif, xy_sum):
	        p = len(queens)
	        if p==n:
	            result.append(queens)
	            return None
	        for q in range(n):
	            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
	                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
	    result = []
	    DFS([],[],[])
	    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

