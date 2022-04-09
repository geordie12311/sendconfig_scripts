#python script utilising nornir_netmiko plugin
#script will send a set of commands to hosts in the
#nornir host file

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result
#importing netmiko send_config library

nr = InitNornir(config_file="config.yaml")

def send_config_test(task):
    task.run(task=netmiko_send_config, config_commands=("username cisco priv 15 secret Cisco1")
#function is sending the configuration commands to the hosts
results = nr.run(task=send_config_test)
print_result(results)
#setting the object results to output of the send_config_test function
