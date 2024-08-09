import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from scipy import stats

# установка стиля
sns.set(style ="whitegrid")

# загрузка данных
file_path = "googplaystore.csv"
df = pd.read_csv('D:\GB\PARS\Sem_8\googleplaystore.csv')

# вывод датасета
print('первые строки:')
print(df.head())

# обработка отсутств значений
numeric_cols = df.select_dtypes(include=[np.number])
df[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mean())
print(df[numeric_cols.columns])
print(df.describe())

categorical_cols = df.select_dtypes(include=['object']) # выбор категориальных колонок
df[categorical_cols.columns] = categorical_cols.fillna(categorical_cols.mode().iloc[0])
print(df[categorical_cols.columns])
df.drop_duplicates(inplace=True)

plt.figure(figsize=(10, 6))
sns.histplot(df['Rating'], kde=True, color='skyblue')
plt.title('Рейтинг приложений')
plt.show()

plt.figure(figsize=(12, 8))
sns.countplot(y = 'Category', data= df, order=df['Category'].value_counts().index,palette='viridis')
plt.title('across category')
plt.show()

# распределение платных и бесплатных приложений

plt.figure(figsize=(7, 5))
sns.countplot(x="Type", data=df)
plt.title("Free vs Paid")
plt.show()

# обнаружение и обработка выбросов
z_scores = np.abs(stats.zscore(df.select_dtypes(include=np.number))) # z оценки для числовых переменных
df = df[(z_scores <3).all(axis=1)] # удаление строк с выбросами

# стандартизицая данных (числовых переменных)
df_standardized = df.copy() # копия датафрейм
df_standardized[numeric_cols.columns] = (df_standardized[numeric_cols.columns] \
                                         - df_standardized[numeric_cols.columns].mean()) / df_standardized[numeric_cols.columns].std()

# one hot encoding
# df = pd.get_dummies(df, columns=['Category'], prefix='Category_type', drop_first=True)

# создание сводной таблицы
# pivot_table = df.pivot_table(index="Category", columns='ContentRating_Teen', values='Rating', aggfunc='mean')
# print(pivot_table)

# преобразование категорийной переменной в числовую
label_encoder = LabelEncoder()
df['Type_Encoded'] = label_encoder.fit_transform(df['Type'])

# сохранение
output_file_path = 'clear_gapps.csv'
df.to_csv('labelappout.csv', index=False)



