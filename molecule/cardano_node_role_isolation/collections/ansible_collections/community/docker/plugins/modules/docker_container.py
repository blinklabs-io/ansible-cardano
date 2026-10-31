#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec={
            "command": {"type": "list", "elements": "str"},
            "image": {"type": "str", "required": True},
            "name": {"type": "str", "required": True},
            "env": {"type": "dict"},
            "ports": {"type": "list", "elements": "str"},
            "restart_policy": {"type": "str"},
            "stop_timeout": {"type": "int"},
            "volumes": {"type": "list", "elements": "str"},
        },
        supports_check_mode=True,
    )
    module.exit_json(changed=False)


if __name__ == "__main__":
    main()
