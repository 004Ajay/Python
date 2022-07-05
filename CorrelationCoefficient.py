import numpy as np
from scipy.stats import pearsonr

hand = [17, 15, 19, 17, 21]
height = [150, 154, 169, 172, 175]

# To find is there correlation is present or not
value = np.corrcoef(hand, height)
print("Correlation value: ")
print(value)

# To find percentage of correlation using pearsonr
val = pearsonr(hand, height)
lst = list(val)
print("Pearsonr value: ", lst)
if lst[1] > 0.05:
    print("We reject Null Hypothesis, since", round(lst[1], 5), "is greater than 0.05")
else:
    print("We accept Null Hypothesis")