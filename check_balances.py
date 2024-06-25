import os
import random
from web3 import Web3

def generate_private_keys(num_keys):
    keys = []
    for _ in range(num_keys):
        private_key = ''.join([random.choice('0123456789abcdef') for _ in range(64)])
        keys.append(private_key)
    return keys

def main():
    try:
        # Get Infura Project ID from environment variables
        infura_project_id = os.getenv('INFURA_PROJECT_ID')
        if not infura_project_id:
            raise ValueError("Infura Project ID not found in environment variables")
        
        infura_url = f"https://mainnet.infura.io/v3/{infura_project_id}"
        web3 = Web3(Web3.HTTPProvider(infura_url))

        if not web3.isConnected():
            raise ConnectionError("Failed to connect to the Ethereum network")

        # Generate 500 private keys
        private_keys = generate_private_keys(500)

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

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
