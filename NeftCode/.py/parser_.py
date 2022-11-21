import pandas as pd
from datetime import datetime

def days_parse(dates):
    days = [int(day) if day.isdigit() else int(day[:-1]) for day in dates.split(',')]
    return days


years = []
for year in range(2016, 2023):
    cal = pd.read_csv(f'http://xmlcalendar.ru/data/ru/{year}/calendar.csv')
    to_drop = [
        'Год/Месяц',
        'Всего рабочих дней', 'Всего праздничных и выходных дней'
        , 'Количество рабочих часов при 40-часовой рабочей неделе'
        , 'Количество рабочих часов при 36-часовой рабочей неделе'
        , 'Количество рабочих часов при 24-часовой рабочей неделе'
    ]

    cal = cal.drop(columns=to_drop)
    cal = cal.transpose()
    cal.columns = ['dates']
    
    cal.dates = cal.dates.apply(days_parse)
    cal.index = range(1, 13)
    
    years.append(cal)
    
years_map = {
    2016: 0,
    2017: 1,
    2018: 2,
    2019: 3,
    2020: 4,
    2021: 5,
    2022: 6
}

def is_free_optim(dt):
    return dt.day in years[years_map[dt.year]].iloc[dt.month - 1].dates