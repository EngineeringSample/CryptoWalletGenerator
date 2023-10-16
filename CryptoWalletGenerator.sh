#!/bin/bash

# Install Python dependencies
pip install eth-account bitcoinlib tronapi

# Download the Python script file (Replace the GitHub URL and filename)
wget https://raw.githubusercontent.com/YuanLiuchang/CryptoWalletGenerator/main/CryptoWalletGenerator.py

# Run the Python script
python CryptoWalletGenerator.py
