# Exercise #1
clothes = ["socks", "shirt", "skirt", "scarf"]
def insert_element(new_cloth, index=0):
    clothes.insert(index, new_cloth)
    print(clothes)

insert_element('hat', 1)
insert_element('coat', -2)
insert_element('jeans')

#Exercise#2

employee_shift = ["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"]

def replace_employee(employee_shift, old_employee, new_employee):

    old_employee_replace =employee_shift.index(old_employee)
    employee_shift.remove(old_employee)
    employee_shift.insert(old_employee_replace,new_employee)
    print(employee_shift)
replace_employee(employee_shift, "Kelly", "Maria")

