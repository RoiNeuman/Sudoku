#!/usr/bin/env python3
import random


def createGrid():
    newMap = [[0] * 9 for _ in range(9)]
    blocks = [[] * 9 for _ in range(9)]
    attemptPlacing(newMap, 0, 0, [], blocks)
    return newMap


def attemptPlacing(newMap, rawIndex, columnIndex, raw, blocks):
    if columnIndex > 9:
        return False
    pn = []  # pn - possible numbers
    column = []
    for i in range(rawIndex):
        column.append(newMap[i][columnIndex])
    for num in range(1, 10):  # 1, 2,..., 8, 9
        if num not in raw and num not in column and num not in blocks[blockIndex(rawIndex, columnIndex)]:
            pn.append(num)
    while len(pn) != 0:
        randomNum = random.choice(pn)
        newMap[rawIndex][columnIndex] = randomNum
        if columnIndex == 8 and rawIndex == 8:
            return True  # This is a good grid
        raw.append(randomNum)
        blocks[blockIndex(rawIndex, columnIndex)].append(randomNum)
        if columnIndex < 8:
            if attemptPlacing(newMap, rawIndex, (columnIndex+1), raw, blocks):
                return True
            pn.remove(randomNum)
            raw.remove(randomNum)
            blocks[blockIndex(rawIndex, columnIndex)].remove(randomNum)
        else:
            if rawIndex == 8:
                pn.remove(randomNum)
                raw.remove(randomNum)
                blocks[blockIndex(rawIndex, columnIndex)].remove(randomNum)
                continue
            if attemptPlacing(newMap, (rawIndex+1), 0, [], blocks):
                return True
            pn.remove(randomNum)
            raw.remove(randomNum)
            blocks[blockIndex(rawIndex, columnIndex)].remove(randomNum)
    return False


def blockIndex(raw, column):
    if raw < 3 and column < 3:
        return 0
    if raw < 3 and 2 < column < 6:
        return 1
    if raw < 3 and 5 < column:
        return 2
    if 2 < raw < 6 and column < 3:
        return 3
    if 2 < raw < 6 and 2 < column < 6:
        return 4
    if 2 < raw < 6 and 5 < column:
        return 5
    if 5 < raw and column < 3:
        return 6
    if 5 < raw and 2 < column < 6:
        return 7
    if 5 < raw and 5 < column:
        return 8

