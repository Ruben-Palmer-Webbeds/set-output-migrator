#!/bin/bash

# This script is used to migrate all ::set-outputs from the github actions to the convention
# It will discover all yamls or ymls files inside .github of all files from the directory passed as parameter

# Usage: ./migrate-set-output.sh <directory>

# Example: ./migrate-set-output.sh /home/user/my-repo

# check if the parameter was passed
if [ -z "$1" ]
then
  echo "No directory passed as parameter"
  exit 1
fi

# check if the directory exists
if [ ! -d "$1" ]
then
  echo "Directory $1 does not exist"
  exit 1
fi

# discover all yml or yaml files of the directory that are inside .github
files=$(find "$1" -type f -name "*.yml" -o -name "*.yaml" | grep ".github")

for file in $files
do
    python3 setOutputDeprecation.py -d -p "$file"
done

