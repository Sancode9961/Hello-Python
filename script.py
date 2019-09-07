import sys

import requests

print(sys.version)
print(sys.executable)


def great(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(great("world"))
print(great("Sandeep"))

r = requests.get("https://google.com")
print(r.status_code)
print(r.ok)

# shift+alt+f to format document

# for virtial environment>>pip -m venv venv  >>even/Scripts/activate
# get-executionpolicy
# Set-ExecutionPolicy RemoteSigned
# Restricted – No scripts can be run.
# AllSigned – Only scripts signed by a trusted publisher can be run.
# RemoteSigned – Downloaded scripts must be signed by a trusted publisher.
# Unrestricted – All Windows PowerShell scripts can be run.
# You Should Also Know:

# sort imports, linting,default settings,default keyboard shortcuts  >>ctl+shift+p

