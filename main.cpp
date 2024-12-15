#include <iostream>
#include "GameBoard.h"
#include "Ship.h"

int main() {
    GameBoard board(10, 10);

    Ship ship1(4, Ship::Horizontal);
    Ship ship2(3, Ship::Vertical);

    if (!board.addShipToBoard(ship1, 2, 2)) {
        std::cerr << "Failed to place ship1!" << std::endl;
    }

    if (!board.addShipToBoard(ship2, 4, 5)) {
        std::cerr << "Failed to place ship2!" << std::endl;
    }

    board.fireAt(3, 3);
    board.fireAt(5, 5);
    board.fireAt(8, 8);

    std::cout << "Game board:" << std::endl;
    board.displayBoard();

    return 0;
}
