from scripts.helpful_scripts import get_account
from brownie import SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"


def main():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(
                simple_collectible.address, simple_collectible.tokenCounter() - 1
            )
        )
    )
