class Contact:
    countID = 0
    def __init__(self, fname, lname, email, text):
        self.__class__.countID +=1
        self.__contactCount = self.__class__.countID
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__text = text


    def get_contactCount(self):
        return self.__contactCount
    def set_fname(self, fname):
        self.__fname = fname
    def set_lname(self, lname):
        self.__lname = lname
    def set_email(self, email):
        self.__email = email
    def set_text(self, text):
        self.__text = text


    def get_fname(self):
        return self.__fname
    def get_lname(self):
        return self.__lname
    def get_email(self):
        return self.__email
    def get_text(self):
        return self.__text

