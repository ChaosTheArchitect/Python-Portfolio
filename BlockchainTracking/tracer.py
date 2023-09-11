import requests
import time

BASE_URL = "https://blockchain.info"
CORS_PARAM = "&cors=true"

bitcoin_address = '34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo'


def fetch_address_transactions(bitcoin_address):
    """Fetch transactions of a Bitcoin address."""
    url = f"{BASE_URL}/rawaddr/{bitcoin_address}?format=json{CORS_PARAM}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error fetching transactions for address {bitcoin_address}. Status code: {response.status_code}")

    data = response.json()
    return data["txs"]


def trace_address(bitcoin_address: str, depth: int = 1):
    """Trace Bitcoin address and display transaction details."""

    if depth <= 0:
        return

    time.sleep(10)  # sleep for 10 seconds before making a new request

    print(f"\nTracing address: {bitcoin_address} (Depth: {depth})\n")
    transactions = fetch_address_transactions(bitcoin_address)

    for tx in transactions:
        print(f"Transaction ID: {tx['hash']}")

        # Display inputs (senders)
        for input_data in tx["inputs"]:
            prev_out = input_data["prev_out"]
            print(f"Received from address: {prev_out['addr']}, Amount: {prev_out['value']} Satoshis")
            if depth > 1:
                trace_address(prev_out['addr'], depth-1)

        # Display outputs (receivers)
        for out in tx["out"]:
            print(f"Sent to address: {out['addr']}, Amount: {out['value']} Satoshis")
            if depth > 1:
                trace_address(out['addr'], depth-1)

    print("\n")

# Starting point using the provided Bitcoin address


trace_address(bitcoin_address, depth=2)
