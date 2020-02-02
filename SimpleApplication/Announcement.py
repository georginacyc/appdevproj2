class Announcement:
    count = 0

    def __init__(self, date, title):
        self.__class__.count += 1
        self.set_count(self.__class__.count)
        self.__count = self.get_count()
        self.__date = date
        self.__title = title
        self.__description = ""

    def set_count(self, count):
        self.__count = self.__class__.count
    def set_date(self, date):
        self.__date = date
    def set_title(self, title):
        self.__title = title
    def set_description(self, description):
        self.__description = description

    def get_count(self):
        return self.__count
    def get_date(self):
        return self.__date
    def get_title(self):
        return self.__title
    def get_description(self):
        return self.__description
