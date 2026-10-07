# dingo

Deploy Dingo in Docker with persistent database and IPC directories. This role
installs chrony when `chrony_enabled` is true.

## Runtime configuration

| Variable | Default | Purpose |
| --- | --- | --- |
| `dingo_version` | `0.20.0` | Image tag; architecture suffixes can be included. |
| `dingo_network` | `mainnet` | Cardano network; selects the default network-config and topology paths. |
| `dingo_docker_image` | `ghcr.io/blinklabs-io/dingo:{{ dingo_version }}` | Full image reference. |
| `dingo_command` | `[]` | Container command as an argument list; empty uses the image default. |
| `dingo_docker_extra_ports` | `[]` | Additional Docker port mappings, such as `6001:3002`. |
| `dingo_extra_env` | `{}` | Environment overrides merged over the role's environment. Values must be strings. |
| `dingo_port` / `dingo_container_port` | `3001` / `3001` | Published host port and Dingo's listening port. |
| `dingo_db_dir` / `dingo_db_container_dir` | `{{ dingo_dir }}/data` / same | Host and container database paths. |
| `dingo_ipc_dir` / `dingo_ipc_container_dir` | `{{ dingo_dir }}/ipc` / same | Host and container socket directories. |
| `dingo_socket_name` | `node.socket` | Socket filename inside the IPC directory. |
| `dingo_user` / `dingo_group` | `root` / `root` | Ownership of managed directories and configuration. Match the image's runtime UID/GID. |
| `dingo_restore_snapshot` | `true` | Enable first-run Mithril bootstrap; false sets an empty `RESTORE_SNAPSHOT`. |

## Configuration files

Cardano's network configuration and Dingo's YAML configuration are separate.
`dingo_config_file` points to the network config inside the container. Set
`dingo_manage_config: true` and `dingo_config_host_file` to mount an existing
host network-config file read-only. The default host path equals the container
path; the role does not generate this file or its genesis siblings.

To generate and mount Dingo YAML, set `dingo_manage_node_config: true` and
provide `dingo_node_config` as a mapping. The role writes it to
`dingo_node_config_file` (default `{{ dingo_config_dir }}/dingo.yaml`) and mounts
it read-only at `dingo_node_config_container_file` (default
`/etc/dingo/dingo.yaml`). Do not include signing-key contents in this mapping.
Configuration changes restart the container; unchanged configuration does not.

## Topology

Set `dingo_manage_topology: true` to generate a topology. The host destination
is `dingo_topology_host_file`; `dingo_topology_file` is the read-only container
path. Both default to `{{ dingo_config_dir }}/{{ dingo_network }}/topology.json`,
or `/opt/cardano/config/mainnet/topology.json` with the default directories and
network.

`dingo_topology` must be a mapping containing a complete topology object,
including grouped local roots, trust settings, valencies, and empty public roots.
An empty mapping uses
the legacy `dingo_topology_bootstrap_peers`, `dingo_topology_localroots`,
`dingo_topology_publicroots`, and `dingo_topology_use_ledger_after_slot` variables.
A topology change restarts the container.

## Block production

Set `dingo_block_producer: true` and point `dingo_keys_dir` at the existing hot-key
and operational-certificate directory. It is mounted read-only at
`dingo_keys_container_dir`. The role supplies `dingo_shelley_kes_key`,
`dingo_shelley_opcert`, and `dingo_shelley_vrf_key` as paths inside that mount;
it does not generate or copy keys. Cold signing keys must stay outside the
managed host.

## Example

```yaml
- hosts: servers
  roles:
    - role: blinklabs.cardano.dingo
      dingo_version: '0.78.0'
      dingo_network: preview
      dingo_port: 6000
      dingo_container_port: 3001
      dingo_command:
        - serve
        - --genesis-bootstrap-enabled=false
        - --chainsync-strategy=round-robin
```

## License

Apache-2.0
