import csv

def write_in_csv(student_info_l):
    
    with open('student_admin_info.csv', 'a', newline='') as cf:
        writer=csv.writer(cf)

        if cf.tell()==0:
            writer.writerow(['Name', 'age', 'contact number', 'email id'])

        writer.writerow(student_info_l.split(' '))
        print('given information has been registered successfully')



condition=True
studentnum=1

while (condition):
    student_info=input('enter the student #{} information (enter only in this format) (Name Age Contact email): '.format(studentnum))

    student_info_l=student_info.split(' ')
    
    print('\nthe information entered is: \nName: {} \nAge: {} \nContact number: {} \nEmail: {}'
    .format(student_info_l[0], student_info_l[1], student_info_l[2], student_info_l[3]))

    while condition:

        check=input('is the entered information correct (y/n): ')
        if check=='y' or check=='n':
            break
        else:
            print('give a valid confirmation(y/n)')


    if check=='y':

        write_in_csv(student_info) 

        while condition:
            condition_check=input('do you want to enter the information of another student (y/n): ')
            if condition_check=='y' or condition_check=='n':
                break
            else:
                print('give a valid confirmation(y/n)')

        if condition_check=='y':
            condition=True
            studentnum=studentnum+1

        elif condition_check=='n':
            condition=False

    elif check=='n':
        print('please enter the correct information!')

print('\nPLEASE DELETE THE PREVIOUS FILE IF YOU WANT THE INFORMATION TO BE IN A NEW FILE \nTHANK YOU!')
    
