# starting line graph
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()


# line chart
import matplotlib.pyplot as plt
x=[1,5,6,7]
y=[4,6,7,8]
plt.plot(x,y)
plt.show()


# Customize chart                      matplotlib line parameters
import matplotlib.pyplot as plt
plt.figure(figsize=(4,3)) # figure size
x=[2,4,5,6]
y=[4,7,8,9]
plt.plot(x,y, color="m", marker='o', linestyle='dashed', linewidth=2,markersize=15)
plt.title("Nice chart")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()


# Advance line chart - multiple Lines and Legends
import matplotlib.pyplot as plt
x=[2,4,5,6]
y1=[4,7,8,9]
y2=[9,12,13,14]

plt.plot(x,y1,label='Sales 2024')
plt.plot(x,y2,label='Sales 2026')

plt.title("New Sales")
plt.xlabel("x axis")
plt.ylabel("y axis")

plt.legend()
plt.show()



# bar chart
import matplotlib.pyplot as plt
x=[2,4,5,6]
y=[4,7,8,9]

plt.bar(x,y)
plt.title("Bar chart")
plt.xlabel("x axis")
plt.ylabel("y axix")

plt.show()



# Histogram
import matplotlib.pyplot as plt
import random
data= [random.randint(1,10)for _ in range(100)]

plt.hist(data,bins=5)
plt.title("Histogram")
plt.show()



# Pie Chart
import matplotlib.pyplot as plt
catagories=["A","B","C","D","E"]
sales=[10,20,30,40,50]

plt.pie(sales,labels=catagories,autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()



# Scatter plot
import matplotlib.pyplot as plt
y1=[1,5,6,7]
y2=[4,6,7,8]
plt.scatter(y1,y2)
plt.title("Scatter plot")
plt.show()



# Subplot


import matplotlib.pyplot as plt
# bar chart
catagories=['Mon','Tues','Wed','Thurs','Sat']
sales=[10,20,30,40,50]
# scatter chart
y1=[2,4,5,6,5]
y2=[4,5,6,7,8]

plt.figure(figsize=(6,4))
# first plot...bar
plt.subplot(1,2,1) # row, coloumn, position
plt.bar(catagories,sales)
plt.title("Bar Chart")
plt.xlabel("X axis")
plt.ylabel("y axix")

# second plot...scatter
plt.subplot(1,2,2) # row, coloumn, position
plt.bar(y1,y2)
plt.title("Scatter Chart")
plt.xlabel("X axis")
plt.ylabel("y axix")

plt.show()



# pandas with Matplotlib
import pandas as pd

data={
    'Month':["Jan","Feb","March"],
    'Sales':[10,20,30]
}

df = pd.DataFrame(data)
df
plt.bar(df['Month'],df['Sales'])
plt.title("pandas with matplotlib")
plt.show()