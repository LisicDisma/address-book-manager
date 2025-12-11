
from setuptools import setup, find_packages

setup(
    name='address-book-manager', 
    version='0.1.0', 
    packages=find_packages("."),
    scripts=["bin/address-book-cli"], 
    url='https://github.com/LisicDisma/address-book-manager', 
    license='Apache-2.0',
    author='Шабанова Ксения Алексеевна',
    author_email='kotukkc@gmail.com', 
    description='''Простой, полностью автономный пакет на Python для управления контактами и адресами, включающий классы Contact, Address и AddressBook.
    ## Address Book Manager (address-book-manager)
    
    Этот пакет предоставляет основные классы для работы с адресной книгой:
    * `Address`: хранение улицы, города и индекса.
    * `Contact`: хранение имени, телефона, email и объекта `Address`.
    * `AddressBook`: контейнер для контактов с методами для добавления, удаления, поиска, редактирования и экспорта в JSON.
    
    Пакет также включает исполняемый файл `address-book-cli` для запуска демонстрации из командной строки.
    ''', 
    include_package_data=True,
    install_requires=[],

)

