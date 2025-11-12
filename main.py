import requests

def fetch_users(api_url):
    """Fetches user data from the API, handles HTTP exceptions."""
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        users = response.json()
        if not isinstance(users, list) or not users:
            print("API returned an empty or invalid user list.")
            return []
        return users
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return []

def display_users_from_city_starting_with(users, start_letter='S'):
    """Prints users whose address.city starts with a specific letter."""
    filtered_users = [
        (idx, user)
        for idx, user in enumerate(users, start=1)
        if user.get('address', {}).get('city', '').startswith(start_letter)
    ]

    if not filtered_users:
        print(f"No users found from cities starting with '{start_letter}'.")
        return

    for idx, user in filtered_users:
        name = user.get('name', 'N/A')
        username = user.get('username', 'N/A')
        email = user.get('email', 'N/A')
        city = user.get('address', {}).get('city', 'N/A')
        print(f"User {idx}:")
        print(f"Name: {name}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"City: {city}")
        print('-' * 24)

def main():
    API_URL = "https://jsonplaceholder.typicode.com/users"
    users = fetch_users(API_URL)
    display_users_from_city_starting_with(users, start_letter='S')

if __name__ == "__main__":
    main()
