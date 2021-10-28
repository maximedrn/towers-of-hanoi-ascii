"""@author: Maxime."""


from colorama import init, Back as B, Fore, Style
from time import sleep
import os

"""Colorama module constants."""
init(convert=True)
reset = Style.RESET_ALL
red = Fore.RED
colors = [B.YELLOW, B.GREEN, B.CYAN, B.BLUE, B.MAGENTA, B.RED, B.WHITE]


class Hanoi:
    """Towers of Hanoi class - GUI ASCII interface."""

    def __init__(self, discs: int, timer: int) -> None:
        self.discs = discs
        self.timer = timer
        self.size = 4
        self.discs_list = self.discs_ascii()
        self.a, self.b, self.c = self.discs_list.copy(), [], []
        self.show_towers()
        self.play(discs)

    def discs_ascii(self) -> list:
        """Create all discs size with ASCII."""
        discs_list = []
        for disk in range(self.discs):
            color = colors[disk]
            space = ' ' * (self.discs - disk) * (self.size // 2)
            disk_ = f'{space}{color}' + \
                    f'{" " * (disk + 1) * self.size}{reset}{space}'
            discs_list.append(f'{disk_}')
        return discs_list

    def play(self, discs: int = 5, a: str = 'A', b: str = 'C',
             c: str = 'B') -> None:
        """Recursive Python function to solve the tower of Hanoi."""
        if discs == 1:
            print(f'Move disk {colors[0]}   {reset}' +
                  f' from tower {a} to tower {b}.\n')
            self.move(discs, a, b)
            return
        self.play(discs - 1, a, c, b)
        print(f'Move disk {colors[discs - 1]}   {reset}' +
              f' from tower {a} to tower {b}.\n')
        self.move(discs, a, b)
        self.play(discs - 1, c, b, a)

    def move(self, discs: int, a: str, b: str) -> None:
        """Move discs from a list to another list."""
        eval(f'self.{a.lower()}').pop(0)  # Remove first disk of tower.
        eval(f'self.{b.lower()}').insert(0, self.discs_list[discs - 1])
        self.show_towers()

    def show_towers(self) -> None:
        """Print towers with discs."""
        a, b, c = self.a.copy(), self.b.copy(), self.c.copy()
        spaces = ' ' * (self.discs + 1) * self.size
        for tower in [a, b, c]:
            if len(tower) < self.discs:
                for _ in range(self.discs - len(tower)):
                    tower.insert(0, spaces)
        for line in range(self.discs):
            for _ in range(2):
                lines = ''
                for tower in [a, b, c]:
                    lines += tower[line]
                print(lines)
        sleep(self.timer)
        cls()  # Clear console.


def cls() -> None:
    """Clear console function."""
    # Clear console for Windows using 'cls' and Linux & Mac using 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    cls()  # Clear console.
    while True:
        discs = input('Number of discs: ')
        if discs.isdigit():
            if 0 < int(discs) < 8:
                discs = int(discs)
                timer = input('Time to wait between round: ')
                if timer.isdigit():
                    timer = int(timer)
                    cls()  # Clear console.
                    hanoi = Hanoi(discs, timer)
                    break
        cls()  # Clear console.
        print(f'{red}Must be an integer between 1 and 7.{reset}')
