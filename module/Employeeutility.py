def calculate_salary(basic_salary, leaves):
    paid_leaves = 15
    if leaves > paid_leaves:
        extra_leaves = leaves - paid_leaves
        basic_salary -= (basic_salary / 30) * extra_leaves
    return basic_salary


def calculate_bonus(salary, emp_type):
    if emp_type == "coder":
        return salary * 0.10
    elif emp_type == "designer":
        return salary * 0.15
    elif emp_type == "manager":
        return salary * 0.05
    else:
        return 0


emp_name = input("Enter employee name: ")
emp_type = input("Enter employee type (coder/designer/manager): ").lower()
leaves_taken = int(input("Enter leaves taken: "))
basic_salary = float(input("Enter basic salary: "))

# Calculation
salary_after_leaves = calculate_salary(basic_salary, leaves_taken)
bonus = calculate_bonus(salary_after_leaves, emp_type)
final_salary = salary_after_leaves + bonus

# Output
print("\nEmployee Name:", emp_name)
print("Employee Type:", emp_type)
print("Final Salary:", final_salary)




