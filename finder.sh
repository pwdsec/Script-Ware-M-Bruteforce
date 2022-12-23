#!/bin/bash

# Check if asar is installed
if ! [ -x "$(command -v asar)" ]
then
  # If asar is not installed, install it
  npm install -g asar
fi

# Unpack the asar file
npx asar extract /Applications/Script-Ware.app/Contents/Resources/update.asar /Applications/Script-Ware.app/Contents/Resources/update

# Navigate to the output directory
cd /Applications/Script-Ware.app/Contents/Resources/update

# If the file is found, print its path
if [ $? -eq 0 ]
then
  echo "SW-Auth file found at:"
  echo $(find . -name "SWMAuth2")
else
  echo "SW-Auth file not found"
fi
