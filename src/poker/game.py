from deck import Deck
from dataclasses import dataclass

@dataclass
class Player:
    name: str
    stack: float
    hand: list
    status: bool
    chips_in_play: float  # previously was bet, renamed for consistency

    def __str__(self) -> str:
        return self.name

    def post_ante(self, ante: float) -> None:
        self.stack -= ante
        self.chips_in_play += ante


@dataclass
class Pot:
    total: float = 0

    def reset_pot(self) -> None:
        self.total = 0

    def add_to_pot(self, amount: float) -> None:
        self.total += amount

    def award_pot(self, player: Player) -> None:
        player.stack += self.total

    def split_pot(self, players: list[Player]) -> None:
        for player in players:
            player.stack += self.total / len(players)


@dataclass
class Dealer:
    pot: Pot
    deck: Deck
    current_bet: float = 0
    button: int = 0

    # Rhode Island Hold'em
    def deal_hand(self, players: list[Player]):
        for player in players:
            if player is not None:  # Only deal to non-empty seats
                player.hand = self.deck.dealCards(1)
                # this error can be ignored as we will never not have enough cards

    def move_button(self, players: list[Player]):
        self.button = (self.button + 1) % len(players)

    # we don't need blind setting functions for now


class Table:
    def __init__(self, seats) -> None:
        self.seats = seats
        self.seats: list[None] = [None] * seats

    def __str__(self) -> str:
        return str(self.seats)

    def seat_player(self, player, seat) -> None:
        self.seats[seat] = player
