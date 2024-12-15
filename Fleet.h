#ifndef FLEET_H
#define FLEET_H

#include "Ship.h"
#include <vector>

class Fleet {
public:
    void addShip(const Ship& newShip);
    bool areAllSunk() const;
    void attackShip(size_t shipIndex, size_t segmentIndex);

private:
    std::vector<Ship> ships;
};

#endif
