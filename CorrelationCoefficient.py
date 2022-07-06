import numpy as np # For Correlation Coefficient
from scipy.stats import pearsonr # For Pearson r value 

hand = [17, 15, 19, 17, 21]
height = [150, 154, 169, 172, 175]

# To find is there correlation is present or not
corrValue = np.corrcoef(hand, height)
print(f"Correlation value:\n{corrValue}") # For simplicity, f-string is used

# To find percentage of correlation using pearsonr
lst = list(pearsonr(hand, height))
print("Pearsonr value: ", lst)
if lst[1] > 0.05: # Not sure about this...
    print(f"We reject Null Hypothesis, since, {round(lst[1], 5)} is greater than 0.05")
else:
    print("We accept Null Hypothesis")