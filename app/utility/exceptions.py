class RoundOverException(Exception):
    def __init__(self, msg='Cannot take more cards after busted or stood', *args):
        super().__init__(msg, *args)
