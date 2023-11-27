class ParkingGarage:

    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if not self.tickets:
            print('\nSorry, this garage is currently full. try our other garage located at 212 San Jacinto st.')
            return
        
        ticket_number = self.tickets.pop(0)
        parking_space = self.parkingSpaces.pop(0)
        self.currentTicket[ticket_number] = {'paid': False, 'parking_space': parking_space}
        print(f"\nTicket #{ticket_number} issued. Please proceed to parking space #{parking_space}.")

    def payForParking(self):
        ticket_number = int(input('Enter your ticket number: '))
        if ticket_number in self.currentTicket and not self.currentTicket[ticket_number]['paid']:
            print('you have been parked for __ hours, and owe $__.')
            accept_charges = input("Type 'yes' to accept this charge and exit garage: ")

            if accept_charges.lower() == "yes":
                self.currentTicket[ticket_number]['paid'] = True
                self.parkingSpaces.append(self.currentTicket[ticket_number]['parking_space'])
                print('\nYour ticket has been paid, you have 15 minutes to leave.')
                print('\tThank you, have a nice day!')
            else:
                print('To dispute this charge, please pull off to the side and call our help line at 1-800-555-5555.')
        else:
            print('Invalid ticket number.')

    def leaveGarage(self):
        ticket_number = int(input('Enter your ticket number: '))

        if ticket_number in self.currentTicket:
            if self.currentTicket[ticket_number]['paid']:
                print('Thank you, have a nice day!')
                self.parkingSpaces.append(self.currentTicket[ticket_number]['parking_space'])
                self.tickets.append(ticket_number)
                del self.currentTicket[ticket_number]
            else:
                print('Payment not recieved, please pay to leave')
        else:
            print('invalid ticket number')

    def currentOpenSpots(self):
        print('\nThe following parking spaces are currently available: ')
        print(sorted(self.parkingSpaces))


garage = ParkingGarage(total_tickets=20, total_parking_spaces=20)

def run_program():
    while True:
        print('\nParking Menu:')
        print("1 - print parking ticket")
        print("2 - pay for parking ticket")
        print('3 - see current open spots')

        choose = input('Enter your choice of option (1 , 2, or 3): ')

        if choose == '1':
            garage.takeTicket()
        elif choose == '2':
            garage.payForParking()
        elif choose == '3':
            garage.currentOpenSpots()
        else:
            print('Invalid choice. please try again')

run_program()