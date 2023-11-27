class ParkingGarage:

    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}

    def takeTicket(self):
        if not self.tickets:
            print("\nSorry, the garage is full. No tickets available.")
            return

        ticket_number = self.tickets.pop(0)
        parking_space = self.parkingSpaces.pop(0)
        self.currentTicket[ticket_number] = {"paid": False, "parking_space": parking_space}
        print(f"\nTicket #{ticket_number} issued. Parking space #{parking_space} assigned.")

    def payForParking(self):
        ticket_number = int(input("\nEnter your ticket number: "))
        if ticket_number in self.currentTicket and not self.currentTicket[ticket_number]["paid"]:
            payment = input("Enter the payment amount: ")
            if payment and payment.isdigit():
                payment_amount = int(payment)
                self.currentTicket[ticket_number]["paid"] = True
                print("\nTicket paid. You have 15 minutes to leave.")
            else:
                print("Invalid payment amount. Please pay a valid amount to leave.")
        else:
            print("Invalid ticket number or ticket already paid.")


    def leaveGarage(self):
        ticket_number = int(input("Enter your ticket number: "))
        if ticket_number in self.currentTicket:
            if self.currentTicket[ticket_number]["paid"]:
                print("Thank you, have a nice day!")
                self.parkingSpaces.append(self.currentTicket[ticket_number]["parking_space"])
                self.tickets.append(ticket_number)
                del self.currentTicket[ticket_number]
            else:
                print("Payment not received. Please pay to leave.")
        else:
            print("Invalid ticket number.")

# Example usage:
garage = ParkingGarage(total_tickets=5, total_parking_spaces=5)

def run_program():
    while True:
        print('\nParking Menu:')
        print("1 - print parking ticket")
        print("2 - pay for parking ticket")

        choose = input('Enter your choice of option (1 or 2): ')

        if choose == '1':
            garage.takeTicket()
        elif choose == '2':
            garage.payForParking()
        else:
            print('Invalid choice. please try again')

run_program()


