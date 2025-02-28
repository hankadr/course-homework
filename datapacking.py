#task1
import pickle
countries = {}

def add_country():
    country = input("Enter country name: ")
    capital = input("Enter capital city: ")
    countries[country] = capital
    print(f"Added: {country} - {capital}")

def delete_country():
    country = input("Enter country to delete: ")
    if country in countries:
        del countries[country]
        print(f"Deleted: {country}")
    else:
        print("Country not found.")

def find_capital():
    country = input("Enter country name to find its capital: ")
    print(f"Capital: {countries.get(country, 'Country not found.')}")

def edit_country():
    country = input("Enter country name to edit: ")
    if country in countries:
        new_capital = input("Enter new capital: ")
        countries[country] = new_capital
        print(f"Updated: {country} - {new_capital}")
    else:
        print("Country not found.")

def save_data(filename="countries.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(countries, file)
    print("Data saved.")

def load_data(filename="countries.pkl"):
    global countries
    try:
        with open(filename, "rb") as file:
            countries = pickle.load(file)
        print("Data loaded.")
    except FileNotFoundError:
        print("No saved data found.")

def menu():
    load_data()  
    while True:
        print("\nMenu:")
        print("1. Add a country and capital")
        print("2. Delete a country")
        print("3. Find a capital")
        print("4. Edit a country’s capital")
        print("5. Save data")
        print("6. Load data")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_country()
        elif choice == "2":
            delete_country()
        elif choice == "3":
            find_capital()
        elif choice == "4":
            edit_country()
        elif choice == "5":
            save_data()
        elif choice == "6":
            load_data()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

menu()

#task2

import pickle
bands = {}

def add_band():
    band = input("Enter band/singer name: ")
    album = input("Enter album name: ")
    bands[band] = album
    print(f"Added: {band} - {album}")

def delete_band():
    band = input("Enter band/singer to delete: ")
    if band in bands:
        del bands[band]
        print(f"Deleted: {band}")
    else:
        print("Band not found.")

def find_album():
    band = input("Enter band/singer name to find album: ")
    print(f"Album: {bands.get(band, 'Band not found.')}")

def edit_band():
    band = input("Enter band/singer name to edit: ")
    if band in bands:
        new_album = input("Enter new album: ")
        bands[band] = new_album
        print(f"Updated: {band} - {new_album}")
    else:
        print("Band not found.")

def save_data(filename="bands.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(bands, file)
    print("Data saved.")

def load_data(filename="bands.pkl"):
    global bands
    try:
        with open(filename, "rb") as file:
            bands = pickle.load(file)
        print("Data loaded.")
    except FileNotFoundError:
        print("No saved data found.")

def menu():
    load_data()  
    while True:
        print("\nMenu:")
        print("1. Add a band and album")
        print("2. Delete a band")
        print("3. Find an album")
        print("4. Edit a band's album")
        print("5. Save data")
        print("6. Load data")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_band()
        elif choice == "2":
            delete_band()
        elif choice == "3":
            find_album()
        elif choice == "4":
            edit_band()
        elif choice == "5":
            save_data()
        elif choice == "6":
            load_data()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

menu()
