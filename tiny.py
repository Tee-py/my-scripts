from tinyman.v1.client import TinymanClient
from dotenv import load_dotenv
import os
import time
from algosdk.v2client.algod import AlgodClient

load_dotenv()

address = os.getenv("ADDRESS")
private_key = os.getenv("PRIVATE_KEY")
app_id = int(os.getenv("VALIDATOR_APP_ID"))

algod_address = os.getenv("ALGOD_ADDRESS")
algod_token = os.getenv("ALGOD_TOKEN")
headers = {"X-API-Key": algod_token }

algod = AlgodClient(algod_token, algod_address, headers)

client = TinymanClient(algod, app_id, address)

CHOICE = client.fetch_asset(297995609)
ALGO = client.fetch_asset(0)

pool = client.fetch_pool(CHOICE, ALGO)

while True:
    quote = pool.fetch_fixed_input_swap_quote(ALGO(1_000_000), slippage=0.01)
    #print(quote)
    if quote.price*10000 >= 50:
        print("This is The set Price")
        break
    print(f'CHOICE per ALGO: {quote.price*10000}')
    print(f'CHOICE per ALGO (worst case): {quote.price_with_slippage*10000}')
    print('\n\n')
    time.sleep(10)


"""
if quote.price_with_slippage > 180:
    print(f'Swapping {quote.amount_in} to {quote.amount_out_with_slippage}')
    # Prepare a transaction group
    transaction_group = pool.prepare_swap_transactions_from_quote(quote)
    # Sign the group with our key
    transaction_group.sign_with_private_key(account['address'], account['private_key'])
    # Submit transactions to the network and wait for confirmation
    result = client.submit(transaction_group, wait=True)

    # Check if any excess remaining after the swap
    excess = pool.fetch_excess_amounts()
    if TINYUSDC in excess:
        amount = excess[TINYUSDC]
        print(f'Excess: {amount}')
        # We might just let the excess accumulate rather than redeeming if its < 1 TinyUSDC
        if amount > 1_000_000:
            transaction_group = pool.prepare_redeem_transactions(amount)
            transaction_group.sign_with_private_key(account['address'], account['private_key'])
            result = client.submit(transaction_group, wait=True)
"""