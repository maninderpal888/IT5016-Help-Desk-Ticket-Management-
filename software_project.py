from collections import namedtuple

# Define a namedtuple for Ticket data
Ticket = namedtuple(
    "Ticket",
    [
        "ticket_number",
        "ticket_creator_name",
        "staff_id",
        "contact_email",
        "description",
        "response",
        "status",
    ],
)


class TicketingSystem:
    def __init__(self):
        self.tickets = []
        self.next_ticket_number = 2000

    def submit_ticket(self, ticket_creator_name, staff_id, contact_email, description):
        new_ticket_number = self.next_ticket_number
        self.next_ticket_number += 1
        ticket = Ticket(
            new_ticket_number,
            ticket_creator_name,
            staff_id,
            contact_email,
            description,
            "Not Yet Provided",
            "Open",
        )
        self.tickets.append(ticket)
        print(f"\nTicket ID: {ticket.ticket_number} - Ticket submitted successfully.")

    def display_tickets(self):
        if not self.tickets:
            print("No tickets to display.")
            return

        for ticket in self.tickets:
            print("\n************Display Tickets *********************")
            print(ticket)

    def ticket_statistics(self):
        created = len(self.tickets)
        resolved = sum(1 for ticket in self.tickets if ticket.status == "Closed")
        to_solve = sum(1 for ticket in self.tickets if ticket.status != "Closed")

        print("\n***************Displaying Ticket Statistics*************\n")
        print(
            f"Tickets Created: {created}\nTickets Resolved: {resolved}\nTickets To Solve: {to_solve}\n"
        )

    def resolve_ticket(self, ticket_number, response):
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_number:
                if "Password Change" in ticket.description:
                    new_password = f"{ticket.staff_id[:2]}{ticket.ticket_creator_name[:3]}"
                    ticket = ticket._replace(response=f"New password generated: {new_password}", status="Closed")
                else:
                    ticket = ticket._replace(response=response, status="Closed")
                print("Ticket resolved successfully.")
                return

        print("Ticket not found.")

    def reopen_ticket(self, ticket_number):
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_number:
                ticket = ticket._replace(status="Reopened")
                print("Ticket reopened successfully.")
                return

        print("Ticket not found.")


# Main function
def main():
    ticketing_system = TicketingSystem()
    print("\n***********************************")
    print("Help Desk Ticketing management")
    print("\n***********************************")
    while True:

        print("\nMenu:")
        print("1. Submit Ticket")
        print("2. Display Tickets")
        print("3. Ticket Statistics")
        print("4. Resolve Ticket")
        print("5. Reopen Ticket")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n************Create a new Ticket*************")
            ticket_creator_name = input("\nEnter ticket creator's name: ")
            staff_id = input("Enter staff ID: ")
            contact_email = input("Enter contact email: ")
            description = input("Enter issue description: ")
            ticketing_system.submit_ticket(
                ticket_creator_name, staff_id, contact_email, description
            )

        elif choice == "2":
            ticketing_system.display_tickets()

        elif choice == "3":
            ticketing_system.ticket_statistics()

        elif choice == "4":
            ticket_number = int(input("\nEnter ticket number to resolve: "))
            response = input("Enter response: ")
            ticketing_system.resolve_ticket(ticket_number, response)

        elif choice == "5":
            ticket_number = int(input("Enter ticket number to reopen: "))
            ticketing_system.reopen_ticket(ticket_number)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from the menu.")


if __name__ == "__main__":
    main()