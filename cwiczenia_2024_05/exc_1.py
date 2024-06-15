#EXERCISE 1: Employee Class
print("Zadanie 1")
class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print(f"Name: {self.emp_name}, ID: {self.emp_id}, Salary: {self.emp_salary}, Department: {self.emp_department}")

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            self.emp_salary += overtime_amount
        return self.emp_salary
#Example Usage:
# Creating employee instances
adam = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
jones = Employee("JONES", "E7499", 45000, "RESEARCH")

# Assigning a new department to an employee
adam.assign_department("MARKETING")

# Printing employee details
adam.print_employee_details()
jones.print_employee_details()

# Calculating salary with overtime
print(f"Adam's new salary with overtime: {adam.calculate_emp_salary(60)}")
#EXERCISE 2: Restaurant Class
print("Zadanie 2")
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = {}
        self.customer_orders = []

    def add_item_to_menu(self, item_name, price):
        self.menu_items[item_name] = price

    def book_tables(self, table_number, customer_name):
        self.book_table[table_number] = customer_name

    def customer_order(self, order):
        self.customer_orders.append(order)

    def print_menu(self):
        for item, price in self.menu_items.items():
            print(f"{item}: {price}")

    def print_table_reservations(self):
        for table, customer in self.book_table.items():
            print(f"Table {table}: Reserved by {customer}")

    def print_customer_orders(self):
        for order in self.customer_orders:
            print(order)
#Example Usage:
# Creating a restaurant instance
my_restaurant = Restaurant()

# Adding items to the menu
my_restaurant.add_item_to_menu("Pizza", 10)
my_restaurant.add_item_to_menu("Burger", 5)

# Booking tables
my_restaurant.book_tables(1, "John Doe")
my_restaurant.book_tables(2, "Jane Smith")

# Taking customer orders
my_restaurant.customer_order({"Table": 1, "Order": ["Pizza", "Coke"]})
my_restaurant.customer_order({"Table": 2, "Order": ["Burger", "Sprite"]})

# Printing the menu
my_restaurant.print_menu()

# Printing table reservations
my_restaurant.print_table_reservations()

# Printing customer orders
my_restaurant.print_customer_orders()
#EXERCISE 3: BankAccount Class
print("Zadanie 3")
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0, date_of_opening=None):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance
#Example Usage:
# Creating a bank account instance
johns_account = BankAccount("123456789", "John Doe", 1000, "2024-06-15")

# Depositing money
johns_account.deposit(500)

# Withdrawing money
johns_account.withdraw(200)

# Checking balance
print(f"John's current balance: {johns_account.check_balance()}")
#EXERCISE 4: Inventory Class
print("Zadanie 4")
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.items[item_id] = {'item_name': item_name, 'stock_count': stock_count, 'price': price}

    def update_item(self, item_id, item_name=None, stock_count=None, price=None):
        if item_id in self.items:
            if item_name:
                self.items[item_id]['item_name'] = item_name
            if stock_count:
                self.items[item_id]['stock_count'] = stock_count
            if price:
                self.items[item_id]['price'] = price

    def check_item_details(self, item_id):
        return self.items.get(item_id, "Item not found")
#Example Usage:
# Creating an inventory instance
store_inventory = Inventory()

# Adding items to the inventory
store_inventory.add_item("001", "Laptop", 10, 999.99)
store_inventory.add_item("002", "Smartphone", 15, 499.99)

# Updating an item in the inventory
store_inventory.update_item("001", stock_count=8)

# Checking item details
print(store_inventory.check_item_details("001"))
