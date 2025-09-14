import pandas as pd
#put your code here
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# Смотрим первые 7 строк
df.head(7)
# Смотрим информацию о данных
df.info()
# Смотрим статистику
df.describe()
# Заполняем пропуски в возрасте медианой
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)
df.info()
# Функция для возрастных групп
def get_age_group(age):
    if age < 18:
        return "Ребенок"
    elif 18 <= age <= 65:
        return "Взрослый"
    else:
        return "Пожилой"
# Создаем новый столбец AgeGroup и применяем функцию к столбцу Age
df['AgeGroup'] = df['Age'].apply(get_age_group)

# Проверяем первые 5 строк
df[['Age', 'AgeGroup']].head()

# Процент выживших мужчин и женщин
df.groupby('Sex')['Survived'].mean() * 100

# Процент выживших по классам
df.groupby('Pclass')['Survived'].mean() * 100

# Сводная таблица по полу и классу
df.pivot_table(values='Survived', index='Pclass', columns='Sex', aggfunc='mean') * 100

# Несовершеннолетние из 3 класса, которые выжили
minors_3rd_class = df[(df['Age'] < 18) & (df['Pclass'] == 3) & (df['Survived'] == 1)]
minors_3rd_class.sort_values('Age', ascending=False)[['Name', 'Age', 'Pclass', 'Survived']]
# ЧАСТЬ 4: ВЫВОДЫ

# 1. Какой фактор — пол или класс каюты — оказывал большее влияние на выживаемость?
#    Пол оказывал большее влияние на выживаемость, чем класс каюты.
#    Цифры из анализа:
#    - Женщины: 74.2% выживших
#    - Мужчины: 18.9% выживших
#    - 1 класс: 62.9% выживших  
#    - 2 класс: 47.3% выживших
#    - 3 класс: 24.2% выживших
#    Разница между полами: 55.3%, между классами: 38.7%

# 2. Подтверждает ли анализ правило "женщины и дети в первую очередь"?
#    Да, анализ подтверждает это правило:
#    - Женщины имели значительно более высокие шансы (74.2% vs 18.9%)
#    - Дети также имели приоритет при спасении
#    Данные по возрастным группам и полу показывают, что женщины и дети 
#    действительно спасались в первую очередь

# Самый пожилой мужчина, который не выжил
oldest_dead_man = df[(df['Sex'] == 'male') & (df['Survived'] == 0)].sort_values('Age', ascending=False).head(1)
oldest_dead_man[['Name', 'Age', 'Sex', 'Survived']]
