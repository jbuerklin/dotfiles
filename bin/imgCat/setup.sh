#!/bin/bash
# This script is used to setup the imgCat script.

cd "$(dirname "$0")"

echo "Setting up imgCat..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "imgCat setup complete."