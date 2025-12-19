import json
import requests
from config import PIHOLE_ADDR, PIHOLE_API_TOKEN

sid = ""
csrf = ""

# Set Functions

def auth():
    # Set up auth variables
    auth_url = f"https://{PIHOLE_ADDR}/api/auth"
    api_key = {"password": PIHOLE_API_TOKEN}
    auth_response = requests.post(auth_url, json=api_key, verify=False)

    # Parse the JSON response
    auth_data = auth_response.json()

    # Uncomment next line to see the auth output
    # print(auth_data)

    # Extract the sid
    global sid
    global csrf
    sid = auth_data["session"]["sid"]
    csrf = auth_data["session"]["csrf"]

def output_table(data):
        data = data.json()
        print(f"{'Domain':<50} {'Count':>10}")
        print("-" * 60)
        for item in data["domains"]:
            print(f"{item['domain']:<50} {item['count']:>10}")

def top_domains():
    global sid
    global csrf
    top_domains_url = f"https://{PIHOLE_ADDR}/api/stats/top_domains"
    headers = {
        "X-FTL-SID": sid,
        "X-FTL-CSRF": csrf
    }
    top_domains = requests.request("GET", top_domains_url, headers=headers, verify=False)
    print(top_domains.json())

    output_table(top_domains)

def show_menu():
    """Display the menu options to the user"""
    print(f"\n=== Connected to: https://{PIHOLE_ADDR} ===")
    print("1. List Top Domains")
#    print("2. Add task")
#    print("3. Remove task")
#    print("4. Toggle completed")
#    print("5. Save list")
#    print("6. Load list")
#    print("7. Quit")

# Main program starts here
def main():
    
    auth()  # Authenticate once at startup

    while True:
        show_menu()
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            top_domains()
#        elif choice == "2":
#            add_task(tasks)
#        elif choice == "3":
#            remove_task(tasks)
#        elif choice == "4":
#            toggle_task(tasks)
#        elif choice == "5":
#            save_list(tasks)
#        elif choice == "6":
#            load_list(tasks)
#        elif choice == "7":
#            print("Goodbye!")
#            break
        else:
            print("Invalid choice!")

# This runs the program
if __name__ == "__main__":
    main()