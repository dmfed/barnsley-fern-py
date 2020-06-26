#!/usr/bin/env python3
import argparse
from turtle import Turtle
import random

def parse_args():
    parser = argparse.ArgumentParser(
        description="Draw Barnsley fern using Python's Turtle graphics.")
    parser.add_argument('-d', '--dots',  metavar='number',
                        help='Number of dots to draw. Deefault is 20000',
                        type=int, default=20000)
    parser.add_argument('-bg', '--background',  metavar='color',
                        type=str, default='white',
                        help='Sets background color.')
    parser.add_argument('-fg', '--foreground',  metavar='color',
                        type=str, default='green',
                        help='Sets pen color color.')
    parser.add_argument('-s', '--scale',  metavar='pixels',
                        type=int, default=500,
                        help='Chooses scale. Default is 500 pixels.')
    parser.add_argument('-ww', '--width', metavar='pixels',
                        type=int, default=600,
                        help='Window width.')
    parser.add_argument('-wh', '--height', metavar='pixels',
                        type=int, default=800,
                        help='Window height.')
    args = parser.parse_args()    
    return args

def draw_fern(pen):
    x = 0.5
    y = 0.0
    for i in range(args.dots):
        r = random.randint(0, 100)
        if r <= 1:
            tempx = 0.5
            tempy = 0.16 * y
        elif r <= 8:
            tempx = 0.2 * x - 0.26 * y + 0.400
            tempy = 0.23 * x + 0.22 * y - 0.045
        elif r <= 15:
            tempx = -0.15 * x + 0.28 * y + 0.575
            tempy = 0.26 * x + 0.24 * y - 0.086
        else:
            tempx = 0.85 * x + 0.04 * y + 0.075
            tempy = -0.04 * x + 0.850 * y + 0.180
        if r == 100:
            r = 0
        r += 1
        x, y = tempx, tempy
        pen.setpos(x * args.scale - args.scale // 2, y * args.scale - args.scale // 2)
        pen.dot(1)

def setup_pen():
    pen = Turtle()
    pen.speed(0)
    pen.ht()
    pen.pu()
    pen.screen.setup (width=args.width, height=args.height)
    pen.screen.title('Barnsley fern')
    pen.screen.bgcolor(args.background)
    pen.screen.tracer(n=15000) # skips frames to speed up drawing
    pen.color(args.foreground)
    return pen

if __name__ == '__main__':
    args = parse_args()
    pen = setup_pen()
    draw_fern(pen)
    input('All done!\nPress Enter to quit')
    exit()
