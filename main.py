import hashlib
import json

class NeuralCoinBlock:
    def __init__(self, last_block_hash, trans_list):
        self.last_block_hash = last_block_hash
        self.trans_list = trans_list

        self.block_data = "-".join(trans_list)+"-"+last_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

# LANGUAGE
with open('transactions.json', encoding='utf-8') as fh:
    transactions = json.load(fh)

block = NeuralCoinBlock("Initial String",["0BTC FROM X TO Y"])
print(block.block_data)
for blockNo,blockData in transactions.items():
    transactions = [trans['value']+'BTC FROM '+trans['from']+' TO '+trans['to'] for trans in blockData]
    
    block = NeuralCoinBlock(block.block_hash, transactions)
    print(block.block_data)
print()
print("LAST HASH -",block.block_data)