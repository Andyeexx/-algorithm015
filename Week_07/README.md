学习笔记

#并查集模版
	def init(p):  
		p = [i for i in range(n)]  # for i = 0 .. n: p[i] = i

	def union(self, p, i, j): 
		p1 = self.parent(p, i) 
		p2 = self.parent(p, j) 
		p[p1] = p2 
	 
	def parent(self, p, i): 
		root = i 
		while p[root] != root: 
			root = p[root] 
		while p[i] != i: # 路径压缩 
			parent[i],i= root,parent[i]
		return root

#字典树模版
	class Trie(object):
		def __init__(self): 
			self.root = {} 
			self.end_of_word = "#" 
	 
		def insert(self, word): 
			node = self.root 
			for char in word: 
				node = node.setdefault(char, {}) 
			node[self.end_of_word] = self.end_of_word 
	 
		def search(self, word): 
			node = self.root 
			for char in word: 
				if char not in node: 
					return False 
				node = node[char] 
			return self.end_of_word in node 
	 
		def startsWith(self, prefix): 
			node = self.root 
			for char in prefix: 
				if char not in node: 
					return False 
				node = node[char] 
			return True

#A* 模版
	def AstarSearch(graph, start, end):
		pq = collections.priority_queue() # 优先级 —> 估价函数
		pq.append([start]) 
		visited.add(start)
		while pq: 
			node = pq.pop() # can we add more intelligence here ?
			visited.add(node)
			process(node) 
			nodes = generate_related_nodes(node) 
	   		unvisited = [node for node in nodes if node not in visited]
			pq.push(unvisited)

#python技巧：
	1.dict.setdefault(key, default=None)作用和get类似
		假如有对应key，就返回对应的value
		假如没有，就添加(key,default)在dict里，并且返回这个default value
	2.set的合并方式： set()|{a}
		visited | {(i,j)}, 用于dfs传入下一层很好用

#208 实现 Trie (前缀树)
	1. 字典树的实现，
		基础结构：
			静态结构：固定长度array
			动态结构：字典{}
			附加：结尾符号定义
		insert：对于每个字母，进入一个字典中的字典 

#212 单词搜索2
	1.使用字典树+dfs
		流程步骤：1.构建字典树，将所有单词输入字典树中，为了提高查询的效率
				2.构建dfs
				3.遍历二维网格的每个位置，把该位置当作单词的第一个字母开始在trie中查询，并且传入dfs，然后依次在字典树中一层一层的查询

#547 朋友圈
	1.使用dfs，记录一个visited
	循环n个人，假如没遇到过，就代表是一个新的群体，
		对于a来说，假如m[a][b]==1，那就跳转到b，并且a，b都标为visited
		重复以上操作
	2. 使用并查集
	先写好并查集的模版，假如m[a][b]==1,那就合并两个的集合，直到最后
	最后遍历n个人，用set来收集他们的parent，返回即可

#130 被围绕的区域
	1.并查集，从边界入手。
		和边界相连的点，和一个dunmmy合并
		其余的点，和各自的group相连
		最后，遍历所有点，判断是否和dummy相连。假如是，则不变；假如不是，变成'X'
	2.使用dfs，从边界入手，
		假如有'O'。开始dfs，把所有相连的'O'变成'B'
		最后，把所有'O'变成'X'。把'B'变成'O'

#36 有效的数独
	1.此题很简单，就利用三个list(set)来查询是否有不符合规定的数字出现即可

#1091 二进制矩阵中的最短路径
	1.bfs
	2.A*, 优先函数为max(abs(n-1-x),abs(n-1-y)),因为斜对角的距离和水平的同为1

#773 滑动谜题
	1.bfs，
		重点是：
			1.提前存好0所在每个点的可移动位置
			2.想好如何判断board的状态是否是目标状态：转变为string，再判断
			3.使用visited 记录已经经历过的状态，防止死循环
		之后就是和bfs一样，可以改成双向的
	2.A*


