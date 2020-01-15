class Invoice:
    countID = 0
    invoiceN = 1000
    def __init__(self,invoiceDate,shipmentDate,shipmentStatus,receivedDate):
        self.__class__.countID +=1
        self.__invoiceCount = self.__class__.countID
        self.__class__.invoiceN +=1
        self.__invoiceNumber = self.__class__.invoiceN
        self.__invoiceDate = invoiceDate
        self.__shipmentDate = shipmentDate
        self.__shipmentStatus = shipmentStatus
        self.__receivedDate = receivedDate


#getter
    def get_invoiceCount(self):
        return self.__invoiceCount
    def get_invoiceNumber(self):
        return self.__invoiceNumber
    def get_invoiceDate(self):
        return self.__invoiceDate

    def get_shipmentDate(self):
        return self.__shipmentDate
    def get_shipmentStatus(self):
        return self.__shipmentStatus
    def get_receivedDate(self):
        return self.__receivedDate

#setter

    def set_invoiceDate(self,invoiceDate):
        self.__invoiceDate = invoiceDate

    def set_shipmentDate(self,shipmentDate):
        self.__shipmentDate = shipmentDate
    def set_shipmentStatus(self,shipmentStatus):
        self.__shipmentStatus = shipmentStatus
    def set_receivedDate(self,receivedDate):
        self.__receivedDate = receivedDate
