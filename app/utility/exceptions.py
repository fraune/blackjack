class RoundOverException(Exception):
    def __init__(self, msg='Cannot take more cards after busted or stood', *args):
        super().__init__(msg, *args)


class UnknownGameStateException(Exception):
    def __init__(self, msg='The state of the endgame is unknown', *args):
        super().__init__(msg, *args)
