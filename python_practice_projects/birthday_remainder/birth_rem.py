import datetime
current_date = datetime.date.today().strftime('%Y-%m-%d') #it is today() and not today
current_date_lst=current_date.split('-')
bday_log =[
    ('god',('2000','01','26')),
    ('human',('2001','11','25'))
]  #include comma between each tuple 
###i want to send notification daily at sometime random time to the user to check if they want to add anyone's birthday to remember and put the add in the if condition
add=input("DO YOU WANT TO ADD A NEW MEMBER'S BIRTHDAY FOR REMINDER?\nIF SO KINDLY COMMENT YES: ").strip().lower() ##how to use \n
print(add[:1]) 
# add[0]: This directly accesses the first character of the string. If the string is not empty, it returns the first character; otherwise, it will result in an IndexError if the string is empty.

# Example:
# add = "example"
# first_char = add[0]  # This gets the first character 'e'
# add[:1]:#This uses slicing to get a substring starting from the beginning (index 0) up to, but not including, the character at index 1. It ensures that even if the string is empty, it won't result in an IndexError, and an empty string will be returned.
###else if no leave it
if add[:1]=='y': #use'=='
    new = input("ADD BIRTHDAY IN THE FORMAT YEAR-MONTH-DAY: ")#how to convert if mentioned april to 04"
    date = new.split('-')
    name = input("Name of the the birthday baby: ")
    bday_log.append(name,tuple(date))
for birthday in bday_log:
    if current_date_lst[1] == birthday[1][1] and current_date_lst[2] == birthday[1][2]:
        age = int(current_date_lst[0]) - int(birthday[1][0])    
        ordinal_suffix = {1: 'st', 2 :'nd', 3:'rd' , 11: 'th' , 12:'th' , 13: 'th'}.get(age %10 if not 10 < age <= 13 else age % 14,'th')
        print(f" It's {birthday[0]}'s {age}{ordinal_suffix} Birthday\n .Kindly wish them now")
        #how to send reminder at 12 at midnight
   





# import datetime #datetime is a library to perform alike operations
# current_date = datetime.date.today().strftime('%Y-%m-%d')
# print(current_date)
# current_date_lst = current_date.split('-')#current date
# print(current_date_lst)
# bday_log = [
#    ('Ayushi', ('1999', '10', '19')),
#    ('Yash', ('1999', '04', '21')),
# ]#name along with birthday date,month,year
# add = input('To add birthday type y:').strip().lower()#confirmation to add new bithday information
# print(add[:1])
# if add[:1] == 'y':
#    new = input('Add birthday in format yyyy-mm-dd:')#adding new birthday
#    # print(new_lst)
#    name = input('Whose bday?')#name
#    date = new.split( '-' )
#    print(date)
#    bday_log.append((name, tuple(date)))#adding the newly mentioned name and birthday to the existing birthday listbday.log
# for birthday in bday_log:
#    # current_dat[1] == birthday[1][1] this will check if current month is same as birth month  and current date is same as
#    # birth date as per preadded log
#    if current_date_lst[1] == birthday[1][1] and current_date_lst[2] == birthday[1][2]:
#        age = int(current_date_lst[0]) - int(birthday[1][0])
#        print(age%10,age%14)
#        ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd', 11: 'th', 12: 'th', 13: 'th'}.get(age % 10 if not 10 < age <= 13 else age % 14, 'th')
#        print(f" It's {birthday[0]}'s {age}{ordinal_suffix} Birthday")