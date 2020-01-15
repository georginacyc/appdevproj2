class Staff:
    count = 000000

    def __init__(self, fname, lname, gender, hp, dob, password, address):
        self.__fname = fname
        self.__lname = lname
        self.__gender = gender
        self.__hp = hp
        self.__dob = dob
        self.__password = password
        self.__address = address
        self.__eID = self.set_eID(self.__class__.count)
        self.__email = self.set_email(self.get_eID())

    def set_fname(self, fname):
        self.__fname = fname
    def set_lname(self, lname):
        self.__lname = lname
    def set_gender(self, gender):
        self.__gender = gender
    def set_hp(self, hp):
        self.__hp = hp
    def set_dob(self, dob):
        self.__dob = dob
    def set_password(self, password):
        self.__password = password
    def set_address(self, address):
        self.__address = address
    def set_eID(self, count):
        count += 1
        self.__eID = count
    def set_email(self, eID):
        self.__email = str(eID) + "@monoqlo.com"

    def get_fname(self):
        return self.__fname
    def get_lname(self):
        return self.__lname
    def get_gender(self):
        return self.__gender
    def get_hp(self):
        return self.__hp
    def get_dob(self):
        return self.__dob
    def get_password(self):
        return self.__password
    def get_address(self):
        return self.__address
    def get_eID(self):
        return self.__eID
    def get_email(self):
        return self.__email