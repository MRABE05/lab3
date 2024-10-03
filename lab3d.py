#!/usr/bin/env python3

# Author ID: 120352224

import subprocess

def free_space():
    # Launch the command and capture the output
    result = subprocess.run(
        "df -h | grep '/$' | awk '{print $4}'", 
        shell=True, 
        text=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    )
    
    # Check for errors in command execution
    if result.returncode != 0:
        return 'Error: ' + result.stderr.strip()
    
    # Return the free space, stripping any newline characters
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())
