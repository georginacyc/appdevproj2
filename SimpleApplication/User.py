class User:
    countID=0
    def __init__(self,firstName,lastName,DOB,gender,email,pw,confirmpw):
        User.countID+=1
        self.__userID=User.countID
        self.__firstName=firstName
        self.__lastName=lastName
        self.__DOB=DOB
        self.__gender=gender
        self.__email=email
        self.__pw=pw
        self.__confirmpw=confirmpw

    def get_firstName(self):
        return self.__firstName
    def get_lastName(self):
        return self.__lastName
    def get_gender(self):
        return self.__gender
    def get_DOB(self):
        return self.__DOB
    def get_email(self):
        return self.__email
    def get_pw(self):
        return self.__pw
    def set_userID(self,userID):
        self.__userID=userID
    def set_firstName(self,firstName):
        self.__firstName=firstName
    def set_lastName(self,lastName):
        self.__lastName=lastName
    def set_gender(self,gender):
        self.__gender=gender
    def set_DOB(self,DOB):
        self.__DOB=DOB
    def set_email(self,email):
        self.__email=email
    def set_pw(self,pw):
        self.__pw=pw

