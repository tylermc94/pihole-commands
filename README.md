# pihole-commands

Requires requests library

Tool to access pihole instance to get various metrics and access certain controls. 

Requires a config.py file with the following:

PIHOLE_ADDR = "http://pi.hole" #Can also be the IP of Pihole, can also use https:// if your instance supports it.

PIHOLE_API_TOKEN = "APP PASSWORD"

## Current Features

### List Top Domains
Lists out the top domains by query count.

### List Top Clients
Lists the most active client devices on the network.

### List Top Blocked Domains
Lists the 10 most frequently blocked domains by query count.

### Add Domain
Allows the user to add domains to the allow or deny lists.

### Pause Blocking
Allows the user to pause DNS blocking for a certain amount of time. A list of common timer values is provided, along with an indefinite option and a custom option. Custom allows the user to enter a time in minutes for the pause to last.

### Pi-Hole Status
Prints a list of relevant metrics.

## Future Goals

### Hardware Controls
I would like to be able to run this on a pi and have a set of push buttons to trigger the different functions and display them on a small screen. This way, the entire thing is self contained and accessible to anyone who can physically get to it. Makes it easier for family members to pause blocking if they encounter issues

### Recently Blocked Domains
A menu to list the 20 recently blocked domains, and an option to select one and automatically whitelist it. 

### Request Auth Key on First Run
If config.py does not exist, or does not contain the API key, the program should prompt the user for their API key and pihole address and add them to the config file.
