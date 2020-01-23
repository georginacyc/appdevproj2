class Announcement:
    def __init__(self, date, title, description):
        self.__date = date
        self.__title = title
        self.__description = ""

    def set_date(self, date):
        self.__date = date
    def set_title(self, title):
        self.__title = title
    def set_description(self, description):
        self.__description = description

    def get_date(self):
        return self.__date
    def get_title(self):
        return self.__title
    def get_description(self):
        return self.__description
