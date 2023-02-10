class GraduationCeremony:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def func(self):
        """
        Dynamic Programing Memoization
        """
        def recursiveFunc(i,ml,ma,dp):

            if i == -1:
                return 1
            if dp[i][ml] != -1:
                return dp[i][ml]
            ans=0
            if ml>0:
                ans = ans + recursiveFunc(i-1,ml-1,ma,dp)
            
            ans = ans + recursiveFunc(i-1,ma,ma,dp)
            dp[i][ml] = ans;           

            return ans

        
        dp = [[-1] * (self.m + 1) for _ in range(self.n + 1)] # a matrix to store the function calls
        recursiveFunc(self.n - 1, self.m -1, self.m -1, dp)  # recursive call to know total valid pemutations from n days
        x1 = dp[self.n -1][self.m - 1] # this tells the number of ways to attend class for given constraints
        x2 = dp[self.n -2][self.m - 2] # this tells those permutations in which last days was absent
        print("The number of ways to attend classes over {} days is: {}".format(self.n,x1))
        print("The probability of missing graduation ceremony is {}/{} ".format(x2,x1))

    def run(self):
        self.func()
