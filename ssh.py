import paramiko

# Define SSH connection parameters
hostname = 'your_remote_server_ip'
port = 22  # Default SSH port
username = 'your_username'
password = 'your_password'  # You can also use key-based authentication

# Initialize an SSH client
ssh = paramiko.SSHClient()

# Automatically add the server's host key (this can be insecure, use with caution)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the SSH server
    ssh.connect(hostname, port, username, password)

    # Specify the directory you want to change to
    target_directory = '/path/to/your/target/directory'

    # Execute the 'cd' command remotely to change the directory
    command = f'cd {target_directory} && pwd'  # 'pwd' to print the current working directory
    stdin, stdout, stderr = ssh.exec_command(command)

    # Print the current working directory after changing
    print("Current Working Directory:")
    print(stdout.read().decode())

    # Close the SSH connection
    ssh.close()

except paramiko.AuthenticationException:
    print("Authentication failed")
except paramiko.SSHException as e:
    print("SSH connection failed:", str(e))
except Exception as e:
    print("Error:", str(e))
