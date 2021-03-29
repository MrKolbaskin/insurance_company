from classes.company import Company
from classes.contract import AutoContract, LifeContract, HouseContract
from classes.insuredEventClass import InsuredEvent
from resources.gc import gc_contracts
import random
import copy
from pprint import pprint


STR2CLS = {
    'AutoContract': AutoContract,
    'LifeContract': LifeContract,
    'HouseContract': HouseContract
}

class Model:

    def __init__(
        self, 
        capital, 
        tax, 
        max_events, 
        contracts_info, 
        duration,
        random_count,
        m):

        self.duration = duration # продолжительность условий
        self.capital = capital # начальный капитал
        self.tax = tax # налоговый процент
        self.max_events = max_events # словарь из значений макс. числа страховых случаев для каждого вида страховки
        self.contracts_info = contracts_info # словарь из начальных условий каждого вида страховки
        self.__generate_demand()
        self.random_count = random_count
        #self.current_demand = {
        #    "AutoContract": 10,
        #    "LifeContract": 1,
        #    "HouseContract": 5
        #} # спрос для каждого вида страховки (будет генерироваться автоматически)
        #self.count_events = {
        #    "AutoContract": 3,
        #    "LifeContract": 3,
        #    "HouseContract": 3
        #}
        self.contracts = {key : [] for key in self.contracts_info}
        self.m = m
        self.logs = [["Модель создана"]]
        self.cur_month = 0
        """
        пример словаря contracts_info
        {
            "AutoContract": {
                "max_sum": int,
                "duration": int,
                "contribution_value": int
            }
        }
        """

    def __generate_rate(self):
        rate = round(random.uniform(0, 1), ndigits=2)
        if not rate:
            rate = 0.01
        return rate
    
    def __generate_demand(self):
        self.current_demand = {}
        self.current_demand = {
            "AutoContract": int(self.contracts_info['AutoContract']['max_sum'] / ((self.contracts_info['AutoContract']['contribution_value'] / 12) * self.contracts_info['AutoContract']['duration'])),
            "LifeContract": int(self.contracts_info['LifeContract']['max_sum'] / (self.contracts_info['LifeContract']['contribution_value'] * self.contracts_info['LifeContract']['duration'])),
            "HouseContract": int(self.contracts_info['HouseContract']['max_sum'] / (self.contracts_info['HouseContract']['contribution_value'] * self.contracts_info['HouseContract']['duration']))
        }

    def __generate_count_events(self, max_count):
        return random.randint(1, max_count)

    @staticmethod
    def __generate_contracts(contract, count, contracts_info):
        #print(contracts_info)
        return [contract(**contracts_info) for ind in range(count)]
    
    def __generate_insured_events(self, count):
        """
        Создание страховых случаев по кол-ву с случайным коэф. повреждения
        """
        return [InsuredEvent(rate) for rate in map(lambda x: self.__generate_rate(), range(count))]
    
    def __pay(self):
        payment_sum = 0
        for key in self.contracts:
            for contract in self.contracts[key]:
                payment_sum += contract.pay()
        #print('-----------------')
        #print("PAYMENT_SUM =", payment_sum)
        self.logs.append([f"Выплата по страховым случаям на сумму {payment_sum}"])
        #print("CAPITAL =", self.company.capital)
        #print('-----------------')
        
        self.company.capital -= payment_sum

    def __sort_insured_events(self, contracts, insured_events):
        shuffle_contracts = random.sample(contracts, k=len(contracts))
        for contract, event in zip(shuffle_contracts, insured_events):
            contract.insured_events.append(event)

    def __create_insured_events(self):
        for key in self.contracts:
            tmp_count_events = self.__generate_count_events(self.max_events[key])
            self.logs.append([f'Произошло страховых случаев по страховке {key} - {min(tmp_count_events, len(self.company.contracts[key]))}'])
            tmp_events = self.__generate_insured_events(tmp_count_events)
            self.__sort_insured_events(self.contracts[key], tmp_events)

    
    def __sell_contracts(self):
        for key in self.current_demand:
            tmp_count = int(self.current_demand[key] * random.random() * self.random_count[key])
            self.logs.append([f"Продажа {tmp_count} страховок вида {key}"])
            self.contracts[key] += self.__generate_contracts(
                STR2CLS[key],
                tmp_count,
                self.contracts_info[key]
                )

    def __str_contracts(self):
        res = {}
        for key in self.contracts:
            res[key] = [contract.json() for contract in self.contracts[key]]
        return res
    
    def get_contracts_info(self):
        return [
            [
                key,
                self.contracts_info[key]['duration'],
                self.contracts_info[key]['max_sum'],
                self.contracts_info[key]['contribution_value']
            ] for key in self.contracts_info]
    
    def get_contracts(self):
        return [[key] + contract.contract_info() for key in self.contracts_info for contract in self.contracts[key]]
    
    def json(self):
        if not hasattr(self, 'company'):
            capital = self.capital
        else:
            capital = self.company.capital
        return {
            "duration": self.duration,
            "capital": capital,
            "tax": self.tax,
            "max_events": self.max_events,
            "contracts_info": self.contracts_info,
            "current_demand": self.current_demand,
            "contracts": self.__str_contracts(),
            "m": self.m
        }

    def start(self): #начало моделирования
        """
        Создание базовых объектов и начало моделирования
        """
        self.company = Company(capital=self.capital, contracts=copy.deepcopy(self.contracts))

    
    def update(self, **kwargs): #Обновление
        self.duration = kwargs['duration']
        self.tax = kwargs['tax'] # налоговый процент
        self.max_events = kwargs['max_events'] # словарь из значений макс. числа страховых случаев для каждого вида страховки
        self.contracts_info = kwargs['contracts_info'] # словарь из начальных условий каждого вида страховки
        self.__generate_demand()
        self.logs.append(["Модель обновлена"])
    
    def simulation(self):
        while self.m and (self.company.capital >= 0):
            self.m -= 1
            self.cur_month += 1
            self.logs.append([f'---- МЕСЯЦ {self.cur_month} ----'])
            self.__sell_contracts()
            self.company.sell(self.contracts)
            contribution_sum = self.company.contribution()
            self.logs.append([f"Взнос на сумму {contribution_sum}"])
            self.contracts = gc_contracts(self.contracts)
            self.__create_insured_events()
            #pprint(self.json())
            self.__pay()
            self.company.pay_tax(percent=self.tax)
            if self.company.capital >= 0:
                self.logs.append([f'Выплата налога на сумму {self.company.capital * (self.tax / 100)}'])
            else:
                self.logs.append([f'Выплата налога на сумму 0'])

        if not self.m:
            return "Модель завершилась"
        if self.company.capital < 0:
            return "Компания банкрот"
        
        

    def tick(self): #обновление состояния через месяц
        if not hasattr(self, 'company'):
            return "Please call start"
        if not self.duration:
            return "Пожалуйста обновите условия"
        if not self.m:
            return "Модель завершилась"
        if self.company.capital < 0:
            return "Компания банкрот"
        
        self.duration -= 1
        self.m -= 1
        self.cur_month += 1
        self.logs.append([f'---- МЕСЯЦ {self.cur_month} ----'])
        self.__sell_contracts()
        self.company.sell(self.contracts)
        contribution_sum = self.company.contribution()
        self.logs.append([f"Взнос на сумму {contribution_sum}"])
        self.contracts = gc_contracts(self.contracts)
        self.__create_insured_events()
        #pprint(self.json())
        self.__pay()
        self.company.pay_tax(percent=self.tax)
        if self.company.capital >= 0:
            self.logs.append([f'Выплата налога на сумму {self.company.capital * (self.tax / 100)}'])
        else:
            self.logs.append([f'Выплата налога на сумму 0'])
