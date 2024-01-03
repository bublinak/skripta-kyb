from sklearn import linear_model
import matplotlib.pyplot as plt

x = [[0, 0], [1, 1]]
y = [0, 1]

for i, j in zip(x, y):
    print(i,j)
    if j == 0:
        plt.plot([i], 'r*')
    else:
        plt.plot([i], 'b*')
        
reg = linear_model.LinearRegression()
reg.fit(x, y)
print(reg.coef_)



