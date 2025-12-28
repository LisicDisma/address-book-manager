"""
Модуль Contact для представления контактной информации, 
включая наследование для адреса.
"""

from .address import Address

class Contact:
    """
    Класс для хранения контактной информации человека.
    Инкапсулирует данные: имя, телефон, email, а также объект Address.
    """
    
    def __init__(self, name: str, phone: str, email: str, address: Address):
        """
        Базовый конструктор класса.
        
        :param name: Имя контакта.
        :param phone: Телефона крнтакта.
        :param email: email контакта.
        :param address: Адресс контакта
        """
        if not isinstance(address, Address):
            raise TypeError("Аргумент 'address' должен быть экземпляром класса Address.")
            
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address 

    def get_name(self) -> str:
        """Возвращает имя контакта."""
        return self.__name

    def get_phone(self) -> str:
        """Возвращает телефон контакта."""
        return self.__phone

    def get_email(self) -> str:
        """Возвращает email контакта."""
        return self.__email

    def get_address(self) -> Address:
        """Возвращает объект Address контакта."""
        return self.__address

 
    def set_name(self, name: str):
        """Устанавливает новое имя контакта.
        :param name: Новое имя
        """
        self.__name = name

    def set_phone(self, phone: str):
        """Устанавливает новый телефон контакта.
        :param phone: Номер телефона
        """
        self.__phone = phone

    def set_email(self, email: str):
        """Устанавливает новый email контакта.
        :param email: Электронная почта
        """
        self.__email = email

    def __str__(self):
        """Возвращает строковое представление объекта Contact."""
        return (f"Имя: {self.__name}, Телефон: {self.__phone}, Email: {self.__email}, "

                f"Адрес: {self.__address.get_full_address()}")
