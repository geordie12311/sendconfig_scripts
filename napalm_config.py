import getpass
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_configure

nr = InitNornir(config_file="config1.yaml")
password = getpass.getpass()
nr.inventory.defaults.password = password

def push_scp(task):
    task.run(task=napalm_configure, configuration="banner motd % THIS IS A TEST BANNER FOR SELBY DEVCIES ONLY, UNAUTHORISED USERS WILL BE SHOT!!! %")

results = nr.run(task=push_scp)
print_result(results)
