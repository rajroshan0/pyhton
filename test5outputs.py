Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 12, in <module>
    print(stats(P,Q))
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 6, in stats
    vol = len(p)
UnboundLocalError: local variable 'p' referenced before assignment

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
[27, 31, 30, 52, 42, 39, 12, 41, 109]
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
[27, 31, 30, 52, 42, 39, 12, 41, 109] 9
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
13
2
7
21
16
16
5
13
37
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
(9, 130, 14.444444444444445)

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 16, in <module>
    print(stats(P,Q))
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 10, in stats
    return vol,sum_of_sample,P_mean
NameError: name 'vol' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 20, in <module>
    print(stats(P,Q))
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 8, in stats
    P_mean = summ_of_sampleP/vol
NameError: name 'summ_of_sampleP' is not defined. Did you mean: 'summof_sampleP'?

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
9 130 14.444444444444445
9 253 28.11111111111111
(None, None)

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
9 130 14.444444444444445
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
the stdev 860.2222222222223
9 130 14.444444444444445
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 29, in <module>
    print(stats(P,Q))
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 11, in stats
    stdev = sqrt(sum((i-P_mean)**2 for i in P))
NameError: name 'sqrt' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
the stdev 29.32954520994525
9 130 14.444444444444445
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
the stdev 9.725237627615083
9 130 14.444444444444445
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
the stdev 9.725237627615083
9 130 14.444444444444445
the stdev 17.08764624870809
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
the stdevP 9.725237627615083
9 130 14.444444444444445
the stdevQ 17.08764624870809
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 37, in <module>
    print(stats(P,Q))
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 10, in stats
    P_median = P[(vol+1)/2]
TypeError: list indices must be integers or slices, not float

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 38, in <module>
    print(stats(P,Q))
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 10, in stats
    P_median = P[m]
TypeError: list indices must be integers or slices, not float

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 39, in <module>
    print(stats(P,Q))
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 11, in stats
    P_median = P[m:i]
NameError: name 'i' is not defined. Did you mean: 'id'?

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median_p 16
the stdevP 9.725237627615083
9 130 14.444444444444445
the stdevQ 17.08764624870809
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median_p 16
the stdevP 9.725237627615083
9 130 14.444444444444445
the stdevQ 17.08764624870809
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median_p 16
the stdevP 9.725237627615083
9 130 14.444444444444445
the stdevQ 17.08764624870809
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median_p 16
the stdevP 9.725237627615083
9 130 14.444444444444445
the stdevQ 17.08764624870809
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
4 a the median
median_p 16
the stdevP 9.725237627615083
9 130 14.444444444444445
the stdevQ 17.08764624870809
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median_p 16
the stdevP 9.725237627615083
9 130 14.444444444444445
the stdevQ 17.08764624870809
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
the stdevP 9.725237627615083
9 130 14.444444444444445
the stdevQ 17.08764624870809
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 52, in <module>
    print(stats(P,Q))
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 44, in stats
    return(vol,mean_P, mean_Q, median_P, median_Q, stdevP, stdevQ)
NameError: name 'mean_P' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 52, in <module>
    print ("check symmetric",symmeasure())
NameError: name 'symmeasure' is not defined. Did you mean: 'symmMeasure'?

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 52, in <module>
    print ("check symmetric",symmMeasure())
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 48, in symmMeasure
    if P_mean - P_median <= 3*stdevP :
NameError: name 'P_mean' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 45, in <module>
    from stats import vol,P_mean, Q_mean, P_median, Q_median, stdevP, stdevQ
ModuleNotFoundError: No module named 'stats'

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 51, in <module>
    print ("check symmetric",symmMeasure())
TypeError: symmMeasure() missing 3 required positional arguments: 'P_mean', 'P_median', and 'stdevP'

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 51, in <module>
    print ("check symmetric",symmMeasure(P_mean,P_median,stdevP))
NameError: name 'P_mean' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 51, in <module>
    print ("check symmetric",symmMeasure(P_mean,P_median,stdevP))
NameError: name 'P_mean' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 52, in <module>
    print("check symmetric", symmMeasure(P_mean, P_median, stdevP))
NameError: name 'P_mean' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/bugfix 5.py
median of P 16
the stdevP 10.369560153534854
9 130 14.444444444444445
median of Q 26
the stdevQ 18.155195154861627
9 253 28.11111111111111
check symmetric symmetric

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 52, in <module>
    print("check symmetric", symmMeasure(P_mean, P_median, stdevP))
NameError: name 'P_mean' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 52, in <module>
    print("check symmetric", symmMeasure(P_mean, P_median, stdevP))
NameError: name 'P_mean' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/bugfix 5.py
median of P 16
the stdevP 10.369560153534854
9 130 14.444444444444445
median of Q 26
the stdevQ 18.155195154861627
9 253 28.11111111111111
check symmetric symmetric

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 52, in <module>
    print("check symmetric", symmMeasure(P_mean, P_median, stdevP))
NameError: name 'P_mean' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 62, in <module>
    print("check symmetric", symmMeasure(P_mean, P_median, stdevP))
NameError: name 'P_mean' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 45, in <module>
    vol, P_mean, Q_mean, P_median, Q_median, stdevP, stdevQ = stats_result
NameError: name 'stats_result' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
check symmetric symmetric

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
check symmetric symmetric

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
check symmetric symmetric
9.725237627615083
None

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
check symmetric symmetric
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 65, in <module>
    print("the correlation coefficient is", corr)
NameError: name 'corr' is not defined

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
check symmetric symmetric
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 65, in <module>
    print("the correlation coefficient is",corrCoeff())
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 63, in corrCoeff
    corr = sum((i-P_mean)*(j-Q_mean)for i,j in (P,Q))
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 63, in <genexpr>
    corr = sum((i-P_mean)*(j-Q_mean)for i,j in (P,Q))
ValueError: too many values to unpack (expected 2)

= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
check symmetric symmetric
Traceback (most recent call last):
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 65, in <module>
    print("the correlation coefficient is",corrCoeff())
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 63, in corrCoeff
    corr = sum((i-P_mean)*(j-Q_mean)for i,j in (P,Q))
  File "/Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py", line 63, in <genexpr>
    corr = sum((i-P_mean)*(j-Q_mean)for i,j in (P,Q))
ValueError: too many values to unpack (expected 2)
>>> 
= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
check symmetric symmetric
the correlation coefficient is 1244.5555555555554
>>> 
= RESTART: /Users/rajroshan/Downloads/6 semester copy/Ankeev sir/Big Data/BIG_DATA PART 2 LABS/test5.py
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
(9, 14.444444444444445, 28.11111111111111, 16, 26, 9.725237627615083, 17.08764624870809)
median of P 16
the stdevP 9.725237627615083
9 130 14.444444444444445
median of q 26
the stdevQ 17.08764624870809
9 253 28.11111111111111
check symmetric symmetric
the correlation coefficient is 0.8263481210053438
