import hashlib
import time

class Move:
    NONE = 0
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


    def __init__(self, commitment, move = 0):
        self.commitment = commitment # this is secret string
        self.move = move



@classmethod
def move_to_str(clss, move,):
    return{
        clss.NON: "None",
        clss.ROCK: "Rock",
        clss.PAPER: "Paper",
        clss.SCISSORS: "Scissors"
    }[move]


class Challenge:
    def __init__(self, creator_address, _id, commitment):
        self.creator_address = creator_address
        self.opponent_address = None

        self.commitments = {
            self.creator_address: Move(commitment)
        }

        self.id = _id

        self.winner_address = None
        self.created_ad = time.time()

    def add_opponent(self, address, commitment):
        self.opponent_address = address
        self.commitments[address] = Move(commitment)

    def reveal(self, address, move, nonce): #nonce is secret number that we will use to hash with
        if not self.commitments.get(self.opponent_address):
            raise Exception("Opponent has not commited")
        

        reveal_hash = Challenge.generate_hash(nonce+ + move)
        commited_move = self.commitments.get(address)

        if commited_move.commitment != reveal_hash:
            raise Exception("Move does not match the commitment.")
    
        self.commitments[address].move = int(move)

    @staticmethod
    def generate_hash(input):
        return hashlib.sha256(input.encode()).hexdigest()
    

    def both_revealed(self):

    
     