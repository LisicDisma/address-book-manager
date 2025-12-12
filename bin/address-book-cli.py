
from address_book_manager import AddressBook, Contact, Address

def main():
    """
    Главная функция для демонстрации работы адресной книги.
    """
    book = AddressBook()
    
    print("=== Демонстрация Address Book Manager ===")

    # 1. Добавление контактов
    print("\n--- Добавление контактов ---")
    addr1 = Address("Главная ул., 10", "Москва", "123456")
    contact1 = Contact("Иван Иванов", "79001234567", "ivan.i@example.com", addr1)
    book.add_contact(contact1)

    addr2 = Address("Ул. Пушкина, 5", "Санкт-Петербург", "987654")
    contact2 = Contact("Петр Петров", "79119876543", "p.petrov@test.ru", addr2)
    book.add_contact(contact2)

    # 2. Поиск
    print("\n--- Поиск контакта по имени 'Иван' ---")
    results = book.find_contact("Иван")
    for r in results:
        print(f"Найдено: {r}")

    # 3. Редактирование
    print("\n--- Редактирование контакта 'Петр Петров' ---")
    book.edit_contact("Петр Петров", {
        'phone': '79110001122', 
        'email': 'new.petrov@test.ru',
        'address': {'city': 'Новый Город'}
    })
    
    print("\n--- Проверка отредактированного контакта ---")
    print(book.find_contact("79110001122")[0])

    # 4. Удаление
    print("\n--- Удаление контакта 'Иван Иванов' ---")
    book.delete_contact("Иван Иванов")

    # 5. Экспорт
    print("\n--- Экспорт оставшихся контактов ---")
    book.export_to_json("my_contacts.json")
    
    print("\n=== Демонстрация завершена ===")

