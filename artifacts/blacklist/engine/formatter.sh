#!/bin/bash

# Check if Python 3.8+ is installed
python_version=$(python3 --version 2>&1 | awk '{print $2}')
required_version="3.8"

if [[ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" == "$required_version" ]]; then
    echo "Python $required_version or newer is installed"
    
    # Check if pip is installed
    if command -v pip &>/dev/null; then
        echo "pip is installed"
        
        # Check if black is installed
        if pip show black &>/dev/null; then
            echo "black is installed"
        else
            echo "black is not installed, installing..."
            pip install black
        fi
    else
        echo "pip is not installed"
        exit 1; 
    fi
else
    echo "Python $required_version or newer is not installed"
    exit 1; 
fi

# Formatting the files using black 
echo "Formatting Python files using black..."
  for file in $(ls *.py); do
      black "$file"
  done