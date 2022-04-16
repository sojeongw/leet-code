class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter, number = ord(coordinates[0])-96, int(coordinates[1])
        return (letter + number) % 2 != 0