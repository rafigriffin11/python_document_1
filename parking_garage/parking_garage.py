class parking_garage():

    def __init__(self, totalTickets):
        self.totalTickets = 50
        # self.parking_Spaces = totalParkingSpaces
        # self.current_Ticket = {}

    def takeTicket(self):
        print("Press '1' to print parking ticket. ")
        option = input('')
        if option == '1':
            totalTickets -= 1
            totalParkingSpaces -= 1
        else:
            print('no ticket purchased')

    def payForParking(self):
        print('Parking Rate: \n $5 for first hour \n $3 per hour after first hour')
        payment = input('How much time would you like to buy?')
        if payment:
            print(f"Your parking is valid for {payment} hour(s).")

    def leaveGarage():






# garage = parking_garage([])

# def run_program():
#     while True:
#         print('\nParking Menu:')
#         print("1 - print parking ticket")
#         print("2 - pay for parking ticket")

#         choose = input('Enter your choice of option (1 or 2): ')

#         if choose == '1':
#             garage.takeTicket()
#         elif choose == '2':
#             garage.leaveGarage()
#         else:
#             print('Invalid choice. please try again')

# run_program()