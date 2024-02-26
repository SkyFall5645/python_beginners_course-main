import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one hot вид
one_hot_data = pd.get_dummies(data['whoAmI'], drop_first=True)

# Объединение с исходным DataFrame
data = pd.concat([data, one_hot_data], axis=1)

# Удаление исходного столбца
data = data.drop('whoAmI', axis=1)

print(data.head())












