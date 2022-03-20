from web3 import Web3

TOTAL_GONS=(2**256-1)-((2**256-1)%(325 * 10**3 * 10**5))
_totalSupply=325 * 10**8
_gonsPerFragment= TOTAL_GONS/_totalSupply
print(_gonsPerFragment)