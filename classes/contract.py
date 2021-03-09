class Contract:
    def __init__(self, duration, max_sum, contribution_value):
        self.duration = duration #Продолжительность контракта
        self.max_sum = max_sum #Максимальная сумма выплаты
        self.contribution_value = contribution_value
        self.insured_events = []
    
    def pay(self):
        payment_sum = 0
        for event in self.insured_events:
            payment_sum += event.rate * self.max_sum
        self.insured_events = []
        return payment_sum
    
    def json(self):
        return {
            "duration": self.duration,
            "max_sum": self.max_sum,
            "contribution_value": self.contribution_value,
            'insured_events': [event.json() for event in self.insured_events]
        }

class AutoContract(Contract):
    def contribution(self):#внесение взноса
        if self.duration % 12 == 0:
            res =  self.contribution_value
        else:
            res = 0
        
        self.duration -= 1
        return res

class HouseContract(Contract):
    def contribution(self):#внесение взноса
        self.duration -= 1
        return self.contribution_value

class LifeContract(Contract):
    def contribution(self):#внесение взноса
        self.duration -= 1
        return self.contribution_value