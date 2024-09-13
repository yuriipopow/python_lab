class Conference:

    def __init__(self, name: str, number_of_participants: int, price: int, location: str, date_timestamp: int, maintainer: str):
        self.__name: str = name
        self.__number_of_participants: int = number_of_participants
        self.__price: int = price
        self.__location: str = location

        self.date_timestamp: int = date_timestamp
        self.maintainer: str = maintainer


    def get_name(self) -> str:
        return self.__name

    def get_number_of_participants(self) -> int:
        return self.__number_of_participants

    def get_price(self) -> int:
        return self.__price

    def get_location(self) -> str:
        return self.__location

    def __repr__(self) -> str:
        return f"Conference: {self.__name}, Number of Participants: {self.__number_of_participants}, Price: {self.__price}, Location: {self.__location}, Date: {self.date_timestamp}, Maintainer: {self.maintainer}"

    def __str__(self) -> str:
        return f"Conference: {self.__name}, Number of Participants: {self.__number_of_participants}, Price: {self.__price}, Location: {self.__location}, Date: {self.date_timestamp}, Maintainer: {self.maintainer}"

    def __del__(self) -> None:
        print(f"{self.__name} is deleted")
        del self
