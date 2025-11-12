# GenshinSolutionPVT

Author: Suraj Arya (thesurajarya)

## Overview
A small Python utility that fetches user data from a public API and prints users whose city name starts with a specific letter (default: "S"). The script demonstrates straightforward HTTP requests, JSON parsing, filtering logic, and robust error handling using Python's standard library and the `requests` package.

## Features
- Fetches user data from https://jsonplaceholder.typicode.com/users
- Filters users by the first letter of their city
- Clear, human-readable output
- Handles network errors, non-200 responses, and empty results
- Easy to customize (change filter letter, timeout, etc.)

## Requirements
- Python 3.7+
- requests library

## Installation
1. Install dependencies:
    ```bash
    pip install requests
    ```

## Usage
Save the script (for example, `main.py`) and run:
```bash
python main.py
```

To change the starting letter, edit the `start_letter` variable in the script, or pass an argument if you add CLI parsing.

## Example output
```
Name: Samantha
Email: samantha@example.com
City: Seattle
-------------------------
Name: Selina Kyle
Email: selina@example.org
City: San Francisco
-------------------------
```

(Actual names / cities depend on the API response.)

## How it works (theory)
1. The script issues an HTTP GET request to the API endpoint using `requests.get`.
2. It checks the HTTP status code:
    - If code is 200, it attempts to parse the body as JSON.
    - For non-200 responses, it raises or logs an appropriate error.
3. The JSON payload is a list of user objects. For each user:
    - Access the nested `address` → `city` field.
    - Compare the first character of the city (case-insensitive) to the target letter.
    - If it matches, print a concise summary (name, email, city).
4. Error handling:
    - Network and connection errors are caught via `requests.exceptions` (ConnectionError, Timeout, HTTPError).
    - JSON decoding errors are handled, with a useful message if the payload is malformed.
    - If no users match the filter, the script prints a clear notification.

## Tips and customization
- Add a command-line interface (argparse) to accept filter letter, endpoint URL, or timeout.
- Use a timeout in `requests.get(..., timeout=5)` to avoid hanging.
- For production use, add retries (e.g., urllib3 Retry or requests.adapters.HTTPAdapter).
- To persist results, write filtered users to CSV or JSON.

## Troubleshooting
- "Error fetching data from API" — check network, proxy, or endpoint availability.
- No users displayed — the API may not contain cities starting with the chosen letter at the moment.
- If JSON parsing fails, verify the endpoint and inspect the raw response.

## License
This project is provided for educational and demonstration purposes. Use and modify freely.

