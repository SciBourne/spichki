from spichki.models import Game, Player


class GameSession:
    def __init__(self, user_name: str, bot_name: str):
        self.game: 'Game' = Game()

        self.user: 'Player' = Player(
            game=self.game,
            name=user_name
        )
        self.bot: 'Player' = Player(
            game=self.game,
            name=bot_name
        )
