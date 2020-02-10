class Sale:
    def __init__(self, saleDate, saleAmt):
        self.__saleDate = saleDate
        self.__saleAmt = saleAmt

    def set_saleDate(self, saleDate):
        self.__saleDate = saleDate
    def set_saleAmt(self, saleAmt):
        self.__saleAmt = saleAmt



    def get_saleDate(self):
        return self.__saleDate
    def get_saleAmt(self):
        return self.__saleAmt
