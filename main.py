# -*- coding: utf-8 -*-
from point import Point
from point import normalize_angle


def main():
    with open('teksty.txt', 'r') as file:
        data = file.readlines()

    points = []
    for line in data:
        point = line.strip().split()
        points.append(Point(point[0], point[1], point[2]))

    length = 0
    azimuth = 0
    for i in range(len(points)-1):
        azimuth += points[i].get_azimuth(points[i+1])
        length += points[i].get_length(points[i+1])

    print(f'length = {length}')
    print(f'azimuth = {azimuth}')


if __name__ == '__main__':
    main()
