# Ansible Collection - blinklabs.cardano

Ansible playbooks and roles to install Cardano services of various types. To
start, this will use Docker images for managing and orchestrating the services.

## Usage

This playbook is published to Ansible Galaxy. The best way to consume it is
using normal methods, documented under
[installing collections](https://docs.ansible.com/ansible/latest/collections_guide/collections_installing.html).

Inside this collection are several roles.

- `blinklabs.cardano.adder`
- `blinklabs.cardano.cardano_db_sync`
- `blinklabs.cardano.cardano_node`
- `blinklabs.cardano.cardano_node_api`
- `blinklabs.cardano.dingo`
- `blinklabs.cardano.kupo`
- `blinklabs.cardano.ogmios`
- `blinklabs.cardano.tx_submit_api`

Each role is documented independently under the roles directory.

While not explicitly required as dependencies, we recommend installing Docker
and the `docker` python module using the roles from `geerlingguy` on Galaxy.

```yaml
    - name: nodePlaybook | Include geerlingguy.pip role
      ansible.builtin.include_role:
        name: geerlingguy.pip
        apply:
          tags:
            - pip
      vars:
        pip_install_packages:
          - name: docker
      tags:
        - always

    - name: nodePlaybook | Include geerlingguy.docker role
      ansible.builtin.include_role:
        name: geerlingguy.docker
        apply:
          tags:
            - docker
      vars:
        docker_install_compose: false
        docker_apt_arch: "{{ { 'aarch64': 'arm64', 'x86_64': 'amd64' }[ansible_facts.architecture] }}"
        docker_users: "{{ DOCKER_USERS | default(ansible_user) }}"
        docker_daemon_options:
          log-driver: "local"
      tags:
        - always
```
