# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# Статья про one hot вид https://colab.research.google.com/drive/1qKamnDiRmpRZkpiqWPkunBdAhmzhMcGz?usp=sharing

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
pd.get_dummies(data['whoAmI'])
# print(data.head()) 
# print(pd.get_dummies(data['whoAmI']))

#Ссылка с решением данной задачи в GoogleCollab: https://colab.research.google.com/drive/1AouFMJmHBEEHca5ZCCy3RiMCPEPLKTls?usp=drive_link