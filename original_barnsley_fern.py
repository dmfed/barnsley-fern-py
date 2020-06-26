#!/usr/bin/env python3
import argparse
from turtle import RawPen, Screen
import random

def parse_args():
    parser = argparse.ArgumentParser(
        description="Draw Barnsley's fern using Python's Turtle graphics.")
    parser.add_argument('-d', '--dots',  metavar='number',
                        help='Number of dots to draw.',
                        type=int, default=20000)
    parser.add_argument('-bg', '--background',  metavar='color',
                        type=str, default='white',
                        help='Background color.')
    parser.add_argument('-fg', '--foreground',  metavar='color',
                        type=str, default='green',
                        help='Drawing color.')
    parser.add_argument('-s', '--scale',  metavar='pixels',
                        type=int, default=50,
                        help='Choose scale. Default is 50 pixels.')
    parser.add_argument('-ww', '--width', metavar='pixels',
                        type=int, default=600,
                        help='Window width.')
    parser.add_argument('-wh', '--height', metavar='pixels',
                        type=int, default=800,
                        help='Window width.')
    args = parser.parse_args()    
    return args

def draw(root):
    pen = RawPen(root)
    pen.speed(0)
    pen.ht()
    pen.pu()
    pen.screen.bgcolor(args.background)
    x = 0.0
    y = 0.0
    for i in range(args.dots):
        r = random.randint(0, 100)
        if r <= 1:
            tempx = 0.0
            tempy = 0.16 * y
        elif r <= 7:
            tempx = 0.2 * x - 0.26 * y 
            tempy = 0.23 * x + 0.22 * y + 1.6
        elif r <= 15:
            tempx = -0.15 * x + 0.28 * y 
            tempy = 0.26 * x + 0.24 * y + 0.44
        else:
            tempx = 0.85 * x + 0.04 * y 
            tempy = -0.04 * x + 0.850 * y + 1.6
        x, y = tempx, tempy
        pen.setpos(x * args.scale - args.scale // 2, y * args.scale - args.scale * 3)
        pen.dot(1, args.foreground)
    print('All done!')
    input('Press any key to quit')

if __name__ == '__main__':
    args = parse_args()
    root = Screen()
    root.setup (width=600, height=800)
    root.title('Barnsley fern')
    root.tracer(n=15000)
    draw(root)
