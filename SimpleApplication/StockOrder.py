class StockOrder:
    stockorderN = 1000
    countID = 0

    def __init__(self, stockorderDate, shipmentDate, shipmentStatus, receivedDate, stockItemSerial, stockorderQuantity):
        self.__class__.countID += 1
        self.__stockorderCount = self.__class__.countID
        self.__class__.stockorderN += 1
        self.__stockorderNumber = self.__class__.stockorderN
        self.__stockorderDate = stockorderDate
        self.__shipmentDate = shipmentDate
        self.__shipmentStatus = shipmentStatus
        self.__receivedDate = receivedDate
        self.__stockItemSerial = stockItemSerial
        self.__stockorderQuantity = stockorderQuantity

    # getter
    def get_stockorderCount(self):
        return self.__stockorderCount

    def get_stockorderNumber(self):
        return self.__stockorderNumber

    def get_stockorderDate(self):
        return self.__stockorderDate

    def get_shipmentDate(self):
        return self.__shipmentDate

    def get_shipmentStatus(self):
        return self.__shipmentStatus

    def get_receivedDate(self):
        return self.__receivedDate

    def get_stockItemSerial(self):
        return self.__stockItemSerial

    def get_stockorderQuantity(self):
        return self.__stockorderQuantity
    # setter

    def set_stockorderDate(self, stockorderDate):
        self.__stockorderDate = stockorderDate

    def set_shipmentDate(self, shipmentDate):
        self.__shipmentDate = shipmentDate

    def set_shipmentStatus(self, shipmentStatus):
        self.__shipmentStatus = shipmentStatus

    def set_receivedDate(self, receivedDate):
        self.__receivedDate = receivedDate

    def set_stockItemSerial(self,stockItemSerial):
        self.__stockItemSerial = stockItemSerial

    def set_stockorderQuantity(self,stockorderQuantity):
        self.__stockorderQuantity = stockorderQuantity
