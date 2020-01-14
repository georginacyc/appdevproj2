class Item:
    countID = 0
    def __init__(self,itemSerial,itemName,itemCategory,itemGender,itemCost,itemPrice):
        self.__class__.countID +=1
        self.__itemSerial = itemSerial
        self.__itemName = itemName
        self.__itemCategory = itemCategory
        self.__itemGender = itemGender
        self.__itemCost = itemCost
        self.__itemPrice = itemPrice
        self.__itemQuantity = 0

    #get attributes

    def get_itemSerial(self):
        return self.__itemSerial
    def get_itemName(self):
        return self.__itemName
    def get_itemCategory(self):
        return self.__itemCategory
    def get_itemGender(self):
        return self.__itemGender
    def get_itemCost(self):
        return self.__itemCategory
    def get_itemPrice(self):
        return self.__itemPrice
    def get_itemQuantity(self):
        return self.__itemQuantity

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
        self.__itemQuantity = itemQuantity
