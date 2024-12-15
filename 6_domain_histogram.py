import pandas as pd
from collections import defaultdict
import matplotlib.pyplot as plt


def get_domain(email_str):
    # функция, которая извлекает домен из почтового адреса
    return email_str.split("@")[-1]


# читаем excel явно указывая названия столбцов чтоб не было unnamed столбца
data = pd.read_excel("./data/sample_table.xls", names=("region", "email", "username", "password", "ID"))

# Заполняем пустые столбцы с регионом предыдущим не-пустым значением
data = data.ffill()

# избавляемся от пустых email
data = data.dropna(subset="email")

# формируем столбец с доменом, в каждой строке он будет получен из email
data["domain"] = data["email"].apply(get_domain)

# считаем количество вхождений каждого уникального домена
domain_stats = data["domain"].value_counts().to_dict()

# рисуем гистограмму
plt.figure()
plt.hist(domain_stats.keys(), label=domain_stats.values())
plt.show()
