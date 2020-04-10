# Nornir-Push-Configs
I created this Nornir script to push CCIE workbook files to my lab environment.

## Tools Needed
For this you'll need to have Netbox setup with devices loaded.  You'll also need to have Nornir installed.

## Running the Script
The runbook.py script takes the following command line arguments:
- "-r" or "--role" to specify the device role in Netbox.  Currently it only accepts "router" or "switch"
- "i" or "--initial" to specify the folder of the initial configurations.

## Blogpost & YouTube Video
You can read more about the creation of this script here: https://journey2theccie.wordpress.com/2020/04/10/automating-my-ccie-lab-pt-5-pushing-workbook-configs-with-nornir

You can view the YouTube Video here: https://www.youtube.com/embed/i6Q4n9wEn0I
