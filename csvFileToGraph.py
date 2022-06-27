import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ADL_202_ex.csv') # Opening CSV File

OverallMean = df['Mark'].mean() # Mean of whole Dataset

# Mean Line Plotting
X_Axis = df['Sl No']
Y_Axis = [OverallMean] * len(X_Axis)
plt.plot(X_Axis, Y_Axis, color='green', linestyle= 'dotted')

# ------------------------------------------------------------------------------------------------------------------------- #

# MALE DATA MANIPULATION
maleData = df.loc[df['Gender']=='m'] # Separating Male's Data
maleLowestMark = maleData['Mark'].min() # Male's min mark
maleHighestMark = maleData['Mark'].max() # Male max mark

# Male man mark plotting
maleHighers = df.loc[(df['Mark'] == maleHighestMark) & ( df['Gender'] == 'm')] # Male's max marks for graph plotting
plt.scatter(maleHighers['Sl No'], maleHighers['Mark'], marker='x', facecolor = 'green') # Scatter Plotting

# Male min mark plotting
maleLowers = df.loc[(df['Mark'] == maleLowestMark) & ( df['Gender'] == 'm')] # Male's min marks for graph plotting
plt.scatter(maleLowers['Sl No'], maleLowers['Mark'], marker='.', facecolor = 'red') # Scatter Plotting

# ------------------------------------------------------------------------------------------------------------------------- #
 
# FEMALE DATA MANIPULATION
femaleData = df.loc[df['Gender']=='f'] # Separating Female's Data
femaleLowestMark = femaleData['Mark'].min() # Female min mark
femaleHighestMark = femaleData['Mark'].max() # Female max mark

# Female man mark plotting
femaleHighers = df.loc[(df['Mark'] == femaleHighestMark) & ( df['Gender'] == 'f')] # Female's max marks for graph plotting
plt.scatter(femaleHighers['Sl No'], femaleHighers['Mark'], marker='x', facecolor = 'blue') # Scatter Plotting

# Female min mark plotting
femaleLowers = df.loc[(df['Mark'] == femaleLowestMark) & ( df['Gender'] == 'f')] # Female's min marks for graph plotting
plt.scatter(femaleLowers['Sl No'], femaleLowers['Mark'], marker='o', facecolor = 'orange') # Scatter Plotting

# ------------------------------------------------------------------------------------------------------------------------- #

plt.xlabel("Serial Number")
plt.ylabel("Marks")

# Key Box
plt.legend(["Mean Line", "Male's Highest Marks", "Male's Lowest Mark", 
            "Female's Highest Marks", "Female's Lowest Mark"], bbox_to_anchor = (1.5 , 1.03))

plt.show() # Displaying the Graph

print("CONCLUSION\nFrom the above graph we could say that", '\033[1m' + 'Females performs better.' + '\033[0m')
print("Reason: Females has most High marks and Males has most Low marks.")