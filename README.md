# practice_task
# H&S Hotel Management System

## Overview
The H&S Hotel Management System is a Python-based program designed to manage customer records for a hotel. It handles various tasks such as booking rooms, ordering food, booking gaming activities, generating bills, and managing customer records.

## Technologies Used
- Python
- `pickle` library for serialization
- `os` library for file operations

## Features
- **Create Records:** Allows users to input and save customer details, room bookings, food orders, and gaming activities. The total bill is computed and stored.
- **Search Records:** Enables searching for customer records by phone number.
- **Delete Records:** Provides functionality to delete customer records based on phone number.
- **Update Records:** Allows updating existing customer details and booking preferences.
- **Display All Records:** Displays all stored customer records.
- **Append Records:** Adds new records to the existing dataset.

## Usage
1. **Create Records** (`Option A`): Enter customer details, book rooms, order food, and select gaming activities. The total bill is calculated and saved.
2. **Search Records** (`Option B`): Search for a customer’s record using their phone number.
3. **Delete Records** (`Option C`): Remove a customer’s record by phone number.
4. **Update Records** (`Option D`): Modify existing customer details or booking information.
5. **Display All Records** (`Option E`): View all customer records stored in the system.
6. **Append Records** (`Option F`): Add new records to the existing data.
7. **Return to Main Menu** (`Option G`): Go back to the main menu.

## Code Structure

- **`createfile()`**: Prompts user to enter customer details and saves them in a file using `pickle`.
- **`cuisine()`**: Handles food orders and calculates the bill.
- **`games()`**: Manages gaming activities and computes the associated costs.
- **`room()`**: Manages room bookings and calculates the rent.
- **`billing_details()`**: Computes the total bill based on room rent, food, and gaming expenses.
- **`append_rec()`**: Adds new customer records to the file.
- **`delete_rec()`**: Deletes a customer record based on phone number.
- **`updatefile()`**: Updates existing customer details.
- **`search_rec()`**: Searches and displays customer records based on phone number.
- **`displayfile()`**: Displays all customer records in the file.

