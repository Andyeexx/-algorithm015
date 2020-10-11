学习笔记

MIT五步DP
1. define subproblems
2. guess(part of solution)
3. relate subproblem solutions
4. recurse & memorize / build DP table bottom-up
5. solve original problem

#538 把二叉搜索树转换为累加树
	1.recursion 反序中序遍历
		设置一个全局变量，先访问右子树，之后把根的值加在这个全局变量上，把根重新赋值，再访问左子树
	2. stack 模拟
		stack从根一路加，加到最右的子树，弹出，更新全局变量，重新赋值弹出的节点，接着访问弹出点的左子树

#18 四数之和
	1.此题和三数之和同理，两个循环确定头和尾的两个数，另外两个数分别用指针指向‘头后面一位’与‘尾前面一位’。假如四数之和小于target，前指针后移。假如大于target，后指针前移。

#62 不同路径
	1.使用动态规划，最上和最左的步数都是1，其他的步数为 grid[i][j]=grid[i-1][j]+grid[i][j-1]

#63 不同路径2
	1.使用动态规划，方法和62相同，只不过grid最开始生成时，需要考虑障碍物，假如有障碍物，之后的位置都过不去

#37 解数独
	1.使用回溯，和N皇后相似，存好限制条件的list，判断每个位置。因为大神代码太强了，想存一下
	def solveSudoku(self, board: List[List[str]]) -> None:
        nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        palace = [[set() for _ in range(3)] for _ in range(3)]  # 3*3
        blank = []
        # 初始化，按照行、列、宫 分别存入哈希表
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == ".":
                    blank.append((i, j))
                else:
                    row[i].add(ch)
                    col[j].add(ch)
                    palace[i//3][j//3].add(ch)
        def dfs(n):
            if n == len(blank):
                return True
            i, j = blank[n]
            rst = nums - row[i] - col[j] - palace[i//3][j//3]  # 剩余的数字 		#神来之笔
            ### rst = nums - (row[i] | col[j] | palace[i//3][j//3])  
            if not rst:
                return False
            for num in rst:
                board[i][j] = num
                row[i].add(num)
                col[j].add(num)
                palace[i//3][j//3].add(num)
                if dfs(n+1):
                    return True
                row[i].remove(num)
                col[j].remove(num)
                palace[i//3][j//3].remove(num)
        dfs(0)

#1143 最长公共子序列
	1.使用动态规划，动态方程是 
		If S1[-1] == S2[-1]: LCS[s1, s2] = LCS[s1-1, s2-1] + 1
		If S1[-1] != S2[-1]: LCS[s1, s2] = Max(LCS[s1-1, s2], LCS[s1, s2-1])
		

#120 三角形最小路径和
	1.使用动态规划，可以自上而下，自下而上
		将dp初始化为triangle本身，每个位置只由对应的那两个位置改变
		也可以将dp初始为triangle最后一行，自下往上，和上面的方法本质相同
		代码总结：https://leetcode.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-(top-down-bottom-up)

#53 最大子序和
	1.使用动态规划
		dp问题公式为
			dp[i] = max(0, dp[i-1])+nums[i]  
		 或者dp[i] = max(nums[i],nums[i]+dp[i-1])
		最大子序和=当前元素自身最大，或者包含之前后最大

#152 乘积最大子数组
	1.使用动态规划
	def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        ma=mi=ans=nums[0]
        for num in nums[1:]:
            tmp1,tmp2= ma*num, mi*num      # tmp2 用来存储ma的值，防止遇到-1，为之后的-1作准备
            ma=max(tmp1,tmp2,num)
            mi=min(tmp1,tmp2,num)
            print(ma,mi)
            ans= max(ans,ma)
        return ans

#106 从中序与后序遍历序列构造二叉树
	1.考察中序与后序的遍历顺序
	后序：左右根
	中序：左根右，
	我们可以从后序确定根，然后在中序中找到根的位置，分别吧左右子树传入下一层

#75	颜色分类
	1.使用三指针，一个指0部署的位置，一个指2部署的位置，一个指针遍历整个list，前提是不超过最后一个指针
	注意：和第二个指针交换数字时，需要让遍历指针停一次，因为刚换过来的数还没有被检查

#198 打家劫舍
	1.使用动态规划，创建二维dp，分别存储偷与不偷当前住户。
		dp[i][0]= max(dp[i-1][0], dp[i-1][1])
        dp[i][1]= dp[i-1][0]+nums[i]
   	2.简化方法一,创建一维dp，存储偷与不偷的最大值
   		dp[i]=max(dp[i-1],dp[i-2]+nums[i])
   	3.再简化，像斐波那契一样，只用两个指针存储上一个值和当前值
   		pre,cur = cur, max(pre+i,cur)
#213 打家劫舍2
	1.属于打家劫舍1的变种，只需将1的部分分别在包含第一个房子和包含第二个房子的list里跑一遍，再比大小即可
	max(helper(nums[1:]),helper(nums[:-1]))

#112 路径总和
	1.使用dfs，注意结束条件除了空节点还有叶子节点的父节点，假如只有一个空节点作为结束条件，就会call两遍叶子节点的结果

#113 路径总和2
	1.使用dfs，和112的区别就是加了个路径当作参数

#518 零钱兑换2
	1. 此题和爬楼梯本质一样，假如每次跨的步数可以是1，2，5
	DP[i] = DP[i-1] + DP[i-2] + DP[i-5], 也就是DP[i] = DP[i] + DP[i-j] ,j =1,2,5
	代码：
		def change(self, amount: int, coins: List[int]) -> int:
	        dp=[0]*(amount+1)
	        dp[0]=1
	        for coin in coins:
	            for i in range(coin,amount+1):
	                dp[i]+= dp[i-coin]
	        return dp[-1]

#121 买卖股票的最佳时机
	1.使用动态规划
		mini=min(prices[i],mini)
        dp[i]= max(dp[i-1],prices[i]-mini)

#122 买卖股票的最佳时机2
	1.使用动态规划
		dp[i][0]=max(dp[i-1][0], dp[i-1][1]+prices[i])  #卖出
        dp[i][1]=max(dp[i-1][1], dp[i-1][0]-prices[i])  #买入

#123 买卖股票的最佳时机3
	1.使用动态规划，dp大小为（n,3,2）n天，3包含第0-2次交易，2为持股与不持股
		初始化：第一天，所有次数的股，持股的利润为-prices[i]
		dp[i][j][0]=max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])			#i为天数，j为第j次交易的额股票
        dp[i][j][1]=max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

#309 最佳买卖股票时机含冷冻期
	1.使用动态规划。因为有冷冻期，所以每次买入时的利润应该是前一天不持股的利润减去当前价格
		dp长度应该增加一个第0天，方便计算第二天
		初始化，第一天的买入价格为-prices[0]
		dp[i][0]= max(dp[i-1][0], dp[i-1][1]+prices[i-1])
        dp[i][1]= max(dp[i-1][1], dp[i-2][0]-prices[i-1])

#714 买卖股票的最佳时机含手续费
	1.使用动态规划，和122一样，只不过买入时多扣一笔
		dp[i][0]= max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1]= max(dp[i-1][1], dp[i-1][0]-prices[i]-fee)
    空间优化后，只需要两个数据来存dp，即滚动数组优化 
    	初始化：dp=[0,-prices[0]]
    	dp[0]= max(dp[0], dp[1]+prices[i])
        dp[1]= max(dp[1], dp[0]-prices[i]-fee)

#188 买卖股票的最佳时机4
	1.使用动态规划，和123一样，只不过用k取代2，并且在k过大时，比如k>len(prices)/2时，当作可操作无限次，执行122即可
	if k>= len(prices)//2:
            dp=[0,0]
            dp[1]= -prices[0]
            for i in range(1,len(prices)):
                dp[0]=max(dp[0],dp[1]+prices[i])
                dp[1]=max(dp[1],dp[0]-prices[i])
            return dp[0]

#64 最小路径和
	1.使用动态规划，此题是最基础的动态规划题，不用新建dp，可直接在原grid上修改
	grid[row][col]+=min(grid[row-1][col], grid[row][col-1])

#647 回文子串
	1.使用中心扩展法，两个循环分别代表substring的头和尾。注意遍历方向。

#221 最大正方形
	1. 使用动态规划
	dp数组含义：dp[i][j] 为以i行j列的坐标为正方形的右下角的正方形能达到的最大的变长
	dp=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
	动态转移方程：
	当matrix[i-1][j-1]为1时，dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1，即上，左上，左的位置的最小值

# 2的幂
	1.使用常规方法，一直整除以二，看最后余数
	1.使用位运算，n & (n-1)==0是假如一个数是二的次幂

#解码方法2
	1.使用动态规划，做法与解码方法一致，只不过加了很多限定条件，不建议再做。浪费时间

#621 任务调度器
	此题的核心概念是greedy algorithm
	1. 使用循环，每次都优先执行列表中剩余频次最高的任务，每次循环后都重新排列列表
	2. 是用数学公式，只有可能两种情况出现：
		1.高频次不大，小频次很多，即没有待命的情况出现，返回原长度
		2.高频词很大，有待命出现，假如最高频次的数量是x,冷却时间为n，最小时间为，(x-1)*(n+1)+list.count(x)
		list.count(x)是计算有多少相同的最高频次会跑到最后

#32 最长有效括号
	1.使用stack，先存入-1, 此-1代表第一个字母的前一个坐标，是为了方便计算计算长度；stack[0]这个位置表示目前合理的的非左括号的位置
	算法：遇到左括号加入栈
		遇到右括号，弹出顶部元素
		假如stack为空，证明当前右括号不合理，当前位置为最新的边界
		假如stack不空，证明当前括号依然合法，并计算最新长度
	2.使用计数，从左到右一次，从右到左一次
		从左到右，假如遇到 '(', left+1，
				假如遇到')', right+1, 假如right==left, left和right都清零， 假如right<left, 那目前的长度为 2*right
		从右到左，和上面相反
	3.使用动态规划
		此题的动态规划不容易想到，我们只考虑查询到')'的情况，
		假如i为')',i-1为'(',dp[i]=dp[i-2]+2
		假如i为')',i-1为')',并且 s[i-dp[i-1]-1]为'(',那证明当前右括号合理
		dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2

#72 编辑距离
	1.使用动态规划，dp为二维存储， dp[i][j]代表word1到i位置和word2到j位置使用的最少的操作数
	动态转移方程： 
	if word1[i-1]==word2[j-1]: dp[i][j]=dp[i-1][j-1]
    if word1[i-1]!=word2[j-1]: dp[i][j]= min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
    其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。

#363 矩形区域不超过 K 的最大数值和
	1.此题的暴力解法是使用动态规划，将左上角和右下角的坐标作为循环框架，会使用四次循环，时间复杂度是O(m^2 n^2)
	每确定一个左上角，建立一个二维dp，存储右下角所表达的矩形的面积
		dp=[[0]*(col+1) for _ in range(row +1) ]        
	    dp[i1][j1]=matrix[i1-1][j1-1]
	对于每个右下角：i2,j2是由i1 j1确定边界的
		dp[i2][j2]= dp[i2-1][j2]+dp[i2][j2-1]-dp[i2-1][j2-1]+matrix[i2-1][j2-1]
	2.数组滚动
	先固定左右边界，不断压入 行累计数组，方法过于需要搭配图形，此处配上链接
	https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/javacong-bao-li-kai-shi-you-hua-pei-tu-pei-zhu-shi/

#403 青蛙过河
	1.使用动态规划，dp为一维存储，dp=[set() for _ in range(n)] 每个dp[i]包含了跳到第i个岛的所有步数
		算法：对于第i个岛，小于i的j的岛，跳到i需要stone[i]-stone[j]的步数，假如这个步数或者步数-1，+1存在于dp[j]中，往dp[i]中加入stone[i]-stone[j]
	2.使用dfs，先将stones变成set，方便使用 in 来查询。创建一个set，用来存储失败的岛屿 与 步数组合
		dfs的传入数据：当前岛屿的标号 和 跳到该岛的步数。
		假如标号等于目标岛屿的标号，返回True
		加入标号与步数组合已经出现过，返回False
		speed+1,speed-1, speed 三种速度施加于当前标号，假如新的标号出现在stones里，则可以跳到这个新岛，传入下一层
		在最外层返回False,因为True没有触发

#410 分割数组的最大值
	1.使用动态规划，dp[i][j]定义：前i个数字，分为j组的最小最大数
		理解分组模式：1到k分成j-1组，k+1到i分成一组，合并起来分为j组
		dp[i][j]=min(dp[i][j], max(dp[k][j-1], sum[i]-sum[k]))
		可以提前建立一个presum计算前i个数的合
		i:1~n
		j:1~min(i,m)
		k:1~i-1
		注：此方法python会超时

	2. 使用二分搜索，左边界为最大的数，即max(nums)；右边界为最大的和，即sum(nums)
	判断条件：以当前mid为基准，看nums可以分成多少个sub-list。
		假如分的数量比m大，即分多了，mid定小了，查右边，left=mid+1；
		假如分的数量比m小，即分少了，mid定大了，查左边，right=mid

#552 学生出勤记录2
	1.使用回溯算法，通过剪枝规避不可奖励的情况，本质上是暴力算法
	2.使用动态规划，
		dp[i][j]：我们这种方法自动排除了不可奖励的情况
		i为0或1，代表是否有A
		j为0或1或2，代表有几个连续的L
		def checkRecord(self, n: int) -> int:
	        if not n: return 0
	        dp00=dp01=dp10=1
	        dp11=dp12=dp02=0
	        mod=10**9+7
	        for i in range(2,n+1):
	            dp00,dp01,dp10,dp11,dp12,dp02=(
	                (dp00+dp01+dp02)%mod,
	                dp00,
	                (dp10+dp11+dp12+dp00+dp01+dp02)%mod,
	                dp10,
	                dp11,
	                dp01
	            )
	        return (dp00+dp01+dp10+dp11+dp12+dp02)% mod

#76 最小覆盖子串
	1. 使用滑动窗口
	参考链接：https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/
	i为左边界，j为右边界
	步骤1:i不变，不断增加j使滑动窗口增大，直到窗口包含了T的所有元素
	步骤2:j不变，不断减小i使滑动窗口减小，知道i遇到的必要元素只剩一个时停止，此时是局部的最小长度，存入结果备用
	步骤3:让i增加一个位置，循环步骤1的操作，知道j扫描完最后一个字母
	实际操作：用一个dict来记录遇到的字母，先用T中的所有字母初始化，之后在S中遇到一个字母，need[c]就-1，假如need[c]为0就是完美的，假如所有need[c]都小于等于0，那就是局部最小
	优化：设计一个needcount来计数所有T中的元素是否都遍历过了，needcount初始化为s的长度。在步骤1中，假如need[c]大于0，则needcount-1

#312 戳气球
	1.使用动态规划
	参考链接：https://leetcode-cn.com/problems/burst-balloons/solution/zhe-ge-cai-pu-zi-ji-zai-jia-ye-neng-zuo-guan-jian-/
	核心理解：dp[i][j]表示，以i，j为开区间，所能拿到的最多金币，意思是，不戳i和j
	转移方程：dp[i][j]=dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j]
	解释：因为k是最后一戳，所以dp[i][k]和dp[k][j]在这之前都已经被各自戳过了，直接加入计算就可以了

#279 完全平方数
	1.使用动态规划
	dp[i]代表n=i 时，使用的最少的完全平方数
	dp[i]=min(dp[i], dp[i-j]+1) j=从0到n的所有完全平方数
	空间优化：提前预存从0～n的所有完全平方数
	2.使用BFS，每弹出来一次，用弹出来的数减去从0～该数的所有完全平方数，记录步数，再传入deque
	

