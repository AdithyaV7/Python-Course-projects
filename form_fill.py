import datetime
import csv
import os

# Function to calculate the birthday and gender
def calculate_birthday_and_gender(nic):
    if len(nic) == 10 and (nic[9] == 'V' or nic[9] == 'v'): #check nic's V in the end
        birth_year = int(nic[:2]) + 1900
        days = int(nic[2:5])
    elif len(nic) == 12:
        birth_year = int(nic[:4])
        days = int(nic[4:7])
    else:
        return None, None
    
    # Determine gender
    gender = "Male"
    if days > 500:
        gender = "Female"
    
    if gender == "Female": 
        days = days -500

    #For leap years
    if (birth_year%4 == 0) :
        birth_date = datetime.date(birth_year, 1, 1) + datetime.timedelta(days=days - 1)
    else:
        birth_date = datetime.date(birth_year, 1, 1) + datetime.timedelta(days=days - 2)

    return birth_date, gender

#write data in csv file
def write_to_csv(name,nic,birthday,gender):
    file_exist = os.path.isfile('C:/Users/Adithya/Documents/Python VS/GUI-Projects/data.csv')
    with open("C:/Users/Adithya/Documents/Python VS/GUI-Projects/data.csv", "a+",newline='') as file:
        writer = csv.writer(file)
        if not file_exist:
            writer.writerow(['Name', 'NIC', 'Date of Birth', 'Gender'])
        writer.writerow([name, nic, birthday, gender])

#Print values entered
def print_values(birthday, gender, name, nic):
    if birthday and gender:
        print(f"Name: {name}")
        print(f"NIC: {nic}")
        print(f"Birthday: {birthday.strftime('%Y-%m-%d')}")
        print(f"Gender: {gender}")
    else:
        print("Invalid NIC number format.")

# Get user input
name = input("Enter your Name: ")
nic = input("Enter your NIC number: ")

# Calculate birthday and gender
birthday, gender = calculate_birthday_and_gender(nic)
write_to_csv(name,nic,birthday,gender)
print_values(birthday,gender,name,nic)


