import unittest
from main import Order, SinglyLinkedList


class TestOrderLinkedList(unittest.TestCase):
    
    
    # Normal case
    
    def test_append_orders(self):
        ll = SinglyLinkedList()
        ll.append(Order(1, "Ali" , "Laptop"))
        ll.append(Order(2, "John" , "Headphone"))
        
        
        self.assertEqual(ll.head.order.order_id, 1)
        self.assertEqual(ll.head.next.order.order_id, 2)
        
        
    def test_reverse_multiple_orders(self):
        ll = SinglyLinkedList()
        
        ll.append(Order(1, "A", "Item1"))
        ll.append(Order(2, "B", "Item2"))
        ll.append(Order(3, "C", "Item3"))
        
        ll.reverse()
        
        self.assertEqual(ll.head.order.order_id, 3)
        
        

    def test_order_information(self):
        order = Order(10, "Ali", "Laptop")
        self.assertEqual(order.customer_name, "Ali")
        self.assertEqual(order.order_details,  "Laptop")
        
        
        
        # Edge case
        
        
        
        
    def test_reverse_empty_list(self):
        ll = SinglyLinkedList()
        
        ll.reverse()
        self.assertIsNone(ll.head)
        
        
    def test_reverse_single_order(self):
        
        ll = SinglyLinkedList()
        
        ll.append(Order(2, "John" , "Headphon"))
        ll.reverse()
        self.assertEqual(ll.head.order.order_id, 2)
        
       
       
    def test_append_to_empty_list(self):
        ll = SinglyLinkedList()
        
        ll.append(Order(100, "BC", "New TV"))
        
        self.assertIsNotNone(ll.head)
        
        
if __name__ == "__main__":
    unittest.main()
        
        
        
