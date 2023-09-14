# youtous/ansible-limit-hosts-strategy-plugin

[![GitHub Repo stars](https://img.shields.io/github/stars/youtous/ansible-limit-hosts-strategy-plugin?label=✨%20youtous%2Fansible-limit-hosts-strategy-plugin&style=social)](https://github.com/youtous/ansible-limit-hosts-strategy-plugin/)
[![Gitlab Repo](https://img.shields.io/badge/gitlab.com%2Fyoutous%2Fansible--minisign?label=✨%20youtous%2Fansible-limit-hosts-strategy-plugin&style=social&logo=gitlab)](https://gitlab.com/youtous/ansible-limit-hosts-strategy-plugin/)
[![Licence](https://img.shields.io/github/license/youtous/ansible-limit-hosts-strategy-plugin)](https://github.com/youtous/ansible-limit-hosts-strategy-plugin/blob/master/LICENSE)


This repository shows an example of a limit strategy on ansible that blocks the execution of the playbook if the number of hosts is over a maximum allowed capacity.

## Notes

* This kind of plugin can be used in AWX/AAP. You can either control the list of strategy plugins using the default `ansible.cfg` or environment variables.
* In a real usage scenario, anyone can override the limit by providing their own strategy plugin. Consider this example as a **safeguard** but not as an enforcement.
* Since the documentation of the plugin is statically parsed, you would need to manually copy the original one from the `DOCUMENTATION` variable.

## Usage

- List the strategy plugins: `ansible-doc -t strategy -l `
- Run the example playbook: `ansible-playbook -i inventory.ini  test_playbook.yml`

### Output

```text
╰─λ ansible-playbook -i inventory.ini  test_playbook.yml                                                                                 0 < 08:43:05

PLAY [Test Playbook] ********************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************************
ok: [localhost5]
ok: [localhost1]
ok: [localhost4]
ok: [localhost2]
ok: [localhost3]
ok: [localhost6]
ok: [localhost7]
ok: [localhost9]
ok: [localhost8]
ok: [localhost10]

TASK [Dynamically add new hosts] **************************************************************************************************************
changed: [localhost1] => (item=11)
changed: [localhost1] => (item=12)
changed: [localhost1] => (item=13)
changed: [localhost1] => (item=14)
changed: [localhost1] => (item=15)
changed: [localhost1] => (item=16)
changed: [localhost1] => (item=17)
changed: [localhost1] => (item=18)
changed: [localhost1] => (item=19)
changed: [localhost1] => (item=20)
changed: [localhost1] => (item=21)

TASK [Show a message] **************************************************************************************************************************
ok: [localhost1] => {
    "msg": "This is a test message"
}
ok: [localhost2] => {
    "msg": "This is a test message"
}
ok: [localhost3] => {
    "msg": "This is a test message"
}
ok: [localhost4] => {
    "msg": "This is a test message"
}
ok: [localhost5] => {
    "msg": "This is a test message"
}
ok: [localhost6] => {
    "msg": "This is a test message"
}
ok: [localhost7] => {
    "msg": "This is a test message"
}
ok: [localhost8] => {
    "msg": "This is a test message"
}
ok: [localhost9] => {
    "msg": "This is a test message"
}
ok: [localhost10] => {
    "msg": "This is a test message"
}

PLAY [New step] *******************************************************************************************************************************
ERROR! Too many hosts in this playbook count_hosts=21, max_hosts=10
```


## LICENSE

MIT