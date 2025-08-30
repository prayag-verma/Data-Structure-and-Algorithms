from faker import Faker
import csv

# Initialize Faker
fake = Faker()

# Function to generate test data
def generate_test_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "job": fake.job(),
            "company": fake.company(),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
        }
        data.append(record)
    return data

# Save data to a CSV file
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Generate and save test data
if __name__ == "__main__":
    num_records = 100  # Number of test records to generate
    test_data = generate_test_data(num_records)
    save_to_csv(test_data, "test_data.csv")
    print(f"{num_records} test records saved to 'test_data.csv'")
    
    
# from faker import Faker

# fake  = Faker()

# print(f'Username - {fake.user_name()}')
# print(f'Name - {fake.name()}')
# print(f'Address - {fake.address()}')
# print(f'Address - {fake.state()}')
# print(f'Username - {fake.country()}')
# print(f'Username - {fake.email()}')
# print(f'Username - {fake.phone_number()}')
# print(f'Username - {fake.date_of_birth(minimum_age=18, maximum_age=90)}')

# # Output:
# '''Username - jaredbrown
# Name - Mr. Thomas Cox
# Address - 3394 Cruz Mountain Suite 907
# South Suzanne, MD 01694
# Address - Alabama
# Username - Isle of Man
# Username - lindsay24@example.org
# Username - 317-530-4734x385
# Username - 1978-01-01'''