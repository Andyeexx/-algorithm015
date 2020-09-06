学习笔记

面试四步：
	1.clarification 和面试官核对理解的信息：大小写敏感
	2.possible solutions->optimal(time & space)
	3.code
	4.test cases

dictionary常用的function
	1.dic.keys() 返回所有 键
	2.dic.values() 返回所有 值	
	3.dic.items()	返回所有 键和值
	4.dict.clear() 清空dict
	5.dict.get(key,default=None) 返回指定键的值，如果值不在字典中返回default值
	6.dict.has_key(key) 返回key是否在dict中， true 或 false
	7.dict.update(dict2) 把dict2的值/键更新到dict
	8.dict.pop(key) 删除 key和他所对应的value 返回被删除的value
	9.dict.popitem()在Python.7之前的版本中，它会删除随机项，而在3.7版中，它会删除最后插入的项。返回tuple(key,value)
	10.del dict[key] 直接单独删条目
	11.del dict 直接删掉dict

python stack的常用function
注：python3 没有stack模块，所以直接用[] 添加用append，删除用pop，以下为stack通用的指令，但目前没法直接用
	1.Stack(self)     # 创建空栈
    2.is_empty(self)  # 判断栈是否为空
    3.push(self, elem)    # 将元素elem加入栈
    4.pop(self)       # 删除栈中最后加入的元素并将其返回
    5.top(self)           # 取得栈中最后压入的元素，不删除
    6.append() 也可以

python heapq的常用function
注：heapq是小顶堆
	1.heappush(heap,x):x元素插入堆
	2.heappop(heap):弹出对中最小元素
	3.heapify(heap):将heap属性强制应用到任意一个列表
	4.hrapreplace(heap,x):将heap中最小元素弹出，同时x元素入堆
	5.hlargest(n,iter):返回iter中第n大的元素
	6.hsmallest(n,iter):返回iter中第n小的元素

collections.defaultdict()
	1.dict=defaultdict(factory_function)
		这个factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0。
		如果我们不想要value中的元素重复，可以用defaultdict(set)来解决这个问题，set与list不同之处就是set中不允许存在相同的元素。

collections.OrderedDicit()
	1.sorted(iterable,key,reverse)，
		sorted一共有iterable,key,reverse这三个参数。其中iterable表示可以迭代的对象，例如可以是dict.items()、dict.keys()等，key是一个函数，用来选取参与比较的元素，reverse则是用来指定排序是倒序还是顺序，reverse=true则是倒序，reverse=false时则是顺序，默认时reverse=false。采用这种方法可以对字典的value进行排序。注意排序后的返回值是一个list，而原字典中的名值对被转换为了list中的元组。
		>from collections import OrderedDic
		>d={'b':3,'a':4,'c':2,'d':1}
		# 将d按照key来排序
		>OrderedDic(sorted(d.items(),key=lambda t:t[0]))
		OrderedDic([('a',4),('b',3),('c',2),('d',1)])
		# 按照value来排序
		>OrderedDict(sorted(d.items(),key=lambda t:t[1]))
		OrderedDic([('d',1),('c',2),('b',3),('a',4)])
		# 按照key的长度来排序
		>OrderedDic(sorted(d.items(),key=lambda t:len(t[0])))
	2.popitem() 
		使用使用popitem()方法来移除最后一个key-value对.如果我们要删除dict中的key-value,popitem(last=True)按照先进后出的顺序删除dict中的key-value，popitem(last=False)按照先进先出的规则删除dict中的key-value.
	3.move_to_end(key,last=True)
		改变有序的OrderedDict对象的key-value顺序
		d.move_to_end('c') # 将key为c的key-value移动到最后
		d.move_to_end('c',last=False) # 将key为c的key-value移动到最前面

collections.deque()
	1.deque (maxlen=N)
		创建了一个固定长度的队列，当有新的队列已满时会自动移除最老的那条记录
	2.append()
	3.appendleft()
	4.pop()
	5.popleft()

collections.ChainMap()
	1. ChainMap可以合并多个dict，而且效率很高
		>from collections import ChainMap
		> a = {'a': 4, 'c': 2}
		> b = {'b': 3, 'c': 1}
		> c=ChainMap(a,b)
		ChainMap({'a': 4, 'c': 2}, {'b': 3, 'c': 1})
		# 将c变成一个list
		>c.maps
		[{'a': 4, 'c': 2}, {'b': 3, 'c': 1}]

collections.Counter()
	1.统计相关元素出现的次数
	2.elements()
		就是将其中的key值乘以出现次数全部打印出来，当然需要通过list或者其他方式将其所有元素全部展示出来，当出现了负数或者0的情况,负数对应的key值是不会打印的
	3.most_common([n])
		返回value最大的前n个键值对
		n=-1返回空
	4.subtract([iterable_or_mapping])
		c.subtract(d)来进行调用的，如果c中某个元素不存在，则默认其值为0，其实得到的就是将所有元素进行相减的结果 (c,d都是Counter)
	5.Counter支持 
		c.values()
		c.items()
		sum(c.values())
		c.keys()
		c.clear()
		list(c)
		set(c)
		dict(c)
		c += Counter()    #这个是最神奇的，就是可以将负数和0的值对应的key项去掉
collections.namedtuple
	1.命名tuple中的元素，使用namedtuple(typename,field_names)
	>from collections import namedtuple
	>nm=namedtuple('helloworld',['x','y'])
	>n=nm(1,2)
	>n__class__.__name__
	'helloworld'
	>n.x
	1
	>n.y
	2

python 技巧
	1.''.join(list) 将list里的内容和并
	2.[0] * num 创造长度为num的0 list
	3.ord(letter) 可以返回字母的顺序




#239(困难) 滑动窗口的最大值
	1.自己的解法：暴力，不可取
	2.高效的解法：deque
		每次传入的新值和窗口里的旧值去比，比他小的全部删除，确保deque最左侧的数值是窗口中最大的
		使用python中的collection.deque()

#242（简单） 有效的字母异位词
	1. 自己的解法：hash table，利用python的collections.Counter(),假如每个字母的key相应的value相同，则为true

#49（中等） 字母异位词分组
	1.自己的算法：想用collection.Counter()，但发现时间复杂度为O(n^2)
	2.python解法：用sort，然后相同sort结果的放一起
	3.建造一个字母表的list，填入每个字母出现的次数，转化为tuple作为dict的key，让value为原词，最后返回dict的value

#1021(简单)删除最外层的括号
	1. 这种最近相关性的题应该最先想到用stack，遇到'('就加入，遇到')'就弹出顶部。遇到时，假如stack不为空，即非最外层括号，可加入结果
	2. 单指针：
	def removeOuterParentheses(self, S):
        res, count = [], 0
        for c in S:
            if c == '(' and count > 0: res.append(c)
            if c == ')' and count > 1: res.append(c)
            count += 1 if c == '(' else -1
        return "".join(res)

#94 二叉树的中序遍历
	1.recursion 解法，常规解法
	2.用stack模拟recursion，
		弹出顶部node
		假如node被遍历过，加入输出
		假如没有，往stack中加入右，中，左，以及是否被遍历的标签，以此重复

#144 二叉树的前序遍历
	1.recursion 解法，常规解法
	2.用stack模拟recursion，
		弹出顶部node，直接加入结果
		往stack中加入右，左，以此重复

#590 N叉树的后序遍历
	1.recursion 需要用helper function, 因为有多个child，需要用循环
		def postorder(self, root: 'Node') -> List[int]:
        ans=[]
        def helper(root):
            if(not root): 
                return None
            for child in root.children:
                helper(child) 
            ans.append(root.val)
        
        helper(root)
        return ans  

	2.stack 最后的反转是精髓
		def postorder(self, root: 'Node') -> List[int]:
        if(not root):
            return []
        ans=[]
        stack=[root]
        while stack:
            root= stack.pop()
            ans.append(root.val)
            for child in root.children:
                stack.append(child)
        return ans[::-1]

#412 Fizz Buzz
	1. 直接for loop，筛选
	2. 用hash table， 把（3:fizz， 5:buzz）放入table， 对于每个数字，遍历key，假如整除key，string加入value

#589 N叉树的前序遍历
	方法同#590， 遍历child时，从后往前来，后面的先放进去

#429 N叉树的层序遍历
	1. recursion, 用helper function
		def levelOrder(self, root: 'Node') -> List[List[int]]:
	        if(not root):return None
	        ans=[]
	        def helper(node,level):
	            if len(ans)==level:
	                ans.append([])
	            ans[level].append(node.val)
	            for child in node.children:
	                helper(child,level+1)
	        helper(root,0)
	        return ans
    2. 用queue进行BFS：
    	def levelOrder(self, root: 'Node') -> List[List[int]]:
	        if(not root): return None
	        ans=[]
	        queue= collections.deque([root])
	        while(queue):
	            cur_layer=[]
	            for _ in range(len(queue)):
	                node= queue.popleft()
	                cur_layer.append(node.val)
	                queue.extend(node.children)
	            ans.append(cur_layer)
	        return ans   
	3.简化版BFS：
		def levelOrder(self, root: 'Node') -> List[List[int]]:
	        if(not root): return None
	        ans=[]
	        next_layer=[root]
	        while(next_layer):
	            cur_layer=[]
	            ans.append([])
	            for node in next_layer:
	                ans[-1].append(node.val)
	                cur_layer.extend(node.children)
	            next_layer=cur_layer
	        return ans

#258 各位相加
	1. recursion, 用一个helper把数字拆开相加
		def addDigits(self, num: int) -> int:、
	        def helper(num):
	            if(num<10):
	                return num
	            return self.addDigits(num//10)+ num%10
	        num= helper(num)
	        return self.addDigits(num)
	2.O(1)方法，奇招， xyz=100x+10y+z=99x+9y+(x+y+z)
		所以直接算num%9即可得到结果，除了特殊情况
		def addDigits(self, num: int) -> int:
	        if(num<=0):
	            return num
	        if(num%9==0):
	            return 9
	        return num%9

#剑指offer 40 最小的K个数
	1.用sort，暴力解法
	2.用heapq，heapq（小顶堆）中，越小的数优先级越高。所以为了找到最小的k个，我们需要把最小的都放在底部，把大的放在顶部，方便弹出。方法则是把对应数字的负数存入

#264 丑数2 
	注：此题核心是搞懂得到丑数的规律，从1开始，分别呈上2，3，5，得到的数之后依次再乘上2，3，5。以此类推，按大小排序，得到结果。
	1.用heap，从1开始，弹出最小值后，加入结果列表。最小值乘上2，3，5，再分别加入heapq，之后再弹出，再加入新的。
		此方法时间复杂度为O(nlogn)因未每次都要重新排列heap
	2.动态规划(很巧妙)，直接用一个数组表示结果列表，在上面修改，时间复杂度为O(n)
		def nthUglyNumber(self, n: int) -> int:
	        dp,a,b,c=[1]*n,0,0,0
	        for i in range(1,n):
	            dp[i]= min(dp[a]*2, dp[b]*3, dp[c]*5)
	            if dp[a]*2==dp[i] : a+=1
	            if dp[b]*3==dp[i] : b+=1
	            if dp[c]*5==dp[i] : c+=1
	        return dp[-1]

#108 将有序数组转换为二叉搜索树
	1.此题要生成二叉树，所以最直接的方法就是用dfs，因为是升序的数组，直接将数组分为两半，每次找到mid，成为parent节点，再往下分剩余节点

#95 解码方法
	1.动态规划，十分巧妙
	此题的核心概念是斐波那契，s[i]=s[i-1]+s[i-2]，所以可以用两个指针指向s[i-1]和s[i-2]
	当s[i]==0时，判断他是否可以和s[i-1]绑定，假如不可以，直接return 0
	当s[i-1]==1, 可直接运用斐波那契。
	当s[i-1]==2,并 1<=s[i]<=6,可直接运动斐波那契
	假如都不是，则保持两个指针，因为当前情况就相当于所有情况中的一种，即数字各自独立的情况，33333

#107 二叉树的层次遍历2
	1. 用BFS就能解决
