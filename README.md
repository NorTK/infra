# NorTK Infrastructure

NorTK Infrastructure Management and Automation.

## Repository Management

This project includes an Ansible playbook to automate the creation and configuration of local RPM repositories for **Linux Enterprise by NorTK**.

### Prerequisites

- A RHEL, CentOS Stream, or Fedora-based server.
- Ansible installed on the control node.
- SSH access to the target host.

### Usage

1.  **Configure Variables:**
    Copy the example variables file and edit it to define your repositories:
    ```bash
    cp ansible/repos/vars/main.yaml.example ansible/repos/vars/main.yaml
    vi ansible/repos/vars/main.yaml
    ```

2.  **Run the Playbook:**
    Execute the playbook using the provided inventory:
    ```bash
    ansible-playbook -i ansible/repos/inventory ansible/repos/create_repo.yaml
    ```

### What the Playbook Does

- **Infrastructure:** Installs Nginx, `createrepo_c`, and `rpm-build`.
- **Directory Setup:** Creates the repository structure defined in `repo_base`.
- **Nginx Configuration:** Configures a virtual host to serve the repositories via HTTP.
- **Security:** Configures Firewalld and SELinux contexts for web serving.
- **Release Packages:** Builds and deploys `len-<short_name>-release` RPM packages for each repository. These packages allow clients to easily configure the repositories.
- **Update Script:** Generates a dynamic `update_repos.sh` script in the `repo_base` directory for manual metadata updates.

### Repository Configuration

Repositories are defined in the `repositories` list within `vars/main.yaml`:

```yaml
repositories:
  - name: "Linux Enterprise by NorTK OS Repository"
    short_name: "os"
    version: "0.1"
  - name: "Linux Enterprise by NorTK ERP Repository"
    short_name: "erp"
    version: "0.1"
```

Each repository will be served at `http://<repo_fqdn>/<short_name>/`.
