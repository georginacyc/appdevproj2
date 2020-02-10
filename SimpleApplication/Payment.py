class Payment:
    def __init__(self, name, cardno, date, cvv):
        self.__name = name
        self.__cardno = cardno
        self.__date = date
        self.__cvv = cvv

    def set_name(self, name):
        self.__name = name
    def set_cardno(self, cardno):
        self.__cardno = cardno
    def set_date(self, date):
        self.__date = date
    def set_cvv(self, cvv):
        self.__cvv = cvv


    def get_name(self):
        return self.__name
    def get_cardno(self):
        return self.__cardno
    def get_date(self):
        return self.__date
    def get_cvv(self):
        return self.__cvv
