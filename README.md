# GenshinSolutionPVT
Author: Suraj Arya (thesurajarya)

This Python script retrieves user information from a public API and prints details for users whose city names start with the letter 'S'. It demonstrates robust error handling and clean output formatting using only the standard library and the requests library.

Requirements
Python 3.7 or higher

requests library

Install the requests library (if not already installed) using:

text
pip install requests
How to Run
Save the script (for example, as filter_users.py).

Open a terminal and navigate to the directory containing filter_users.py.

Run the script using:

text
python filter_users.py
The script will:

Fetch users from https://jsonplaceholder.typicode.com/users

Print only those whose city starts with S

Handle any API errors and notify you if there are no matching users or connection issues

Troubleshooting
If you see Error fetching data from API, check your network connection or try again later.

If no users are displayed, the API might not have any users whose city starts with 'S' at the time.

Customization
You can change the starting letter by modifying the start_letter value in the script.

License
This project is for educational and demonstration purposes.
