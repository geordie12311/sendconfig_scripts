import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result
#importing send_configs_from_file from nornir_scrapli to send configuration commands from a file
nr = InitNornir(config_file="config.yaml")
#The above line is telling nornir where the config file is located
password = getpass.getpass()
nr.inventory.defaults.password = password

def send_configs(task):
    task.run(task=send_configs_from_file, file="config_test.txt")
#above function is going to use the send_configs to send configuration commands from a file

results = nr.run(task=send_configs)
#above line is setting an object results that is aligned to the task output
print_result(results)
