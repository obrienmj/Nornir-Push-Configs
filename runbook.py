#!/usr/bin/python3
# Created by Michael O'Brien
# Used to push workbook configs to lab devices

#Import plugins
from nornir import InitNornir
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_title, print_result
import argparse
import logging

#Initialize Nornir and Set filters
nr = InitNornir(config_file="config.yaml")
switches = nr.filter(role="switch")
routers = nr.filter(role="router")

#Create Command Line Arguments
parser = argparse.ArgumentParser(description='Push configs to Devices.')
parser.add_argument('--role', '-r', help='Choose router or switch')
parser.add_argument('--initial','-i',help='Name of initial configs')
args = parser.parse_args()

#Create Task function
def push_configs(task):
    config_file = f"configs/{args.initial}/{task.host.name}.txt"
    task.run(task=networking.napalm_configure,
            replace=False,
            filename=config_file,
            severity_level=logging.INFO
            )

#Prompt for creds then assign them to devices
username = input("Enter Username: ")
password = input("Enter Password: ")
nr.inventory.defaults.username = username
nr.inventory.defaults.password = password

#Run tasks against inventory groups
if args.role == 'switch':
    result = switches.run(task=push_configs)
    print_result(result)
elif args.role == 'router':
    result = routers.run(task=push_configs)
    print_result(result)
else:
    print("Undefined role.  Please enter 'router' or 'switch'")



