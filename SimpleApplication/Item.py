class Item:
    countID = 0
    def __init__(self,itemSerial,itemName,itemCategory,itemGender,itemCost,itemPrice,itemDescription):
        self.__class__.countID +=1
        self.__itemCount = self.__class__.countID
        self.__itemName = itemName
        self.__itemSerial = itemSerial
        self.__itemCategory = itemCategory
        self.__itemGender = itemGender
        self.__itemCost = itemCost
        self.__itemPrice = itemPrice
        self.__itemQuantity = 0
        self.__itemDescription = itemDescription
        self.__itemCartQuantity = 1
        self.set_itemStockStatus()
 
    #get attributes
    def get_itemCount(self):
        return self.__itemCount
    def get_itemName(self):
        return self.__itemName
    def get_itemSerial(self):
        return self.__itemSerial
    def get_itemCategory(self):
        return self.__itemCategory
    def get_itemGender(self):
        return self.__itemGender
    def get_itemCost(self):
        return self.__itemCost
    def get_itemPrice(self):
        return self.__itemPrice
    def get_itemQuantity(self):
        return self.__itemQuantity
    def get_itemStockStatus(self):
        return self.__itemStockStatus
    def get_itemDescription(self):
        return self.__itemDescription
    def get_itemCartQuantity(self):
        return self.__itemCartQuantity

    #set attributes

    def set_itemSerial(self,itemSerial):
        self.__itemSerial=itemSerial
    def set_itemName(self,itemName):
        self.__itemName = itemName
    def set_itemCategory(self,itemCategory):
        self.__itemCategory = itemCategory
    def set_itemGender(self,itemGender):
        self.__itemGender = itemGender
    def set_itemCost(self,itemCost):
        self.__itemCost = itemCost
    def set_itemPrice(self,itemPrice):
        self.__itemPrice = itemPrice
    def set_itemQuantity(self,itemQuantity):
        self.__itemQuantity += itemQuantity
    def set_itemDescription(self,itemDescription):
        self.__itemDescription = itemDescription
    # def set_itemCartQuantity(self,itemCartQuantity):
    #     self.__itemCartQuantity = itemCartQuantity

    def set_itemStockStatus(self):
        quantity = self.__itemQuantity
        if quantity>30:
            self.__itemStockStatus = "In Stock"
        elif 30 >= quantity > 0:
            self.__itemStockStatus = "Low on Stock"
        elif quantity == 0:
            self.__itemStockStatus = "Out of Stock"
