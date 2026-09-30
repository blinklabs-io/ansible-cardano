cardano_db_sync
=========

This role deploys a Cardano DB Sync instance.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

The role exposes the following variables:

* `cardano_db_sync_install_method`: installation method; defaults to `docker`.
* `cardano_db_sync_version`: Cardano DB Sync image version; defaults to
  `13.6.0.5`.
* `cardano_node_dir`: base directory for Cardano node data; defaults to
  `/opt/cardano`.
* `cardano_db_sync_state_dir`: host directory for DB Sync state; defaults to
  `{{ cardano_node_dir }}/dbsync-state`.
* `cardano_db_sync_state_container_dir`: container directory for DB Sync state;
  defaults to `/var/lib/cexplorer`.
* `cardano_node_ipc_dir`: host directory containing the node socket; defaults to
  `{{ cardano_node_dir }}/ipc`.
* `cardano_db_sync_ipc_container_dir`: container directory for the node socket;
  defaults to `/node-ipc`.
* `cardano_node_user`: owner for created files and directories; defaults to
  `root`.
* `cardano_node_group`: group for created files and directories; defaults to
  `root`.
* `cardano_db_sync_docker_image`: Docker image to run; defaults to
  `ghcr.io/blinklabs-io/cardano-db-sync:{{ cardano_db_sync_version }}`.
* `cardano_db_sync_docker_container_name`: Docker container name; defaults to
  `cardano-db-sync`.
* `cardano_db_sync_metrics_container_port`: metrics port inside the container;
  defaults to `8080`.
* `cardano_db_sync_metrics_port`: metrics port exposed on the host; defaults to
  `{{ cardano_db_sync_metrics_container_port }}`.
* `cardano_db_sync_network`: Cardano network name; defaults to `mainnet`.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      tasks:
        - include_role:
            name: blinklabs.cardano.cardano_db_sync

License
-------

Apache 2.0

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
