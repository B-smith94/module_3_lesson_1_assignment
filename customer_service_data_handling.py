#Task 1
import copy
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
    all_or_filter = input("Display All or Filter by Status (type all or filter): ")
    if all_or_filter.lower() == "all":
        for ticket, data in tickets.items():
            print(f"Ticket Number: {ticket}")
            for category, user_input in data.items():
                print(f"  {category}: {user_input}")
    elif all_or_filter.lower() == "filter":
        filtered_list = copy.deepcopy(tickets)
        while True:
            open_or_closed = input("Filter by (open/closed): ")
            if open_or_closed.lower() == "open":
                for ticket, data in filtered_list.items():
                    if filtered_list[ticket]["Status"] == "open":
                        print(f"Ticket Number: {ticket}")
                        for category, user_input in data.items():
                            print(f"   {category}: {user_input}")
                break
            elif open_or_closed.lower() == "closed":            
                for ticket, data in filtered_list.items():
                    if filtered_list[ticket]["Status"] == "closed":
                        print(f"Ticket Number: {ticket}")
                        for category, user_input in data.items():
                            print(f"   {category}: {user_input}")
                break
            else:
                print("Invalid input, please try again.")
                continue
    else:
        print("Error: Invalid Input.")

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"},
}

add_service_ticket(service_tickets, "Ticket003")
update_service_ticket(service_tickets, "Ticket003", {"Customer": "Hannah", "Issue": "Unable to update cart", "Status": "open"})
display_tickets(service_tickets)

