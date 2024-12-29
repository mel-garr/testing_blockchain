from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from web3 import Web3
from web3.providers.eth_tester import EthereumTesterProvider
from solcx import compile_source, install_solc
from .utils import blockchain

INFURA_URL = 'https://sepolia.infura.io/v3/68535a9d8e6e4f1f92ca21bd25ce1ed5'
PRIVAE_KEY =   "c7734089f791f1c724451045ff606ffb0d1591bee61d562aa668a58b4a7466a2"
METCA_ACCOUNT = '0xFb02aEeB164786B0885bB178CDC09133872093EE'

CONTRACT_SOURCE_CODE = '''
pragma solidity ^0.8.0;

contract LetterStorage {
    string[] private letters;

    function addLetter(string memory letter) public {
        letters.push(letter);
    }

    function getAllLetters() public view returns (string[] memory) {
        return letters;
    }
}
'''

compiled_sol = compile_source(CONTRACT_SOURCE_CODE)
contract_id, contract_interface = compiled_sol.popitem()

# Create your views here.
def home_view(request):
    web = Web3(Web3.HTTPProvider(INFURA_URL))

    return render(request, 'home.html')

@csrf_exempt
def send_to_back(request):
    if request.method != 'POST':
        return JsonResponse({'error' : 'Invalid reauest method'}, status=405)
    
    letter = 'a'

    result = blockchain.store_letter(letter)
    if result['ok']:
        return JsonResponse({
            'message': 'Letter stored in the blockchain',
            'tx_hash': result['tx_hash']
        })
    else:
        return JsonResponse({
            'error': result['error']
        }, status=400)