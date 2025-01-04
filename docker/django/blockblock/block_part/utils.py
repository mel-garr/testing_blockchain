# from web3 import Web3
# from solcx import compile_source, install_solc
# from django.conf import settings

# INFURA_URL = 'https://sepolia.infura.io/v3/68535a9d8e6e4f1f92ca21bd25ce1ed5'
# PRIVAE_KEY =   "c7734089f791f1c724451045ff606ffb0d1591bee61d562aa668a58b4a7466a2"
# METCA_ACCOUNT = '0xFb02aEeB164786B0885bB178CDC09133872093EE'

# class BlockchainManager:
#     def __init__(self):
#         self.web3 = Web3(Web3.HTTPProvider(INFURA_URL))
#         self.contract = None
#         self.initialize()

#     def initialize(self):
#         if not self.web3.is_connected():
#             raise Exception("Failed to connect to Ethereum network")

#         contract_source = '''
#         pragma solidity ^0.8.0;
#         contract LetterStorage {
#             string[] private letters;
            
#             function addLetter(string memory letter) public {
#                 letters.push(letter);
#             }
            
#             function getAllLetters() public view returns (string[] memory) {
#                 return letters;
#             }
#         }
#         '''
#         install_solc('0.8.0')
#         compiled_code = compile_source(contract_source)
#         _, contract_interface = compiled_code.pipitem()
#         if not hasattr(settings, 'CONTRACT_ADDRESS'):
#             contract = self.web3.eth.contract(
#                 abi=contract_interface['abi'],
#                 bytecode=contract_interface['bin']
#             )
            
#             tx = contract.constructor().build_transaction({
#                 'from': settings.ACCOUNT_ADDRESS,
#                 'nonce': self.web3.eth.get_transaction_count(settings.ACCOUNT_ADDRESS),
#                 'gas': 2000000,
#                 'gasPrice': self.web3.eth.gas_price
#             })
            
#             signed_tx = self.web3.eth.account.sign_transaction(tx, settings.PRIVATE_KEY)
#             tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
#             tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            
#             settings.CONTRACT_ADDRESS = tx_receipt.contractAddress
        
#         # Initialize the contract interface
#         self.contract = self.web3.eth.contract(
#             address=settings.CONTRACT_ADDRESS,
#             abi=contract_interface['abi']
#         )

#     def store_letter(self, letter):
#         """Store a letter in the blockchain"""
#         try:
#             tx = self.contract.functions.addLetter(letter).build_transaction({
#                 'from': settings.ACCOUNT_ADDRESS,
#                 'nonce': self.web3.eth.get_transaction_count(settings.ACCOUNT_ADDRESS),
#                 'gas': 200000,
#                 'gasPrice': self.web3.eth.gas_price
#             })
            
#             signed_tx = self.web3.eth.account.sign_transaction(tx, settings.PRIVATE_KEY)
#             tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
#             tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            
#             return {
#                 'success': True,
#                 'tx_hash': tx_hash.hex()
#             }
#         except Exception as e:
#             return {
#                 'success': False,
#                 'error': str(e)
#             }

# # Create a single instance to be used across the application
# blockchain = BlockchainManager()
from web3 import Web3
from solcx import compile_source
from django.conf import settings
from solcx import compile_source, install_solc
from solcx import get_installable_solc_versions

try:
    # Install solc compiler if not already installed
    install_solc('0.8.28')
    print('ready to go ?')
except Exception as e:
    print(f"Warning: Failed to install solc: {e}")

class BlockchainManager:
    def __init__(self):
        # Connect to Ethereum network (Sepolia testnet)
        self.web3 = Web3(Web3.HTTPProvider(settings.INFURA_URL))
        self.contract = None
        self.initialize()
    
    def initialize(self):
        """Set up the contract"""
        if not self.web3.is_connected():
            raise Exception("Failed to connect to Ethereum network")

        # Compile contract
        contract_source = '''
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
        
        compiled_sol = compile_source(contract_source)
        _, contract_interface = compiled_sol.popitem()
        
        # Deploy contract if we don't have an address
        if not hasattr(settings, 'CONTRACT_ADDRESS'):
            contract = self.web3.eth.contract(
                abi=contract_interface['abi'],
                bytecode=contract_interface['bin']
            )
            
            tx = contract.constructor().build_transaction({
                'from': settings.ACCOUNT_ADDRESS,
                'nonce': self.web3.eth.get_transaction_count(settings.ACCOUNT_ADDRESS),
                'gas': 2000000,
                'gasPrice': self.web3.eth.gas_price
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, settings.PRIVATE_KEY)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            
            settings.CONTRACT_ADDRESS = tx_receipt.contractAddress
        
        # Initialize the contract interface
        self.contract = self.web3.eth.contract(
            address=settings.CONTRACT_ADDRESS,
            abi=contract_interface['abi']
        )

    def store_letter(self, letter):
        """Store a letter in the blockchain"""
        try:
            tx = self.contract.functions.addLetter(letter).build_transaction({
                'from': settings.ACCOUNT_ADDRESS,
                'nonce': self.web3.eth.get_transaction_count(settings.ACCOUNT_ADDRESS),
                'gas': 200000,
                'gasPrice': self.web3.eth.gas_price
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, settings.PRIVATE_KEY)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            
            return {
                'success': True,
                'tx_hash': tx_hash.hex()
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

# Create a single instance to be used across the application
blockchain = BlockchainManager()