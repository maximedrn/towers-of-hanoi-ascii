"""
@author: Maxime.

Github: https://github.com/maximedrn
Version: 1.0
"""


# Colorama module: pip install colorama
from colorama import init, Back as B, Fore, Style

# Python default import.
from time import sleep
import os


"""Colorama module constants."""
init(convert=True)
reset = Style.RESET_ALL  # Reset method.
red = Fore.RED  # Red text color method.
# Discs' background color list.
colors = [B.YELLOW, B.GREEN, B.CYAN, B.BLUE, B.MAGENTA, B.RED, B.WHITE] \
    if os.name == 'nt' else ['1', '2', '3', '4', '5', '6', '7']


class Hanoi:
    """Towers of Hanoi class - GUI ASCII interface."""

    def __init__(self, discs: int, waiting_time: int) -> None:
        self.discs = discs  # Number of discs.
        # Time in seconds of wait between rounds.
        self.waiting_time = waiting_time
        self.size = 4  # Size of discs
        self.discs_list = self.discs_ascii()  # Create discs list.
        # Init each towers: tower A has got a copy of the discs list.
        self.a, self.b, self.c = self.discs_list.copy(), [], []
        self.show_towers()  # Print game.
        self.play(discs)  # Start playing.

    def discs_ascii(self) -> list:
        """Create all discs size with ASCII and Colorama colors."""
        discs_list = []  # Empty list for discs.
        for disk in range(self.discs):
            # Apply a whitespace character for Windows or an asterisk.
            char = ' ' if os.name == 'nt' else '*'
            # Apply background color, only works on Windows.
            color = colors[disk] if os.name == 'nt' else ''
            # Add whitespaces to align each disk perfectly.
            space = ' ' * (self.discs - disk) * (self.size // 2)
            disk_ = f'{space}{color}' + \
                    f'{char * (disk + 1) * self.size}{reset}{space}'
            discs_list.append(f'{disk_}')  # Add disk to discs list.
        return discs_list

    def play(self, discs: int = 5, a: str = 'A', b: str = 'C',
             c: str = 'B') -> None:
        """Recursive Python function to solve the tower of Hanoi."""
        if discs == 1:
            # End of the game.
            print(f'Move disk {colors[0]}   {reset}' +
                  f' from tower {a} to tower {b}.\n')
            self.move(discs, a, b)  # Edit towers' lists.
            return  # Stop recursive loop.
        self.play(discs - 1, a, c, b)  # Invert towers C and B.
        print(f'Move disk {colors[discs - 1]}   {reset}' +
              f' from tower {a} to tower {b}.\n')
        self.move(discs, a, b)  # Edit towers' lists.
        self.play(discs - 1, c, b, a)  # Invert Tower A and C.

    def move(self, discs: int, a: str, b: str) -> None:
        """Move discs from a list to another list."""
        # Get variable name with a and b strings.
        eval(f'self.{a.lower()}').pop(0)  # Remove first disk of tower.
        # Insert at first position of the list a new disk.
        eval(f'self.{b.lower()}').insert(0, self.discs_list[discs - 1])
        self.show_towers()  # Print game.

    def show_towers(self) -> None:
        """Print towers with discs."""
        # Make a copy of towers to do not affect game.
        a, b, c = self.a.copy(), self.b.copy(), self.c.copy()
        # Create whitespaces.
        spaces = ' ' * (self.discs + 1) * self.size
        for tower in [a, b, c]:
            # Add blank discs to put discs at bottom of the tower.
            if len(tower) < self.discs:
                for _ in range(self.discs - len(tower)):
                    tower.insert(0, spaces)
        # Fusionate each lines of the 3 towers and print them.
        for line in range(self.discs):
            for _ in range(2):
                lines = ''
                for tower in [a, b, c]:
                    lines += tower[line]
                print(lines)
        sleep(self.waiting_time)  # Wait X seconds before next round.
        cls()  # Clear console.


def cls() -> None:
    """Clear console function."""
    # Clear console for Windows using 'cls' and Linux & Mac using 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    cls()  # Clear console.
    while True:
        discs = input('Number of discs: ')
        if discs.isdigit():  # Check if discs is an positive integer.
            if 0 < int(discs) < 8:  # Check if number of discs if 1-7.
                discs = int(discs)
                waiting_time = input('Waiting time between rounds: ')
                # Check if waiting time is a positive float.
                if waiting_time.replace('.', '').isdigit():
                    waiting_time = float(waiting_time)
                    cls()  # Clear console.
                    Hanoi(discs, waiting_time)  # Init Hanoi class.
                    break  # Break while loop to stop program.
                else:
                    # Waiting time is not a positive float.
                    print(f'{red}Must be a positive float or integer.{reset}')
            else:
                # Discs number is not between 1 and 7.
                print(f'{red}Must be between 1 and 7.{reset}')
        else:
            # Discs number is not a positive integer.
            print(f'{red}Must be a positive integer.{reset}')
        cls()  # Clear console.
