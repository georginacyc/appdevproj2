class Shipping:
    countID = 0
    def __init__(self, fname, lname, email, hp, address, address2, postal):
        self.__class__.countID +=1
        self.__shippingCount = self.__class__.countID
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__hp = hp
        self.__address = address
        self.__address2 = address2
        self.__postal = postal


    def get_contactCount(self):
        return self.__shippingCount
    def set_fname(self, fname):
        self.__fname = fname
    def set_lname(self, lname):
        self.__lname = lname
    def set_email(self, email):
        self.__email = email
    def set_hp(self, hp):
        self.__hp = hp
    def set_address(self, address):
        self.__address = address
    def set_address2(self, address2):
        self.__address2 = address2
    def set_postal(self, postal):
        self.__postal = postal

    def get_fname(self):
        return self.__fname
    def get_lname(self):
        return self.__lname
    def get_email(self):
        return self.__email
    def get_hp(self):
        return self.__hp
    def get_address(self):
        return self.__address
    def get_address2(self):
        return self.__address2
    def get_postal(self):
        return self.__postal


