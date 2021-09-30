from brownie import network, config, accounts


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


# def get_account():
#     if (
#         network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
#         or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
#     ):
#         return accounts[0]
#     else:
#         return accounts.add(config["wallets"]["from_key"])
