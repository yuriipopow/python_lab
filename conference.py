class Conference:

    def __init__(self, name, number_of_participants, price, location, date_timestamp, maintainer):
        self.__name = name
        self.__number_of_participants = number_of_participants
        self.__price = price
        self.__location = location

        self.date_timestamp = date_timestamp
        self.maintainer = maintainer


    def get_name(self):
        return self.__name

    def get_number_of_participants(self):
        return self.__number_of_participants

    def get_price(self):
        return self.__price

    def get_location(self):
        return self.__location

    def __repr__(self):
        return f"Conference: {self.__name}, Number of Participants: {self.__number_of_participants}, Price: {self.__price}, Location: {self.__location}, Date: {self.date_timestamp}, Maintainer: {self.maintainer}"

    def __str__(self):
        return f"Conference: {self.__name}, Number of Participants: {self.__number_of_participants}, Price: {self.__price}, Location: {self.__location}, Date: {self.date_timestamp}, Maintainer: {self.maintainer}"

    def __del__(self):
        print(f"{self.__name} is deleted")
        del self
