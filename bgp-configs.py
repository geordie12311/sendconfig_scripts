"""Python script to generate bgp
configuration from jinja2 template"""

import getpass
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_utils.plugins.functions import print_result


"""Initialising nornir and using getpass to prompt for password"""

nr = InitNornir(config_file="config.yaml")
password = getpass.getpass()
nr.inventory.defaults.password = password


"""Loading the host var files into memory"""

def load_vars(task):
    loader = task.run(task=load_yaml, file=f"host_vars/{task.host}.yaml")
    task.host["facts"] = loader.result
    push_bgp(task)


"""Generating the bgp configuration using jinja2 template"""

def push_bgp(task):
    template = task.run(task=template_file, template="bgp.j2", path="templates")
    task.host["bgp_config"] = template.result
    rendered = task.host["bgp_config"]
    configuration = rendered.splitlines()
    task.run(task=send_configs, configs=configuration)


results = nr.run(task=load_vars)
print_result(results)
