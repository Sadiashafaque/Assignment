### Assignment

#### Question
In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

#### Prerequisite
`Python 3` must be installed in your local machine.

#### How to run ?
To run the assignment execute following command:
```
python main.py
```
You will be asked to enter the number of days for graduation ceremony

#### Approach
For each day, I am recursively finding out to whether miss class or attend class.If i miss a class, my consective absent decreases by one, other wise it is reset to m. Total possibilities is 2^N, but I am storing the repeating subproblems in a matrix od size n*m. So time complexity becomes polynomial.

**Time Complexity**: O(N * M) where N is number of days, and M is consective days for which I can be absent.
**Space Complexity** : O(N * M) + O(N) for matrix and recursive calls.
