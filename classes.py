from collections import UserDict

class Field:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError
        self.value = value
        
    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        return True

class Name(Field):
    pass

class Phone(Field):
    def is_valid(self, value):
        return len(value) == 10 and value.isdigit()

        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def find_phone(self, number: str) -> Phone:
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None

    def add_phone(self, number):
        phone = Phone(number)
        self.phones.append(phone)
        return phone

    def remove_phone(self, number):
        phone = self.find_phone(number)
        if not phone:
            raise ValueError
        self.phones.remove(phone)

    def edit_phone(self, oldnumber, newnumber):
        if self.find_phone(oldnumber):
            self.add_phone(newnumber)
            self.remove_phone(oldnumber)
        else:
            raise ValueError


    def __str__(self):
        return f"Contact name: {str(self.name)}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data[record.name.value] = record
    
    def find(self, name: str) -> Record:
        return self.data.get(name, None)
    
    def delete(self, name: str) -> Record:
        return self.data.pop(name, None)
    
    def __str__(self):
        result = ""
        for record in self.data.values():
            result += f'{str(record)}\n'
        return result
