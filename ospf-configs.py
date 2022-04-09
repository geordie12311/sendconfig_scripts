"""Python script to send ospf config using jinja2 template"""

import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_utils.plugins.functions import print_result

# importing libraries including load_yaml and template_file for jinja2

nr = InitNornir(config_file="config.yaml")
user = input("Please enter your username: ")
password = getpass.getpass()
nr.inventory.defaults.username = user
nr.inventory.defaults.password = password
# initialising nornir with config.yaml config file and prompting for username / password



def load_vars(task):
    loader = task.run(task=load_yaml, file=f"host_vars/{task.host}.yaml")
    task.host["facts"] = loader.result
    push_ospf(task)
# creating a function to load host specific yaml var files and starting the push ospf task which will run after load_vars


def push_ospf(task):
    template = task.run(task=template_file, template="ospf.j2", path="templates")
    task.host["ospf_config"] = template.result
    rendered = task.host["ospf_config"]
    configuration = rendered.splitlines()
    task.run(task=send_configs, configs=configuration)
    # creating a function to load the jinja2 template file held in the templates folder and render it in the ospf config


results = nr.run(task=load_vars)
print_result(results)
# running the load_vars function which will then run push_ospf function afterwards and printing the results
