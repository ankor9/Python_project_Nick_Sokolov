from homework_2_2_base import Wariors

class Archer(Wariors):
    def tell_function(self):
        print(f'I am an archer!')
        self.shoot = 0
    def archer_shoot(self):  # archer shoot
        self.shoot += 1
    def get_shoot(self): # print out shoot/s by archer
        return f'{self.name} shoots: {self.shoot}'

class Doctor(Wariors):
    def tell_function(self):
        print(f'I am a doctor!')
        self.doc_gave_health = 0
    def gave_health(self): # gave health by doctor
        self.doc_gave_health += 1
    def get_doc_gave_health(self): # print out health given by doctor
        return f'{self.name} gave health: {self.doc_gave_health}'

class Infantryman(Wariors):
    def tell_function(self):
        print(f'I am an infantryman!')
        self.strike = 0
    def infantryman_strike(self): # infantryman strike
        self.strike += 1
    def get_strike(self): # print out strike/s by infantryman
        return f'{self.name} strikes: {self.strike}'

archer_1 = Archer("First archer")
doctor_1 = Doctor("First doctor")
doctor_2 = Doctor("Second doctor")
infantryman_1 = Infantryman("First infantryman")

archer_1.say_name()
archer_1.tell_function()
archer_1.health_up()
archer_1.move_up()
archer_1.archer_shoot()
print(archer_1.get_health())
print(archer_1.get_move())
print(archer_1.get_shoot(), "\n")

doctor_1.say_name()
doctor_1.tell_function()
doctor_1.health_up()
doctor_1.health_up()
doctor_1.move_up()
doctor_1.move_up()
doctor_1.gave_health()
print(doctor_1.get_health())
print(doctor_1.get_move())
print(doctor_1.get_doc_gave_health(), "\n")

doctor_2.say_name()
doctor_2.tell_function()
doctor_2.health_up()
doctor_2.health_up()
doctor_2.move_up()
doctor_2.move_up()
doctor_2.gave_health()
print(doctor_2.get_health())
print(doctor_2.get_move())
print(doctor_2.get_doc_gave_health(), "\n")

infantryman_1.say_name()
infantryman_1.tell_function()
infantryman_1.health_up()
infantryman_1.health_up()
infantryman_1.health_up()
infantryman_1.move_up()
infantryman_1.move_up()
infantryman_1.move_up()
infantryman_1.infantryman_strike()
print(infantryman_1.get_health())
print(infantryman_1.get_move())
print(infantryman_1.get_strike(), "\n")