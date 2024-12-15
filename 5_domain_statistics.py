import pandas as pd
from collections import defaultdict


def get_domain(email_str):
    # функция, которая извлекает домен из почтового адреса
    return email_str.split("@")[-1]


def print_results(data, group_column, count_column):
    result_series = data.groupby(group_column)[count_column].value_counts().groupby(level=0).head(1)
    result = result_series.index.tolist()
    for region, domain in result:
        print(f"Самый популярный домен в регионе {region} - это {domain}")


# читаем excel явно указывая названия столбцов чтоб не было unnamed столбца
data = pd.read_excel("./data/sample_table.xls", names=("region", "email", "username", "password", "ID"))

# Заполняем пустые столбцы с регионом предыдущим не-пустым значением
data = data.ffill()

# избавляемся от пустых email
data = data.dropna(subset="email")

# формируем столбец с доменом, в каждой строке он будет получен из email
data["domain"] = data["email"].apply(get_domain)

print_results(data, "region", "domain")
