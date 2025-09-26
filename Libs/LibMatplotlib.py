import numpy as np
import matplotlib.pyplot as plt
import random

# x_data = np.random.random(1000) * 100
# y_data = np.random.random(1000) * 100


# plt.scatter(x_data, y_data, c = "blue", marker = "*", s = 150, alpha=0.3) 
# plt.show()









# """years = []
# for i in range (16):
#     years.append(2006+i)"""
# years = [2006 + x for x in range(16)]

# weights = []
# for i in range(16):
#     weights.append(random.randint(79,89))

# plt.plot(years, weights, c="g", lw=4 , linestyle="--")
# plt.show()








# x = ["Python", "C++", "Java", "C", "JS"]
# y = [140, 60, 80, 50, 120]
# plt.bar(x, y, color="b", edgecolor = "g", width = .5 , align="edge")
# plt.show()








# ages = np.random.normal(20, 1.5, 1000)

# plt.hist(ages, bins=20, cumulative=True)
# #OR
# # plt.hist(ages, bins=[ages.min(), 18, 21, ages.max()])
# plt.show()








# x = ["Python", "C++", "Java", "C", "JS"]
# y = [140, 60, 80, 50, 120]
# z = [0, 0, 0, 0.2, 0]

# plt.pie(y, labels = x, explode = z, autopct = "%.1f%%", pctdistance=.8, startangle=160)
# plt.show()






# heights = np.random.normal(172, 8, 300)

# plt.boxplot(heights)
# plt.show()






# years = [2014,2015, 2016, 2017, 2018, 2019, 2020, 2021]

# income = [55, 56, 62, 61, 72, 72, 73, 75]

# income_ticks = list(range(50, 81, 2))

# plt.plot(years, income)
# plt.title("Yearly Income of John", fontsize = 20)
# plt.xlabel("Years")
# plt.ylabel("Income")
# plt.yticks(income_ticks, [f"${x}K" for x in income_ticks])
# plt.show()







# stock_a = [100, 97, 101, 99, 97, 94, 95, 93]
# stock_b = [97, 95, 98, 100, 101, 97, 98, 95]
# stock_c = [90, 92, 97, 94, 91, 93, 95, 98]

# plt.plot(stock_a, label = "Company_1")
# plt.plot(stock_b, label = "Company_2")
# plt.plot(stock_c, label = "Company_3")

# plt.legend(loc = "lower right")
# plt.show()








# x1, y1 = np.arange(100), np.random.random(100)
# x2, y2 = np.random.random(100), np.random.random(100)

# plt.figure(1)
# plt.plot(x1, y1)

# plt.figure(2)
# plt.scatter(x2, y2)

# plt.show()









# x = np.arange(100)
# fig ,axs = plt.subplots(2,2)

# axs[0,0].plot(x, np.sin(x))                          #top left
# axs[0,0].set_title("Sine Wave")

# axs[0,1].plot(x, np.cos(x))                          #top right
# axs[0,1].set_title("Cose Wave")

# axs[1,0].plot(x, np.tan(x))                          #bottom left
# axs[1,0].set_title("Tan Wave")

# axs[1,1].scatter(x, np.random.random(100))           #bottom right
# axs[1,1].set_title("Random")

# fig.suptitle("Four plots")
# plt.show()







ax = plt.axes(projection = "3d")

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

ax.scatter(x, y, z)
ax.set_title("3D Plot")
plt.show()