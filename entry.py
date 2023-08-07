import json
import time

def create_json_object():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    arrival_time = time.strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "name": name,
        "email": email,
        "arrival_time": arrival_time
    }

    return data

def save_json_object(data):
    try:
        with open("data.json", "r") as file:
            entries = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        entries = []

    entries.append(data)

    with open("data.json", "w") as file:
        json.dump(entries, file, indent=4)

def main():
    print("Welcome to Entry Object Creator!")
    while True:
        data = create_json_object()
        save_json_object(data)
        print("Entry object created and saved.")

        choice = input("Do you want to create another Entry object? (yes/no): ").lower()
        if choice != 'yes':
            break

    print("Thank you for using Entry Object Creator!")

if __name__ == "__main__":
    main()
