from solution import GraduationCeremony

if __name__ == "__main__":
    n = int(input("Enter the number of days: \n"))
    m = 4
    if n < 0 or m < 0:
        raise Exception("Invalid Inputs")
    if n < m:
        print("The number of ways to attend classes over {} days is: {}".format(n,2**n))
        print("The probability of missing graduation ceremony is {}/{} ".format(2**(n-1),2**n))
    else:
        obj = GraduationCeremony(n,m)
        obj.run()
