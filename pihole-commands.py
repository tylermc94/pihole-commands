import json
import requests # pyright: ignore[reportMissingModuleSource]
from config import PIHOLE_ADDR, PIHOLE_API_TOKEN
import urllib3
#disable tls warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sid = ""
csrf = ""

# Set Functions

def auth(): #Authenticate to pihole and return sid and csrf tokens
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


def output_table(data, data_key, col1_header, col1_key, col2_header="Count", col2_key="count"): # Format json output as table
    data = data.json()
    print(f"{col1_header:<50} {col2_header:>10}")
    print("-" * 60)
    for item in data[data_key]:
        print(f"{item[col1_key]:<50} {item[col2_key]:>10}")

def top_domains():
    global sid
    global csrf
    top_domains_url = f"https://{PIHOLE_ADDR}/api/stats/top_domains"
    headers = {
        "X-FTL-SID": sid,
        "X-FTL-CSRF": csrf
    }
    top_domains = requests.request("GET", top_domains_url, headers=headers, verify=False)

    output_table(top_domains, "domains", "Domain", "domain")

def top_blocked_domains():
    global sid
    global csrf
    top_domains_url = f"https://{PIHOLE_ADDR}/api/stats/top_domains"
    params = {
        "Blocked": True
    }
    headers = {
        "X-FTL-SID": sid,
        "X-FTL-CSRF": csrf
    }
    top_blocked_domains = requests.request("GET", top_domains_url, params=params, headers=headers, verify=False)

    output_table(top_blocked_domains, "domains", "Domain", "domain")


def top_clients():
    global sid
    global csrf
    top_clients_url = f"https://{PIHOLE_ADDR}/api/stats/top_clients"
    headers = {
        "X-FTL-SID": sid,
        "X-FTL-CSRF": csrf
    }
    top_clients = requests.request("GET", top_clients_url, headers=headers, verify=False)

    output_table(top_clients, "clients", "Client Name", "name")

def add_domain():
    global sid
    global csrf
    #Create API endpoint URL, requires the type of add
    print("\nWhat type of domain would you like to add?")
    print("1. Whitelist")
    print("2. Blacklist")
    domain_type_choice = input("\nChoose an option: ")
    if domain_type_choice == "1":
        domain_type = "allow"
    elif domain_type_choice == "2":
        domain_type = "deny"
    else:
        print("Invalid choice!")
    add_domain_url = f"https://{PIHOLE_ADDR}/api/domains/{domain_type}/exact"
    #Get domain to be added
    domain = input("\nDomain to be added:")
    params = {
        "domain": domain,
        "comment": "Added with pihole-commands script",
        "groups": [
            0
        ],
        "enabled": True
    }
    headers = {
        "X-FTL-SID": sid,
        "X-FTL-CSRF": csrf
    }
    #send request
    add_domain_request = requests.request("POST", add_domain_url, json=params, headers=headers, verify=False)
    #confirm success or failure
    if add_domain_request.status_code == 201:
        print(f"\nSuccessfully added {domain} to {domain_type} list!")
    else:
        print(f"\nFailed to add domain. Status code: {add_domain_request.status_code}")
        print(add_domain_request.json())  # Show the error message

def show_menu():
    """Display the menu options to the user"""
    print(f"\n=== Connected to: https://{PIHOLE_ADDR} ===")
    print("1. List Top Domains")
    print("2. List Top Clients")
    print("3. List Top Blocked Domains")
    print("4. Add Domain")
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
        elif choice == "2":
            top_clients()
        elif choice == "3":
            top_blocked_domains()
        elif choice == "4":
            add_domain()
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