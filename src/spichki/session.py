from spichki.models import Game, Player


class GameSession:
    def __init__(self, user_name: str, bot_name: str):
        self.__game: 'Game' = Game()

        self.__user: 'Player' = Player(
            game=self.__game,
            name=user_name
        )
        self.__bot: 'Player' = Player(
            game=self.__game,
            name=bot_name
        )

        @property
        def game(self):
            return self.__game

        @property
        def user_name(self):
            return self.__user.name

        @property
        def bot_name(self):
            return self.__bot.name
