from commun.game import createGame


class serverData:
    def __init__(self, theme):
        self.game = createGame(theme = theme)
