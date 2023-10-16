from eth_account import Account
from bitcoinlib.wallets import Wallet
from tronapi import Tron

# Get the user's choice of cryptocurrency
selected_currency = input("Select the cryptocurrency to generate a wallet (ETH/BTC/TRX, default is ETH): ").strip().lower()

if selected_currency not in ["eth", "btc", "trx"]:
    selected_currency = "eth"  # Default choice is ETH

# Get the number of wallets to generate
num_wallets = int(input(f"Enter the number of {selected_currency.upper()} wallets to generate: "))

wallets = []

if selected_currency == "eth":
    for _ in range(num_wallets):
        account = Account.create()
        wallet = {
            "private_key": account.key.hex(),
            "address": account.address,
        }
        wallets.append(wallet)

elif selected_currency == "btc":
    for _ in range(num_wallets):
        wallet = Wallet.create()
        wallet_data = wallet.serialize()
        wallet = {
            "private_key": wallet_data["wif"],
            "address": wallet_data["address"],
        }
        wallets.append(wallet)

elif selected_currency == "trx":
    tron = Tron()
    for _ in range(num_wallets):
        account = tron.create_account()
        wallet = {
            "private_key": account.private_key,
            "address": account.address.base58,
        }
        wallets.append(wallet)

# Write the generated private keys and addresses to a text file
output_file = f"{selected_currency}_wallets.txt"
with open(output_file, "w") as f:
    for wallet in wallets:
        f.write(f"Private Key: {wallet['private_key']}\n")
        f.write(f"Address: {wallet['address']}\n\n")

print(f"{num_wallets} {selected_currency.upper()} wallet(s) have been generated and saved to {output_file}.")
