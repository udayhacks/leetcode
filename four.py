import os
import subprocess

# Function to execute a command and return the result
def execute_command(command):
    try:
        # Execute the command and capture the output
        result = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
        return result.strip()
    except subprocess.CalledProcessError as e:
        # Return the error message
        return e.output.strip()

# Example usage:
# List all processes
print(execute_command('tasklist'))

# Get system information
print(execute_command('systeminfo'))

# Get network configuration
print(execute_command('ipconfig /all'))
