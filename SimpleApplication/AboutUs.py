class AboutUs:
    def __init__(self, aboutUsName, aboutUsRole):
        self.__aboutUsName = aboutUsName
        self.__aboutUsRole = aboutUsRole

    def set_aboutUsName(self, aboutUsName):
        self.__aboutUsName = aboutUsName
    def set_aboutUsRole(self, aboutUsRole):
        self.__aboutUsRole = aboutUsRole



    def get_aboutUsName(self):
        return self.__aboutUsName
    def get_aboutUsRole(self):
        return self.__aboutUsRole
