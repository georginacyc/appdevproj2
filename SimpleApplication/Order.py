class Order:
    orderN = 1000
    countID = 0

    def __init__(self,orderDate,shipmentDate,shipmentStatus,receivedDate):
        self.__class__.countID +=1
        self.__orderCount = self.__class__.countID
        self.__class__.orderN += 1
        self.__orderNumber = self.__class__.orderN
        self.__orderDate = orderDate
        self.__shipmentDate = shipmentDate
        self.__shipmentStatus = shipmentStatus
        self.__receivedDate = receivedDate


#getter
    def get_orderCount(self):
        return self.__orderCount
    def get_orderNumber(self):
        return self.__orderNumber
    def get_orderDate(self):
        return self.__orderDate

    def get_shipmentDate(self):
        return self.__shipmentDate
    def get_shipmentStatus(self):
        return self.__shipmentStatus
    def get_receivedDate(self):
        return self.__receivedDate


#setter

    def set_orderDate(self,orderDate):
        self.__orderDate = orderDate

    def set_shipmentDate(self,shipmentDate):
        self.__shipmentDate = shipmentDate
    def set_shipmentStatus(self,shipmentStatus):
        self.__shipmentStatus = shipmentStatus
    def set_receivedDate(self,receivedDate):
        self.__receivedDate = receivedDate
