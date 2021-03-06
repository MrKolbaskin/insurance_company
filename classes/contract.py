class Contract:
    def __init__(self, duration, max_sum, contribution_value):
        self.duration = duration #Продолжительность контракта
        self.max_sum = max_sum #Максимальная сумма выплаты
        self.contribution_value = contribution_value
        self.insured_events = []
        self.log_events = []
    
    def pay(self):
        payment_sum = 0
        for event in self.insured_events:
            payment_sum += event.rate * self.max_sum
        self.log_events = self.insured_events
        self.insured_events = []
        return payment_sum
    
    def json(self):
        return {
            "duration": self.duration,
            "max_sum": self.max_sum,
            "contribution_value": self.contribution_value,
            'insured_events': [event.json() for event in self.insured_events]
        }
    
    def contract_info(self):
        return [self.duration, self.max_sum, self.contribution_value, '; '.join([str(event.rate) for event in self.log_events])]

class AutoContract(Contract):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.first_contribution = True

    def contribution(self):#внесение взноса
        if self.first_contribution or self.duration % 12 == 0:
            self.first_contribution = False
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