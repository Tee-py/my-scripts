from algofi_amm.utils import get_account_balances, get_application_global_state, get_application_local_state
from algofi_amm.v0.client import AlgofiAMMClient
from algofi_amm.v0.asset import Asset
from algosdk.v2client import indexer, algod
from algofi_amm.v0.config import Network
import json



app_id = 465814065

address = "TBGSXXIPFBUF5GLQNKDF4ECRXFQNR3HGQJL6QT56RAP5H3SWG2YMVSHXMQ"
indexer_url = "https://algoindexer.algoexplorerapi.io"
asset_snapshot_url = "https://thf1cmidt1.execute-api.us-east-2.amazonaws.com/Prod/amm_asset_snapshots/?network=MAINNET"
amm_assets_url = "https://thf1cmidt1.execute-api.us-east-2.amazonaws.com/Prod/amm_assets/?network=MAINNET"
amm_pools_url = "https://thf1cmidt1.execute-api.us-east-2.amazonaws.com/Prod/amm_pools/?network=MAINNET"
app_url = f"https://mn3.algofi.org/v2/applications/{app_id}"

# instantiate indexer client
Indexer = indexer.IndexerClient("", indexer_url, {"X-API-Key": ""})
AlgodClient = algod.AlgodClient("", "https://node.algoexplorerapi.io", {"X-API-Key": ""})
AMMClient = AlgofiAMMClient(AlgodClient, Indexer, Indexer, address, Network.MAINNET)
res = Indexer.lookup_account_application_local_state(address)
with open('file.json', 'w') as file:
    json.dump(res, file, indent=4)

"""
result = get_account_balances(Indexer, address, filter_zero_balances=True)
assets = result.keys()

for asset in assets:
    #print(AMMClient.network)
    #ass = Asset(AMMClient, asset)
    pass
    #print(f"Price Is: {ass.refresh_price()}")
    #print(AMMClient.get_user_balance(ass))
    #print(AMMClient.get_user_balances(address)) --> Same As Account Info
    # --> Returns Info About Asset
    #print(AMMClient.get_user_info(address)) --> Retunrs User Info including Localstate of Apps
"""   
