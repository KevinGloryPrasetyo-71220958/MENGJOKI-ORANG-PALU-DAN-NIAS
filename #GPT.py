#GPT
class Patient:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

class Node:
    def __init__(self, patient):
        self.patient = patient
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def insert(self, patient):
        new_node = Node(patient)
        if not self.head or patient.priority > self.head.patient.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and patient.priority <= current.next.patient.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def pop(self):
        if not self.head:
            return None
        popped_patient = self.head.patient
        self.head = self.head.next
        return popped_patient

    def delete(self, patient_name):
        current = self.head
        if current and current.patient.name == patient_name:
            self.head = current.next
            return
        while current.next:
            if current.next.patient.name == patient_name:
                current.next = current.next.next
                return
            current = current.next

    def peek(self):
        return self.head.patient if self.head else None

    def is_empty(self):
        return self.head is None

# Contoh penggunaan:
queue = PriorityQueue()

# Menambahkan pasien ke antrian dengan prioritas
queue.insert(Patient("John", 3))
queue.insert(Patient("Alice", 1))
queue.insert(Patient("Bob", 2))

# Mengambil pasien dengan prioritas tertinggi
print("Pasien dengan prioritas tertinggi:", queue.pop().name)

# Menghapus pasien tertentu dari antrian
queue.delete("Alice")

# Melihat pasien dengan prioritas tertinggi tanpa menghapusnya
print("Pasien dengan prioritas tertinggi (peek):", queue.peek().name)

# Memeriksa apakah antrian kosong
print("Antrian kosong:", queue.is_empty())



#BING
class Patient:
    def _init_(self, name, priority):
        self.name = name
        self.priority = priority

class Node:
    def _init_(self, patient=None, next=None):
        self.patient = patient
        self.next = next

class PriorityQueue:
    def _init_(self):
        self.head = None

    def push(self, patient):
        new_node = Node(patient)
        if not self.head or patient.priority > self.head.patient.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and patient.priority <= current.next.patient.priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def pop(self):
        if not self.head:
            return None
        else:
            popped = self.head.patient
            self.head = self.head.next
            return popped

    def delete(self, patient):
        current = self.head
        previous = None
        while current and current.patient != patient:
            previous = current
            current = current.next
        if previous is None:
            self.head = current.next
        elif current:
            previous.next = current.next
            current.next = None

    def peek(self):
        if not self.head:
            return None
        else:
            return self.head.patient

    def is_empty(self):
        return not bool(self.head)