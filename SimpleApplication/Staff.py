class Staff:
    count = 0

    def __init__(self, fname, lname, gender, hp, dob, password, address, type):
        self.__class__.count += 1
        self.__fname = fname
        self.__lname = lname
        self.__gender = gender
        self.__hp = hp
        self.__dob = dob
        self.__password = password
        self.__address = address
        self.set_eID(self.__class__.count)
        self.__eID = self.get_eID()
        self.set_email(self.get_eID())
        self.__email = self.get_email()
        self.__type = type

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
        eID = str(count).zfill(6)
        self.__eID = eID
    def set_email(self, eID):
        self.__email = str(eID) + "@monoqlo.com"
    def set_type(self, type):
        self.__type = type

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
    def get_type(self):
        return self.__type
