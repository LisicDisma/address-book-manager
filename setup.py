
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
    description='Простой, полностью автономный пакет на Python для управления контактами и адресами, включающий классы Contact, Address и AddressBook.', 
    include_package_data=True,
    install_requires=[],

)
