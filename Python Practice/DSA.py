# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insert_at_beginning(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def insert_at_end(self, data):
#         if self.head == None:
#             self.head = Node(data, None)
#             return
        
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data)
    
#     def insert_values(self, data):
#         for val in data:
#             self.insert_at_end(val)
    
#     def length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count += 1
#             itr = itr.next
#         return count

#     def remove_at(self, index):
#         if index<0 or index>=self.length():
#             raise Exception("Invalid Index")
#         elif index == 0:
#             self.head = self.head.next
#             return
        
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index-1:
#                 itr.next = itr.next.next
#                 break
#             count += 1
#             itr = itr.next

#     def insert_at(self, index, data):
#         if index<0 or index>self.length():
#             raise Exception("Invalid Index")
#         elif index == 0:
#             self.insert_at_beginning(data)
#             return
#         elif index == self.length():
#             self.insert_at_end(data)
#             return
        
#         itr = self.head
#         count = 0
#         while itr:
#             if count == index-1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 return
#             count += 1
#             itr = itr.next
        
#     """
#     def insert_after_value(self, value, data):
#         node = Node(data)
#         itr = self.head
#         count = 0
#         while itr:
#             if count == self.length():
#                 raise Exception("Invalid Input")
#             elif itr.data == value:
#                 node.next = itr.next
#                 itr.next = node
#                 return
#             itr = itr.next
#             count += 1
#     """

#     def insert_after_value(self, value, data):
#         itr = self.head
#         while itr:
#             if itr.data == value:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 return
#             itr = itr.next
#         raise Exception("Invalid Input")


#     """
#     def remove_value(self,val):
#         if val == self.head.data:
#             self.head = self.head.next
#             return
#         count = 0
#         itr = self.head
#         while itr:
#             if itr.next.data == val:
#                 itr.next = itr.next.next
#                 return
#             elif count == self.length():
#                 raise Exception("Invalid Input")
#             count += 1
#             itr = itr.next
#     """
#     def remove_value(self, val):
#         if self.head is None:
#             raise Exception("List is empty")

#         if self.head.data == val:
#             self.head = self.head.next
#             return

#         itr = self.head
#         while itr.next:
#             if itr.next.data == val:
#                 itr.next = itr.next.next
#                 return
#             itr = itr.next

#         raise Exception("Invalid Input")


#     def print(self):
#         if self.head is None:
#             print("Linked List is empty")
#             return

#         itr = self.head
#         llist = ""
#         while itr:
#             llist += str(itr.data) + " --> "
#             itr = itr.next
#         llist += "null"
#         print(llist)



# if __name__ == "__main__":
    # ll = LinkedList()
    # ll.insert_at_beginning(20)
    # ll.insert_at_end(30)
    # ll.insert_at_beginning(10)
    # ll.insert_at_end(40)
    # # ll.insert_values([50, 60, 70, 80, 90, 100)
    # # ll.remove_at(4)
    # # ll.insert_at(9, 110)
    # # ll.insert_after_value(40, 50)
    # ll.remove_value(40)
    # ll.print()


















# class Hash_Table:
#     def __init__(self):
#         self.max = 100
#         self.arr = [None for i in range(self.max)]
    
#     def get_hash(self, key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.max
    
#     def __setitem__(self, key, val):
#         self.arr[self.get_hash(key)] = val

#     def __getitem__(self, key):
#         print(self.arr[self.get_hash(key)])
    
#     def __delitem__(self, key):
#         self.arr[self.get_hash(key)] = None





# if __name__ == "__main__":
#     ht = Hash_Table()
#     ht["10 august"] = 234
#     ht["11 august"] = 246
#     ht["12 august"] = 252
#     ht["13 august"] = 292
#     ht["14 august"] = 278
#     ht["15 august"] = 250
#     ht["13 august"]
#     del ht["13 august"]
#     ht["13 august"]


















