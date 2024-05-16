#!/bin/bash

# Usage: ./remove_regex.sh regex_pattern file_path

if [ $# -ne 3 ]; then
  echo "Usage: $0 regex_pattern file_path"
  exit 1
fi

regex_pattern=$1
replace_string=$2
file_path=$3

# Checking if the file exists
if [ ! -f "$file_path" ]; then
  echo "$file_path does not exist."
  exit 1
fi

# Backup the file
cp "$file_path" "$file_path.bak"

# Removing lines matching the given regex pattern
sed -i "s/$regex_pattern/$replace_string/g" "$file_path"

echo "Lines matching '$regex_pattern' have been removed from $file_path."
echo "A backup of the original file has been created: $file_path.bak"
