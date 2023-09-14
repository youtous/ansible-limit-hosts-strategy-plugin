# limit_hosts.py

from ansible.plugins.strategy import StrategyBase


DOCUMENTATION = '''
    name: limit_hosts
    short_description: Limit hosts to a maximum number
    description:
        - Limit hosts to a maximum number
        - in the real documentation you would like to extend the real documentation from strategy.linear
    author: youtous
'''

# extending original doc
#
# from ansible.plugins.strategy.linear import DOCUMENTATION as PARENT_DOCUMENTATION
# DOCUMENTATION = PARENT_DOCUMENTATION

from ansible.utils.display import Display
from ansible.errors import AnsibleError

display = Display()
from ansible.plugins.strategy.linear import StrategyModule as StrategyLinear

class StrategyModule(StrategyLinear):
    def __init__(self, *args, **kwargs):
        super(StrategyModule, self).__init__(*args, **kwargs)
        self.max_hosts = 10

        max_hosts = self.get_max_hosts()
        count_hosts = len(self._tqm._inventory.get_hosts())
        if count_hosts > max_hosts:
            raise AnsibleError(f"Too many hosts in this playbook count_hosts={count_hosts}, max_hosts={max_hosts}")


    def get_max_hosts(self):
        return self.max_hosts

