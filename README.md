# pihole-commands

Requires requests library

Tool to access pihole instance to get various metrics and access certain controls. 

Requires a config.py file with the following:

PIHOLE_ADDR = "pi.hole" #Can also be the IP of Pihole

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