from random import randint
from typing import Optional


class Game:
    def __init__(self):
        self.__matches: int = 20
        self.__win: Optional[bool] = None

        self.__current_move: Optional['Player'] = None
        self.__computer_player: Optional['Player'] = None
        self.__user_player: Optional['Player'] = None

    @property
    def matches(self) -> int:
        return self.__matches

    @matches.setter
    def matches(self, new_matches: int) -> None:
        if new_matches:
            self.__matches = new_matches
        else:
            self.__win = self.finish_game()

    @property
    def win(self) -> Optional[bool]:
        return self.__win

    @property
    def current_move(self) -> Optional['Player']:
        return self.__current_move

    @property
    def computer_player(self) -> Optional['Player']:
        return self.__computer_player

    @property
    def user_player(self) -> Optional['Player']:
        return self.__user_player

    def start_game(self, user: 'Player', bot: 'Player') -> None:
        self.__matches = 20
        self.__current_move = (user, bot)[randint(0, 1)]

        self.__user_player = user
        self.__computer_player = bot

    def finish_game(self) -> bool:
        if self.__current_move == self.__user_player:
            return True
        else:
            return False


class Player:
    def __init__(self, name: str, game: 'Game'):
        self.__name = name
        self.__game = game

    @property
    def name(self):
        return self.__name

    @property
    def game(self):
        return self.__game

    def take_matches(self, num_matches: int) -> None:
        assert 1 <= num_matches <= 3 and num_matches <= self.game.matches
        self.__game.matches -= num_matches
