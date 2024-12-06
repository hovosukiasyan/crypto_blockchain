import time

from block import Block

class Blockchain:
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.init_genesis_block()

    def init_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        print("Genesis block's hash:")
        print(genesis_block.hash)
        self.chain.append(genesis_block)

    def add_block(self, block, proof):
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash or not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        return (block_hash.endswith('000') and block_hash == block.compute_hash())

    def proof_of_work(self, block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.endswith('000'):
            block.nonce += 1
            computed_hash = block.compute_hash()

        print("This is the last nonce number:")
        print(block.nonce)
        print("And this is the resulting computed_hash:")
        print(computed_hash)
        print("We thank miner Armen and give him a reward of 0.0000000001 BTC")
        return computed_hash

    @property
    def last_block(self):
        return self.chain[-1]

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        if not self.unconfirmed_transactions:
            return False
        last_block = self.last_block
        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)
        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index