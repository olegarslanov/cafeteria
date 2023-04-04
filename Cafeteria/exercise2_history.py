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

# Algorithm:

#    1. Reservation:
#
# a) for one table
# input: name, surname, time_hour and check if table reserved (for study reason time is checked only for hour is same)
# if name, surname and hour is same, print that reservation is
# if not, print welcome message
# please enter number of guests
# check, if guest <= number of seat and time != reservation time got message to assign table
# if not got message sorry we dont have  free tables
#
# b) for more tables
# assign a table (single, double or family) by guest number
#
# implement a function that shows how many free tables and reserved tables there are( tell size of
#  free tables) make a function that shows Name/Surname/Time Reserved after reserved table id
# is given if user want to see

#     2. Ordering:
# make a function that lets customer choose anything he wishes from menus
# Give customer options to change the order before payment( delete, add,update amount )
# after ordering is finished show full cost of the order and approx waiting time
# add an option to add tips(% from full cost)

#     3. Payment:
# implement payment
# Log the receipt using loggin


# 1 Padariau 1 stalas 1 rezervacija, kuria galiu patikrinti

# class Reservation:
#     def __init__(self, name):
#         self.name = name


# class Table:
#     def __init__(self, table_number) -> None:
#         self.table_number = table_number

#     def create_reservation(self, name):
#         self.reservation = Reservation(name)

#     def check_aviability(self, name):
#         if self.reservation.name == name:
#             return False
#         return True


# class Person:
#     def __init__(self, name):
#         self.name = name


# table = Table(1)
# table.create_reservation("Oleg")

# print(table.check_aviability("Oleg"))


# 2 Papildziau, kad galima patikrinti kelios rezervacijos
# from typing import List

# class Reservation:
#     def __init__(self, name):
#         self.name = name


# class Table:
#     def __init__(self, table_number) -> None:
#         self.table_number = table_number
#         self.reservations: List[Reservation] = []

#     def create_reservation(self, name):
#         reservation = Reservation(name)
#         self.reservations.append(reservation)

#     def check_aviability(self, name):
#         for reservation in self.reservations:
#             if reservation.name == name:
#                 return False
#         return True


# class Person:
#     def __init__(self, name):
#         self.name = name


# table = Table("1")

# table.create_reservation("Oleg")
# table.create_reservation("Luiz")

# print(table.check_aviability("Luiz"))

# 3 Papildziau, kad tikrintu pagal name and surname
# from typing import List

# class Reservation:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname


# class Table:
#     def __init__(self, table_number) -> None:
#         self.table_number = table_number
#         self.reservations: List[Reservation] = []

#     def create_reservation(self, name, surname):
#         reservation = Reservation(name, surname)
#         self.reservations.append(reservation)

#     def check_aviability(self, name, surname):
#         for reservation in self.reservations:
#             if reservation.name == name and reservation.surname == surname:
#                 return False
#         return True


# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname


# table = Table("1")

# table.create_reservation("Oleg", "Arslanov")
# table.create_reservation("Luiz", "Fernandez")


# print(table.check_aviability("Luiz", "Fernandez"))

# 4 Papildziau, kad tikrintu 1 stala rezervacija pagal rezervuota laika (valanda) ir dabartini
# from typing import List
# import datetime

# now_hour = (lambda t: t.strftime("%H"))(datetime.datetime.now())
# now_hour = int(now_hour)


# class Reservation:
#     def __init__(self, name: str, surname: str, reservation_hour: int) -> None:
#         self.name = name
#         self.surname = surname
#         self.reservation_hour = reservation_hour


# class Table:
#     def __init__(self, table_number) -> None:
#         self.table_number = table_number
#         self.reservations: List[Reservation] = []

#     def create_reservation(self, name, surname, reservation_hour):
#         reservation = Reservation(name, surname, reservation_hour)
#         self.reservations.append(reservation)

#     def check_aviability(self, name, surname, now_time):
#         for reservation in self.reservations:
#             if (
#                 reservation.name == name
#                 and reservation.surname == surname
#                 and reservation.reservation_hour == now_time
#             ):
#                 return False
#         return True


# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname


# table = Table("1")
# table.create_reservation("Oleg", "Arslanov", 18)
# table.create_reservation("Luiz", "Fernandez", 21)
# print(table.check_aviability("Luiz", "Fernandez", now_hour))


# 5 Papildziau, kad ...
# please enter number of guests
# check, if guest <= number of seat and time != reservation time got message to assign table
# if not got message sorry we dont have free tables

from typing import List
import datetime

now_hour = (lambda t: t.strftime("%H"))(datetime.datetime.now())


class Cafeteria:
    tables = {
        "single_table": {
            "nr1": {"reserved": False},
            "nr2": {
                "reserved": True,
                "name": "customer_name",
                "surname": "customer_surname",
                "reservation_hour": "some_future_time",
            },
        },
        "double_table": {"nr3": {"reserved": False}, "nr4": {"reserved": False}},
        "family_table": {
            "nr5": {"reserved": False},
            "nr6": {"reserved": False},
            "nr7": {"reserved": False},
        },
    }
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

    # def check_aviability(self, guests_quant):
    #     for reservation in self.reservations:
    #         elif (reservation.reservation_hour != now_hour):
    #             print("But good news for You, we have table free. Please sit down")


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


# single_table = Table(1)
# double_table = Table(2)
family_table = Table(5)

family_table.create_reservation("Oleg", "Arslanov", 18)
family_table.create_reservation("Luis", "Fernandez", 21)

family_table.check_aviability(
    input("Please enter name:"),
    input("Please enter surname:"),
    int(now_hour),
)

# if table.check_reservation == True:
#     table.check_aviability(
#         input("We can check for free table. Please enter how many guests:")
# )
