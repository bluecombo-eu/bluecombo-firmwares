import json
import os
import hashlib

"""
This script reads the JSON file containing the of firmwares.
For each firmware file, it calculates the file size and the MD5 hash.
It then updates the JSON file with the calculated values.

Usage:
python update_size_hash.py
"""

def get_file_size(file_path):
  return os.path.getsize(file_path)

def get_file_hash(file_path):
  with open(file_path, 'rb') as f:
    bytes = f.read()
    return hashlib.md5(bytes).hexdigest()

with open('../firmwares.json', 'r+') as file:
  data = json.load(file)
  for device in data['devices']:
    for firmware in device['firmwares']:
      file_path = '..' + firmware['path']
      firmware['size'] = get_file_size(file_path)
      firmware['md5'] = get_file_hash(file_path)
  file.seek(0)
  json.dump(data, file, indent=4)
  file.truncate()