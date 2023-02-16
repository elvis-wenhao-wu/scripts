# `OpenSSH`

## Set up

- Server
    - Package: `openssh-server`
    - Config: `/etc/ssh/sshd_config` (system wide) & `/etc/ssh/sshd_config.d/*.conf`
- Client
    - Package: `openssh-client` & `ssh`
    - Config: `/etc/ssh/ssh_config` (system wide) & `~/.ssh/config` (user wide)

## Configuration

- Use different port other than 22
    - Replicate system wide config `/etc/ssh/sshd_config` into a newly created user config `/etc/ssh/sshd_config.d/sshd.conf` and uncomment the port config there
- 

## Authentication/Authorization

- Client Authentication: Password or Public-key

    - Password Authentication

        - Client authenticates itself to the server: `ssh user@host`

    - Public-Key Authentication

        - Produce Public/Private key pair: 

            ```
            ssh-keygen -t ecdsa -b 521
            ```

            - Note that the key itself does not follow any PCKS format but has its own spec (see reference below)
            - Key fingerprint reproduce: `ssh-keygen -lf ~/.ssh/id_ecdsa.pub` ([What is a SSH key fingerprint and how is it generated?](https://superuser.com/questions/421997/what-is-a-ssh-key-fingerprint-and-how-is-it-generated))

        - Copy paste the public key content into the server authorized key file: `~/.ssh/authorized_keys` (manually) or `ssh-copy-id -i ~/.ssh/id_ecdsa.pub user@host` (shell command)

        - Client can log in the server by: `ssh -i ~/.ssh/private_key user@host`

    - Public-Key Authentication (through agent forwarding in a weired way)

        - Start SSH Agent at login: `eval `ssh-agent`` (Pay attention to the subshell relationship in Bash and why we better do this in a parent shell before `tmux` gets involved)

        - Add private key to the agent so that the agent can perform the authentication for you: `ssh-add ~/.ssh/id_rsa` (check if the private key has been added successfully by listing the private keys held by the agent: `ssh-add -l`)

        - Modify client config: `~/.ssh/config` (sample pasted below)

            ```bash
            Host <hostlabel>
                HostName <ipaddr>
                User <username>
                Port <port>
                IdentityFile <publickeyfile> # to bypass passphrase (should be private key in normal way)
                IdentitiesOnly yes
            ```

        - Usage: `ssh <hostlabel>` (Note that in this way, you do not need to type password to access the server however you do need to re-add the private key to the agent when each terminal session closes. In this way you somewhat protects the server from being accessed by others when the client is compromised)

- Server Authorization

    - Config file: `/etc/sshd_config`

- Server Authentication

    - Known host mechanism
        - On the first time when you connect into the remote machine, the remote machine will copy its public key onto the client `~/.ssh/known_hosts` to identify itself, protecting the client against future MitM attack. “If the server isn’t already known and trusted, ssh prompts the user to confirm the server by presenting a hash of the server’s public key called the key fingerprint” - Unix and Linux System Administration Handbook 5ed
        - Host keys are just ordinary SSH key pairs. Each host can have one host key for each algorithm, e.g. `/etc/ssh/ssh_host_rsa_key`. The host keys are usually automatically generated when an SSH server is installed. They can be regenerated at any time. - [ssh academy](https://www.ssh.com/academy/ssh/keygen#creating-an-ssh-key-pair-for-user-authentication)

## Usage

- Remote shell:
    - Password auth: `ssh user@host` (different port `ssh user@host -p 2022`)
    - Key auth: `ssh -i ~/.ssh/private_key user@host`
- Local Port forwarding:
    - Case 1 Jupyter Notebook:
        - Open a remote application on the server side: `jupyter notebook --no-browser --port=8888` (jupyter notebook opened at port 8888 headlessly)
        - Perform port forwarding on the client side: `ssh -fNTL 8000:localhost:8888 user@host` (`-f` means “Requests ssh to go to background just before command execution….(when) if ssh is going to ask for passwords or passphrases” while `-N` means “Do not execute a remote command. This is useful for just forwarding ports.” `-T` ”Disable pseudo-terminal allocation” in case any control characters are intercepted and interpreted by the remote shell and `-L` means “listen to either a TCP port on the local side” - `ssh` man page)
        - Access remote application on the client side: Open a browser and enter `localhost:8000` to access jupyter notebook on the server side
    - Case 2 PostgreSQL:
        - Open a remote application on the server side: turn on postgres functionality
        - Perform port forwarding on the client side: `ssh -fNTL 5433:127.0.0.1:5432 user@host`
        - Access remote application on the client side: `psql -h 127.0.0.1 -p 5433 -d postgres -U postgres`
- Remote Port Forwarding
- Dynamic Port Forwarding (see reference below)
    - Allocate a socket to listen to localhost: `ssh -fNT -D127.0.0.1:9001 user@host`
    - Configure Firefox:
        - Turn on `Manual proxy configuration`
        - Enter `127.0.0.1` in `SOCKS Host` and `9001` in `Port` and use `SOCKS v5`
        - Turn on `Proxy DNS when using SOCKS v5`

## Reference

- SSH The Secure Shell The Definitive Guide
- Unix and Linux System Administration Handbook 5ed
- [What are the differences between ssh generated keys(ssh-keygen) and OpenSSL keys (PEM)and what is more secure for ssh remote login?](https://security.stackexchange.com/questions/29876/what-are-the-differences-between-ssh-generated-keysssh-keygen-and-openssl-keys)
- [Generating private+public keypair for SSH: difference between ssh-keygen and openssl?](https://superuser.com/questions/1535116/generating-privatepublic-keypair-for-ssh-difference-between-ssh-keygen-and-ope)
- [The OpenSSH Private Key Format](https://coolaj86.com/articles/the-openssh-private-key-format/) & its [Github file explanation](https://github.com/openssh/openssh-portable/blob/2dc328023f60212cd29504fc05d849133ae47355/PROTOCOL.key)
- [Why use `-T` with `ssh`](https://stackoverflow.com/questions/42505339/why-use-t-with-ssh)
- [SSH Tunnel - Local, Remote and Dynamic Port Forwarding](https://blog.jakuba.net/ssh-tunnel---local-remote-and-dynamic-port-forwarding/)