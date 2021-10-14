# 0.014015849
# 1.4016×10¹⁶
from brownie import Lottery, accounts, config, network
from web3 import Web3
from scripts.deploy import deploy_lottery


def test_get_entrance_fee():
    # Arrange
    lottery = deploy_lottery()
    # Act
    # 2,000 eth / usd
    # UsdEntryFee is 50
    # 2000/1 == 50/x == 0.025
    expected_entrance_fee = Web3.toWei(0.025, "ether")
    entrance_fee = lottery.getEntranceFee()
    # Assert
    assert expected_entrance_fee == entrance_fee
