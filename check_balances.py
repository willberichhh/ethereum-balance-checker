import os
from web3 import Web3

# Get Infura Project ID from environment variables
infura_project_id = os.getenv('INFURA_PROJECT_ID')
infura_url = f"https://mainnet.infura.io/v3/{infura_project_id}"
web3 = Web3(Web3.HTTPProvider(infura_url))

# List of private keys
private_keys = [
    "730f6bc56887665193154da5f771dc940edd04a63b8c2b7f7a13253e9509311a",
    "6b75f4054b2f739b43c4940751379e43520df147c5fba2c8ac3de86b7d8f4bb7",
    # add the rest of your private keys here...
]

def private_key_to_address(private_key):
    account = web3.eth.account.privateKeyToAccount(private_key)
    return account.address

def check_balances(private_keys):
    balances = {}
    for pk in private_keys:
        address = private_key_to_address(pk)
        balance = web3.eth.get_balance(address)
        balances[address] = web3.fromWei(balance, 'ether')
    return balances

balances = check_balances(private_keys)
for address, balance in balances.items():
    print(f"Address: {address}, Balance: {balance} ETH")
