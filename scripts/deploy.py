import os
from brownie import network, accounts, config, Hello
#INFURA_API = 

def main():
    dev = accounts.add('')
    hello = Hello.deploy({'from': dev})
    print(hello.address)