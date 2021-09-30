from brownie import accounts, config
import os


def deploy_simple_storage():
    # account = accounts[0]
    # account = accounts.load("rinkeby-testnet")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    account = accounts.add(config["wallets"]["from_key"])

    print(account)


def main():
    deploy_simple_storage()
