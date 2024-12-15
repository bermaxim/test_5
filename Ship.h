#ifndef SHIP_H
#define SHIP_H

#include <vector>
#include <cstddef>
#include <algorithm>


class Ship {
public:
    enum SegmentState { Intact, Damaged, Destroyed };
    enum Direction { Horizontal, Vertical };
     
    Ship(size_t size, Direction dir);
    size_t getSize() const;
    Direction getDirection() const;
    SegmentState getSegmentStatus(size_t segmentIndex) const;
    void damageSegment(size_t segmentIndex);
    bool isSunk() const;

private:
    size_t size;
    Direction direction;
    std::vector<SegmentState> segments;

    static void validateSize(size_t size);
    void ensureValidSegment(size_t segmentIndex) const;
};

#endif
