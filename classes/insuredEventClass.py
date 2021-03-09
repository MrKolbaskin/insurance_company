class InsuredEvent:
    def __init__(self, rate):
        self.rate = rate # коэффициент повреждения
    
    def json(self):
        return {
            'rate': self.rate
        }