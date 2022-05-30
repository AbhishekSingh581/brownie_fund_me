from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_script import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3

def deploy_fund_me():
    account=get_account()
    # if we are on persistance network like rinkeby
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS :
        priceFeed_address=config["networks"]["rinkeby"]["eth_usd_price_feed"]
    
    else:
        print("This active network is {network.show_active()}") 
        if len(MockV3Aggregator) <=0 :
            mockv3aggregator=MockV3Aggregator.deploy(18,Web3.toWei(2000,"ether"),{"from":account})
        priceFeed_address=mockv3aggregator.address;
        
    fund_me=FundMe.deploy(priceFeed_address,{"from":account},publish_source=config["networks"][network.show_active()]["verify"])   #pass to FundMe Contract
    print("Contract deploy to {fund_me.address}")
    
    

def main():
    deploy_fund_me()