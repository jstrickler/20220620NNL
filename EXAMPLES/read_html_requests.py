#!/usr/bin/env python
import requests

response = requests.get("https://navalnuclearlab.energy.gov/")  # <1>

for header, value in sorted(response.headers.items()): # <2>
    print(header, value)
print()

print(response.content[:200].decode())   # <3>
print('...')
print(response.content[-200:].decode())   # <4>
