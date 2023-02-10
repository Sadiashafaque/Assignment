class GraduationCeremony:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def solve1(self):
        """
        Dynamic Programing Memoization
        """
        def rec(i,ml,ma,dp):

            if i == -1:
                return 1
            if dp[i][ml] != -1:
                return dp[i][ml]
            ans=0
            if ml>0:
                ans = ans + rec(i-1,ml-1,ma,dp)
            
            ans = ans + rec(i-1,ma,ma,dp)
            dp[i][ml] = ans;           

            return ans

        
        dp = [[-1] * (self.m + 1) for _ in range(self.n + 1)]
        rec(self.n - 1, self.m -1, self.m -1, dp)  # total number of valid way to attend classes
        x1 = dp[self.n -1][self.m - 1]
        x2 = dp[self.n -2][self.m - 2]
        print("The number of ways to attend classes over {} days is: {}".format(self.n,x1))
        print("The probability of missing graduation ceremony is {}/{} ".format(x2,x1))

    def run(self):
        self.solve1()
