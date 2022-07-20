#This program gets employee data from users and saves it as records in the employee.txt file
def main():
    #Get the number of records
    num_emps=int(input('How many records do you want to create? '))

    #Open a file for writing
    employee_file=open('employees.txt',mode='w',encoding='utf-8')

    #Get the data 
    for emp_num in range(num_emps):
        print(f'Enter data for employee {emp_num+1}:')
        name=input('Name: ')
        id=int(input('ID Number: '))
        dept=input('Department: ')

        #Write the data as record to the file
        employee_file.write(f'{name}\n')
        employee_file.write(f'{id}\n')
        employee_file.write(f'{dept}\n')
        print()
    employee_file.close()
    print('Employee records written to employees.txt')

main()