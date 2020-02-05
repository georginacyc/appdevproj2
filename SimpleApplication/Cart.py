from wtforms import Form

class Cart:
    countID = 0
    def __init__(self,cartItem, cartQuantity, cartSubtotal, cartItemSerial):
        self.__class__.countID += 1
        self.__cartCount = self.__class__.countID
        self.__cartItem = cartItem
        self.__cartQuantity = cartQuantity
        self.__cartSubtotal = cartSubtotal
        self.__cartItemSerial = cartItemSerial

    def get_cartCount(self):
        return self.__cartCount
    def get_cartItem(self):
        return self.__cartItem
    def get_cartQuantity(self):
        return self.__cartQuantity
    def get_cartSubtotal(self):
        return self.__cartSubtotal
    def get_cartItemSerial(self):
        return self.__cartItemSerial

    def set_cartItem(self,cartItem):
        self.__cartItem = cartItem
    def set_cartQuantity(self,cartQuantity):
        self.__cartQuantity = cartQuantity
    def set_cartSubtotal(self,cartSubtotal):
          self.__cartSubtotal = cartSubtotal
    def set_cartItemSerial(self,cartItemSerial):
          self.__cartItemSerial = cartItemSerial


    def set_updatePrice(self):
        pass

class addtocartForm(Form):
    pass
