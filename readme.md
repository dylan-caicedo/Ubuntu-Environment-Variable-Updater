# Ubuntu Environment Variable Updater

**Ubuntu Environment Variable Updater** is an out of box solution to update or create persistent environment variables (System-wide) persisted in bash files (.sh) using the console.

## Installation
Use the latest ubuntu library for this project.

## Usage
Before start using this project, please make sure you have correctly set the following environment variables and they are avaible in your console.

- ENV_FILE_PATH: must be the absolute path of the desired env file (.sh) to be updated. Please make sure the process has read and write permissions when running the project.
---
To run the project:
`py update-env.py var="{var}" value="{value}"`

The parameters are as following:
- var: this is the environment variable name you want to update (or create)
- value: this is the environment variable value you want to set.

Feel free to use the python interpreter you have at hand. For this example, py is been used.

When no environment variable is found, it is created and the given value is assigned.

## References
[Ubuntu Environment Variables](https://help.ubuntu.com/community/EnvironmentVariables)
