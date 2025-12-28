"""
Инициализация пакета Address Book Manager.
Предоставляет быстрый доступ к основным классам: Contact, Address, AddressBook.
"""

from .address import Address
from .contact import Contact
from .address_book import AddressBook

__all__ = ["Address", "Contact", "AddressBook"]
