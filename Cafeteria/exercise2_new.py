# Cafeteria project : Create an live menu and payment system (a.k.a console program) :

# First the program should ask if table was reserved/ not (Providing your full name) .
# And then if not would assign you a table (there is a specific number single, double or family tables) .
# After table is assigned to you, system should show how many free tables are and how which are
# reserved/occupied. The system must be able to show name/surname of the person of the reserved
#  table (CLI option : enter reserved table number ; OUTCOME: Name/Surname/Time Reserved)
#
# After assigning table, system should show different menu options for breakfast, lunch , dinner ,
# drinks (alcohol. alcohol free), to choose from. Special menu for vegetarian and vegan must be
# included too in the special menu. All menu items should have weight, preparation time in minutes,
# calories, and price.
# I have to have an option to change the order before the payment section. Thus I can delete,
# add more, update amount of the same order.
# I should be able to choose whatever I want from all menus in one ordering. After I finish,
# I need to see what I chosen, the full payable amount and approx waiting time for the food to
#  be served
# Add an option to add tips (% from the full cost) to the final bill.
# After the payment , system should generate the receipt (logging).


from typing import List
import datetime

now_hour = (lambda t: t.strftime("%H"))(datetime.datetime.now())


class Cafeteria:
    # tables
    single_table = [1]
    double_table = [2, 3]
    family_table = [4, 5, 6]
    # meniu


class Reservation:
    def __init__(self, name: str, surname: str, reservation_hour: int) -> None:
        self.name = name
        self.surname = surname
        self.reservation_hour = reservation_hour


class Table:
    def __init__(self, number_of_seats: int) -> None:
        self.number_of_seats = number_of_seats
        self.reservations: List[Reservation] = []

    def create_reservation(self, name, surname, reservation_hour):
        reservation = Reservation(name, surname, reservation_hour)
        self.reservations.append(reservation)

    def check_aviability(self, name: str, surname: str, now_hour: int):
        for reservation in self.reservations:
            if (
                reservation.name == name
                and reservation.surname == surname
                and reservation.reservation_hour == now_hour
            ):
                print(
                    f"Welcome to our Cafeteria {name} {surname}. You have reservation"
                )
                return False

        print(f"Welcome to our Cafeteria {name} {surname}. You dont have reservation")
        return True


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


single_table = Table(1)
double_table = Table(2)
family_table = Table(5)

family_table.create_reservation("Oleg", "Arslanov", 18)
family_table.create_reservation("Luis", "Fernandez", 21)

family_table.check_aviability(
    input("Please enter name:"),
    input("Please enter surname:"),
    int(now_hour),
)
