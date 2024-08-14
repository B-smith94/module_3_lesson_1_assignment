#Task 1
def add_service_ticket(ticket_dict, ticket_num):
    if ticket_num not in ticket_dict:
        ticket_dict[ticket_num] = {}
        print(f"{ticket_num} added.")
    else:
        print(f"{ticket_num} already exists")


def update_service_ticket(ticket_dict, ticket_num, ticket_data):
    if ticket_num in ticket_dict:
        ticket_dict[ticket_num] = ticket_data
        print(f"{ticket_num} updated.")
    else:
        print(f"{ticket_num} not found.")

def display_tickets(tickets):
    for ticket, data in service_tickets.items():
        print(f"Ticket Number: {ticket}")
        for category, user_input in data.items():
            print(f"  {category}: {user_input}")

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"},
}

add_service_ticket(service_tickets, "Ticket002")
update_service_ticket(service_tickets, "Ticket002", {"Customer": "Hannah", "Issue": "Unable to update cart", "Status": "open"})
display_tickets(service_tickets)

