# -*- coding:utf-8 -*-
import sys

def build_frame(line, frame_border):
    frame_idx = []
    p = 0
    for char in line:
        if char == '[':
            frame_idx.append(p)
        elif char == ']':
            left_border = frame_idx.pop()
            frame_border[p] = left_border
            frame_border[left_border] = p
        p = p + 1

def run(line):
    li = [0]
    frame_border = {}
    pos = 0
    build_frame(line, frame_border)
    idx = 0
    while idx < len(line):
        p = line[idx]
        if p == '+':
            li[pos] = li[pos] + 1
        elif p == '-':
            li[pos] = li[pos] - 1
        elif p == '>':
            pos = pos + 1
            if pos == len(li):
                li.append(0)
        elif p == '<':
            pos = pos - 1
        elif p == '.':
            sys.stdout.write(chr(li[pos]))
        elif p == ',':
            x = sys.stdin.read(1)
            li[pos] = x
        elif p == '[':
            if not li[pos]:
                idx = frame_border[idx]
        elif p == ']':
            if li[pos]:
                idx = frame_border[idx]
        idx = idx + 1

if __name__ == '__main__':
    # Hello World! 1
    #line = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'

    # Hello World! 2
    #line = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'

    # Arch is the best!
    #line = '++>++++++>+++++<+[>[->+<]<->++++++++++<]>>.<[-]>[-<++>]<----------------.---------------.+++++.<+++[-<++++++++++>]<.>>+.++++++++++.<<.>>+.------------.---.<<.>>---.+++.++++++++++++++.+.<<+.[-]++++++++++.'

    # Happy new year, gods bless the Kw33n!%
    #line = '++++++++++[>+++>++++>+++++++>++++++++++>+++++++++++<<<<<-]>>>++.>---.>++..+++++++++.<<<<++.>>>>-----------.---------.++++++++++++++++++.<<<<.>>>>++.<++++.----.>-------.<<<++++.<.>>>++++++.>---.<---.>++++.<<<<.>>>--.++++++++++.-------.>..<<<<.>>>>+.<+++.---.<<<.>>+++.>>+++.<<<+++++++..>>>---------.<<<<+.'

    line = ''
    run(line)

