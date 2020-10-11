def checkRecord(self, n: int) -> int:
        if not n: return 0
        dp00=dp01=dp10=1 #第一个数字表示几个A，第二个表示几个连续的L
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