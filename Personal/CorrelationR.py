# Maths problem calculation

import math
import statistics

x = [10, 12, 15, 30, 25, 27, 32]
y = [70, 2, 80, 100, 11, 16, 7]

n_div = 1/len(x)
x_mean = round(statistics.mean(x), 4)
y_mean = round(statistics.mean(y), 4)
xy_bar = round(x_mean * y_mean, 4)

XiYi, Xi_sq, Yi_sq = [], [], []
Xi_sq_sum, Yi_sq_sum, XiYi_sum = 0, 0, 0

for i in range(len(x)):
    x_mean_sq = round(x_mean * x_mean, 4)
    y_mean_sq = round(y_mean * y_mean, 4)

for i in range(len(x)):
    Xi_sq.append(x[i]*x[i])
    Yi_sq.append(y[i]*y[i])

for i in range(len(x)):    
    XiYi.append(x[i] * y[i])
    
Xi_sq_sum = sum(Xi_sq)
Yi_sq_sum = sum(Yi_sq)
XiYi_sum = sum(XiYi)

Pxy = ((n_div)*XiYi_sum) - xy_bar
sig_x = math.sqrt(((n_div)*Xi_sq_sum) - x_mean_sq)
sig_y = math.sqrt(((n_div)*Yi_sq_sum) - y_mean_sq)
r = Pxy / (sig_x * sig_y)

print(f"\n{'-'*73}\n| x\t|\ty\t|\tXiYi\t|\tXi_sq\t|\tYi_sq\t|\n{'-'*73}")
for i in range(len(x)):
    print(f"| {x[i]}\t|\t{y[i]}\t|\t{XiYi[i]}\t|\t{Xi_sq[i]}\t|\t{Yi_sq[i]}\t|\n{'-'*73}")   
print(f"\nx̄: {x_mean}\t|\tȳ: {y_mean}\t|\tx̄ȳ: {xy_bar}\t|\tΣXiYi: {XiYi_sum}\t|\n")
print(f"\nΣx̄^2: {x_mean_sq}\t|\tΣȳ^2: {y_mean_sq}\t|\tΣXi^2: {Xi_sq_sum}\t|\tΣYi^2: {Yi_sq_sum}\t|\n\n{'-'*90}")     
print(f"\nPxy: {round(Pxy, 4)}\t|\tσx: {round(sig_x, 4)}\t|\tσy: {round (sig_y, 4)}\t|\tr: {round(r, 4)}\n\n{'-'*90}")
