'''
Class Constructor
In the examples above, we have created an object from the Person class. However, a class without a constructor is not really useful in real applications. Let us use constructor function to make our class more useful. Like the constructor function in Java or JavaScript, Python has also a built-in init() constructor function. The init constructor function has self parameter which is a reference to the current instance of the class Examples:
'''

class person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
p = person('Parineeta','Sarkar')
print('Full Name: ',p.firstName+' '+ p.lastName)

'''Object Methods
Objects can have methods. The methods are functions which belong to the object.

Example:
'''

class person_1:
    def __init__(self,firstName,lasrName):
        self.firstName = firstName
        self.lastName = lasrName
    def person_info(self):
        return f'My name is {self.firstName} {self.lastName}'
    
p_1 = person_1('Parineeta','Sarkar')
print(p_1.person_info())

'''
Object Default Methods
Sometimes, you may want to have a default values for your object methods. If we give default values for the parameters in the constructor, we can avoid errors when we call or instantiate our class without parameters. Let's see how it looks:

Example:
'''

class person_2:
    def __init__(self,firstName='Parineeta',lastName='Sarkar'):
        self.firstName = firstName
        self.lastName = lastName
    def person_info(self):
        return f'My full name is {self.firstName} {self.lastName}'
p_2 = person_2()
p_3 = person_2('Soumajit','Sarkar')
print(p_2.person_info())
print(p_3.person_info())


'''
Inheritance
Using inheritance we can reuse parent class code. Inheritance allows us to define a class that inherits all the methods and properties from parent class. The parent class or super or base class is the class which gives all the methods and properties. Child class is the class that inherits from another or parent class. Let us create a student class by inheriting from person class.
'''
class Student(person_2):
    def __init__(self, firstName='Parineeta', lastName='Sarkar',gender = 'male'):
        self.gender = gender
        super().__init__(firstName, lastName)
    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'My full name is {self.firstName} {self.lastName} and my gender is {gender}'
s1 = Student('Mayuri','Sarkar','female')
print(s1.person_info())


'''
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
'''

class PersonAccount:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.income = {}
        self.expenses = {}
    def add_income(self,amount,description):
        self.income[description] = amount
    def add_expense(self,amount,description):
        self.expenses[description] = amount
    def total_income(self):
        return sum(self.income.values())
    def total_expense(self):
        return sum(self.expenses.values())
    def account_balance(self):
        return self.total_income() - self.total_expense()
    def account_info(self):
        info = f'Account balance for {self.firstname} {self.lastname}:\n'
        info += f'Total income: {self.total_income()}\n'
        info += f'Total expences: {self.total_expense()}\n'
        info += f'Account Balanace: {self.account_balance()}\n'
        info += "Account Balance:\n"
        for desc, amount in self.income.items():
            info += f"  {desc}: {amount}\n"
        info += "Expense Details:\n"
        for desc, amount in self.expenses.items():
            info += f"  {desc}: {amount}\n"
        return info
    
p_4 = PersonAccount("John", "Doe")
p_4.add_income(5000, "Salary")
p_4.add_income(1000, "Bonus")
p_4.add_expense(2000, "Rent")
p_4.add_expense(500, "Groceries")
print(p_4.account_info())
