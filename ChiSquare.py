female = [60, 54, 46, 41]
male = [40, 44, 53, 57]
row_total = [100, 98, 99, 98]
col_total = [201, 194]

fem_mul = (col_total[0]/395) # 395 = grand_total
male_mul = (col_total[1]/395)

female_col_mul = []
male_col_mul = []
female_Es = []
male_Es = []

for i in range(len(row_total)):
    fem_row_mul = (row_total[i] * fem_mul)
    male_row_mul = (row_total[i] * male_mul)
    female_col_mul.append(round(fem_row_mul, 4))
    male_col_mul.append(round(male_row_mul, 4))
   
print("Female e value: ", female_col_mul)
print("Male e value: ", male_col_mul)

O = female +  male
E = female_col_mul + male_col_mul

# O : Observed Values, E : Expected Value
print("All observations: ", O)
print("All Expectations:", E)
res = 0
for i in range(len(O)):
    res = res + (((O[i] - E[i]) * (O[i] - E[i]))/E[i])
print("Chi Square value: ", round(res, 4))

# To check the result & find probability:
import scipy.stats as stats
check = stats.chisquare(O, E)
lst = list(check)
print("Verification: ", check)
if lst[1] > 0.05:
    print("We accept Null Hypothesis, since", round(lst[1], 5), "is greater than 0.05")
else:
    print("We reject Null Hypothesis")    