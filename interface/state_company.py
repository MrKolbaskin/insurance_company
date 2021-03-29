def state_company(company, cur_month, current_demand):
    return f"""Текущий месяц: {cur_month}
Страховая компания
    Капитал в у.е. : {company.capital}
    Кол-во договоров страхование автомобиля: {len(company.contracts['AutoContract'])}
    Кол-во договоров страхование жизни: {len(company.contracts['LifeContract'])}
    Кол-во договоров страхование имущества: {len(company.contracts['HouseContract'])}
"""

def current_demands(current_demand):
    return f"""


Коэффициент текущего спроса: {current_demand['AutoContract']}
Коэффициент текущего спроса: {current_demand['LifeContract']}
Коэффициент текущего спроса: {current_demand['HouseContract']}
"""