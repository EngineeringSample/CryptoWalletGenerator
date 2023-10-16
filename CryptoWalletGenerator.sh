#!/bin/bash

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Python is not installed. Please install Python."
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "pip is not installed. Please install pip."
    exit 1
fi

# Install Python dependencies
pip install eth-account bitcoinlib tronapi

# Download the Python script file (Replace the GitHub URL and filename)
wget https://raw.githubusercontent.com/YuanLiuchang/CryptoWalletGenerator/main/CryptoWalletGenerator.py

# Run the Python script
python CryptoWalletGenerator.py
