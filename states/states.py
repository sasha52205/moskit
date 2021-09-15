from aiogram.dispatcher.filters.state import StatesGroup, State




class Phone(StatesGroup):
    phone = State()
    any = State()
    ru = State()
    uz = State()
    usa = State()
    
    
class Account(StatesGroup):
    Q1 = State()
    Q2 = State()

    
class Email(StatesGroup):
    email = State()
    yandex = State()
    gmail = State()



    
class Fio(StatesGroup):
    Q1 = State()
    Q2 = State()
    
    
    
    
class Adress(StatesGroup):
    Q1 = State()
    Q2 = State()
    
    
class Nik(StatesGroup):
    Q1 = State()
    Q2 = State()

    
class Transport(StatesGroup):
    Q1 = State()
    Q2 = State()


    
class Doc(StatesGroup):
    Q1 = State()
    Q2 = State()


    
class Domen(StatesGroup):
    domen = State()
    any = State()
    Q2 = State()
    
class Cash(StatesGroup):
    Q1 = State()
    Q2 = State()





