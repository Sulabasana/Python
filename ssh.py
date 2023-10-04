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

    # Command 1: Check file content
    file_path = '/path/to/your/file.txt'
    check_command = f'cat {file_path}'

    stdin, stdout, stderr = ssh.exec_command(check_command)

    # Read the file content
    file_content = stdout.read().decode().strip()

    # Perform action based on file content
    if "some_condition" in file_content:
        # Command 2: Change directory
        target_directory = '/path/to/your/target/directory'
        change_dir_command = f'cd {target_directory} && pwd'
        stdin, stdout, stderr = ssh.exec_command(change_dir_command)
        print("Current Working Directory:")
        print(stdout.read().decode())

        # Command 3: Execute another command
        command_to_execute = 'ls -l'
        stdin, stdout, stderr = ssh.exec_command(command_to_execute)
        print("Command Output:")
        print(stdout.read().decode())
    else:
        print("File content condition not met")

    # Close the SSH connection
    ssh.close()

except paramiko.AuthenticationException:
    print("Authentication failed")
except paramiko.SSHException as e:
    print("SSH connection failed:", str(e))
except Exception as e:
    print("Error:", str(e))
