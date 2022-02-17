from tinyman.v1.client import TinymanClient
from dotenv import load_dotenv
import os
import time
from algosdk.v2client.algod import AlgodClient
from algosdk import mnemonic

load_dotenv()

address = os.getenv("ADDRESS")
private_key = mnemonic.to_private_key(os.getenv("PRIVATE_KEY"))
app_id = int(os.getenv("VALIDATOR_APP_ID"))

algod_address = os.getenv("ALGOD_ADDRESS")
algod_token = os.getenv("ALGOD_TOKEN")
headers = {"X-API-Key": algod_token }

algod = AlgodClient(algod_token, algod_address, headers)

client = TinymanClient(algod, app_id, address)

CHOICE = client.fetch_asset(297995609)
ALGO = client.fetch_asset(0)

pool = client.fetch_pool(CHOICE, ALGO)

def swap(amount: int):
    quote = pool.fetch_fixed_input_swap_quote(CHOICE(amount*100), slippage=0.01)
    print(quote)
    print(private_key)

    print(f'Swapping {quote.amount_in} to {quote.amount_out_with_slippage}')
    # Prepare a transaction group
    transaction_group = pool.prepare_swap_transactions_from_quote(quote)

    transaction_group.sign_with_private_key(address, private_key)
    result = client.submit(transaction_group, wait=True)
    print(result)
    return True

if __name__ == "__main__":
    amount = input("Enter Amount Of Choice To Swap")
    try:
        amount = int(amount)
        if amount <= 0:
            print("Invalid Amount")
        swap(amount)
    except:
        print("An Error Occurred. Try Again")







# Check if any excess remaining after the swap
"""
excess = pool.fetch_excess_amounts()
if ALGO in excess:
    amount = excess[ALGO]
    print(f'Excess: {amount}')
        # We might just let the excess accumulate rather than redeeming if its < 1 TinyUSDC
        if amount > 1_000_000:
            transaction_group = pool.prepare_redeem_transactions(amount)
            transaction_group.sign_with_private_key(account['address'], account['private_key'])
            result = client.submit(transaction_group, wait=True)
"""



