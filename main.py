class Order:
    def __init__(self, order_id, customer_name, order_details):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_details = order_details
        
        
        
        
    def  __str__(self):
            return f"OrderID: {self.order_id}, Customer: {self.customer_name}, Details: {self.order_details}"
        
        
class Node:
    
    def __init__(self,order):
        self.order = order
        self.next = None
        
        
class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def append(self , order):
        new_node = Node(order)
        
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def display(self):
            current = self.head
            
            if current is None:
                print("No orders in list.")
                return
            while current:
                print(current.order)
                current = current.next
                
                
    def reverse(self):
        pervious = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = pervious
            pervious = current
            current = next_node
            
            
        self.head = pervious
        
        
        
if __name__ == "__main__":
    orders = SinglyLinkedList()

    orders.append(Order(101, "Ali", "Laptop"))
    orders.append(Order(102, "John", "Headphones"))
    orders.append(Order(103, "BC", "New Tv"))

    print("Original Order List:")
    orders.display()

    orders.reverse()

    print("\nReversed Order List:")
    orders.display()
            
        
        
        
        