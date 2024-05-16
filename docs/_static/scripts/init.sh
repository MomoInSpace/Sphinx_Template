#!/bin/bash


# Directory to search for .tex files in
dir="./source/"

# Find all .tex files and touch them
find "$dir" -type f -name "*.tex" -exec touch {} \;

# Find all .tex files and touch them
find "$dir" -type f -name "*.rst" -exec touch {} \;
