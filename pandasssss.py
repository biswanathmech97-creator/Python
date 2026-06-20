# Starting
import pandas as pd
data = {
    'Product': ['Laptop', 'Mouse', 'Monitor'],
    'Price': [55000, 1200, 15000]
}
df = pd.DataFrame(data)
print(df)

# Series............ labeled array
import pandas as pd
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s)

# data frame..
import pandas as pd
data={
    'Student': ['Harry','Faahh','Jupiter'],
    'Marks' :  [45,78,56]
}
df=pd.DataFrame(data)
print(df)
