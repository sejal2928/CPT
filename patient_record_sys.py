import csv

# Get user input
patient_id = input("Enter patient ID: ")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
dob = input("Enter date of birth (YYYY-MM-DD): ")
gender = input("Enter gender: ")
phone_number = input("Enter phone number: ")
address = input("Enter address: ")

# Define the CSV file and headers
csv_file = 'patients.csv'
headers = ['patient_id', 'first_name', 'last_name', 'dob', 'gender', 'phone_number', 'address']

# Create a dictionary with user input
patient_data = {
    'patient_id': patient_id,
    'first_name': first_name,
    'last_name': last_name,
    'dob': dob,
    'gender': gender,
    'phone_number': phone_number,
    'address': address
}

# Write to CSV
with open(csv_file, mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    # Check if the file is empty and write headers if needed
    if file.tell() == 0:
        writer.writeheader()
    writer.writerow(patient_data)

print(f'Data saved to {csv_file}')
