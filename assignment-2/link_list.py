class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find_middle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr.data

    def merge_sorted(self, other):
        merged = LinkedList()
        current1 = self.head
        current2 = other.head
        while current1 and current2:
            if current1.data < current2.data:
                merged.insert(current1.data)
                current1 = current1.next
            else:
                merged.insert(current2.data)
                current2 = current2.next
        while current1:
            merged.insert(current1.data)
            current1 = current1.next
        while current2:
            merged.insert(current2.data)
            current2 = current2.next
        return merged

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    # Creating linked lists
    list1 = LinkedList()
    list2 = LinkedList()

    # Inserting elements
    list1.insert(3)
    list1.insert(7)
    list1.insert(9)
    list1.insert(12)

    list2.insert(2)
    list2.insert(5)
    list2.insert(8)
    list2.insert(10)

    # Displaying lists
    print("List 1:")
    list1.display()
    print("List 2:")
    list2.display()

    # Deleting an element
    list1.delete(7)
    print("List 1 after deleting 7:")
    list1.display()

    # Searching an element
    print("Is 9 in List 1?", list1.search(9))

    # Reversing list
    list1.reverse()
    print("List 1 after reversing:")
    list1.display()

    # Finding middle element
    print("Middle element of List 1:", list1.find_middle())

    # Merging sorted lists
    merged_list = list1.merge_sorted(list2)
    print("Merged sorted list:")
    merged_list.display()
