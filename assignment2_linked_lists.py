# BCP 210: Data Structures and Algorithms I
# Coursework Assignment 1: Linked Lists - Starter Template

class Ticket:
    def __init__(self, ticket_id, student_name, issue):
        """
        Do not modify this constructor.
        """
        self.ticket_id = ticket_id
        self.student_name = student_name
        self.issue = issue
        self.next = None

    def __repr__(self):
        return f"Ticket({self.ticket_id}, '{self.student_name}')"


class TicketQueue:
    def __init__(self):
        self.head = None

    def add_ticket(self, ticket_id, student_name, issue):
        """
        1. Enqueue Ticket (8 Marks)
        Add a new ticket node to the end of the queue.
        """
        # TODO: Implement your solution here
        pass

    def insert_after(self, target_id, ticket_id, student_name, issue):
        """
        2. Priority Insert (10 Marks)
        Insert a new priority ticket immediately after a specified ticket ID.
        Return True if successful, False if the target ID is not found.
        """
        # TODO: Implement your solution here
        pass

    def delete_ticket(self, ticket_id):
        """
        3. Resolve Ticket (9 Marks)
        Delete a resolved ticket from the queue given its ticket ID.
        Return True if deleted, False if the ticket ID is not found.
        """
        # TODO: Implement your solution here
        pass

    def middle_ticket(self):
        """
        4. Find Middle Ticket (8 Marks)
        Find and return the middle Ticket node of the queue in a single traversal pass.
        If the queue has an even number of tickets, return the second middle node.
        """
        # TODO: Implement your solution here
        pass

    def reverse(self):
        """
        5. Reverse Queue (10 Marks)
        Reverse the queue in-place (manipulating pointers, no data copying).
        """
        # TODO: Implement your solution here
        pass

    def display(self):
        """
        6. Display Queue (4 Marks)
        Print all ticket details in the format: "Ticket ID | Student Name | Issue"
        """
        # TODO: Implement your solution here
        pass


if __name__ == "__main__":
    print("--- Testing Assignment 2: Linked Lists ---")
    queue = TicketQueue()
    
    # 1. Test add_ticket
    queue.add_ticket(101, "Silas Gah", "Cannot access student portal")
    queue.add_ticket(102, "Ama Mensah", "WiFi password reset")
    queue.add_ticket(103, "Kofi Osei", "Exam registration issue")
    print("Initial Queue:")
    queue.display()
    
    # 2. Test insert_after
    queue.insert_after(102, 105, "Esi Boakye", "Urgent: Laptop screen broken")
    print("\nQueue after inserting 105 after 102:")
    queue.display()
    
    # 3. Test middle_ticket
    mid = queue.middle_ticket()
    print(f"\nMiddle Ticket: {mid}")
    
    # 4. Test delete_ticket
    queue.delete_ticket(102)
    print("\nQueue after deleting ticket 102:")
    queue.display()
    
    # 5. Test reverse
    queue.reverse()
    print("\nReversed Queue:")
    queue.display()
