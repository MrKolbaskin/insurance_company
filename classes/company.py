from resources.gc import gc_contracts

class Company:
    def __init__(self, capital, contracts):
        self.capital = capital
        self.contracts = contracts

    def contribution(self):#внесение взносов по существующим страховкам
        for key in self.contracts:
            for contract in self.contracts[key]:
                self.capital += contract.contribution()
        self.contracts = gc_contracts(self.contracts)

    def payment(self):#выплата за страховые случаи
        self.contracts = gc_contracts(self.contracts)
        for key in self.contracts:
            for contract in self.contracts:
                for insured_event in contract.insured_events:
                    self.capital -= insured_event.rate * contract.max_sum

    def sell(self, new_contracts):#продажа страховок
        # counts - словарь из кол-ва проданных страховок каждого вида
        self.contracts = gc_contracts(self.contracts)
        for key in new_contracts:
            self.contracts[key] += new_contracts[key]

    def pay_tax(self, percent):#выплата налога
        self.capital *= (100 - percent) / 100