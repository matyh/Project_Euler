"""
https://projecteuler.net/problem=630
Given a set, L, of unique lines, let M(L) be the number of lines in the set and let S(L) be the sum over every line of the number of times that line is crossed by another line in the set. For example, two sets of three lines are shown below:

crossed lines
In both cases M(L) is 3 and S(L) is 6: each of the three lines is crossed by two other lines. Note that even if the lines cross at a single point, all of the separate crossings of lines are counted.

Consider points (T2k−1, T2k), for integer k >=1, generated in the following way:

S0=290797
Sn+1=Sn2mod50515093
Tn=( Snmod2000 )−1000

For example, the first three points are: (527, 144), (−488, 732), (−454, −947). Given the first n points generated in this manner, let Ln be the set of unique lines that can be formed by joining each point with every other point, the lines being extended indefinitely in both directions. We can then define M(Ln) and S(Ln) as described above.

For example, M(L3)=3 and S(L3)=6. Also M(L100)=4948 and S(L100)=24477690.

Find S(L2500).


"""