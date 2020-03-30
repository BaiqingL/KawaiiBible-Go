# -*- coding: utf-8 -*-
import re
import random
import numpy as np
import os
import ntpath
import sys
import ast
def getOwO():
    eye = random.choice([
    u'\U0000006f', u'\U0000004f', u'\U00000030', u'\U000000ba', u'\U00000040',
    u'\U000003a6', u'\U00000075', u'\U00000055', u'\U00002180', u'\U000025cf',
    u'\U0000003b', u'\U0000002e', u'\U000024db', u'\U00000078', u'\U00000058',
    u'\U000003c3', u'\U0000003e', u'\U0000003c', u'\U0000005e', u'\U00000398',
    u'\U000003b8', u'\U00002022', u'\U000000b0', u'\U0000002a', u'\U0001f441',
    u'\U0000fe0f', u'\U000025ef', u'\U000025cb', u'\U0000274d', u'\U00002394',
    u'\U00002b21', u'\U0001d67e', u'\U0001d698', u'\U00002b55', u'\U00000027',
    u'\U00000060', u'\U000025c9', u'\U00002727', u'\U000025d4', u'\U00002b20',
    u'\U000026aa', u'\U0000047a', u'\U0001d616', u'\U00002acf', u'\U00000ca5',
    u'\U00000ca0', u'\U00002686', u'\U000002d8', u'\U0000a004', u'\U0000a03e',
    random.choice([
    u'\U0001f550', u'\U0001f551', u'\U0001f552', u'\U0001f553', u'\U0001f554',
    u'\U0001f555', u'\U0001f556', u'\U0001f557', u'\U0001f558', u'\U0001f559',
    u'\U0001f55a', u'\U0001f55b', u'\U0001f55c', u'\U0001f55d', u'\U0001f55e',
    u'\U0001f55f', u'\U0001f560', u'\U0001f561', u'\U0001f562', u'\U0001f563',
    u'\U0001f564', u'\U0001f565', u'\U0001f566', u'\U0001f567']),
    random.choice([
    u'\U0001f311', u'\U0001f312', u'\U0001f313', u'\U0001f314',
    u'\U0001f315', u'\U0001f316', u'\U0001f317', u'\U0001f318'
    ])
    ])
    mouth = random.choice([
    u'\U00000077', u'\U00000057', u'\U00000414', u'\U000011ba',
    u'\U0000026f', u'\U00000270', u'\U00001d5a', u'\U0000a64d',
    u'\U000023d9', u'\U00000461', u'\U00002a4a', u'\U00000449',
    u'\U00000075', u'\U0001f444', u'\U000002d1\U0000032b'
    ])
    whisker = np.random.choice(['',
    u'\U0000003d\U0000003d', u'\U0000007e\U0000007e',
    u'\U0000002d\U0000002d', u'\U0000203a\U00002039',
    u'\U00002039\U0000203a', u'\U0000003e\U0000003c',
    u'\U000000bb\U000000ab', u'\U000000ab\U000000bb',
    u'\U00002267\U00002266', u'\U00004e09\U00004e09'],
    1, [1, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1])[0]
    close =  np.random.choice(['',
    u'\U00000028\U00000029', u'\U0000005b\U0000005d',
    u'\U0000007b\U0000007d', u'\U00003008\U00003009',
    u'\U00002985\U00002986', u'\U00002983\U00002984',
    u'\U000027c5\U000027c6', u'\U00002993\U00002994',
    u'\U0000fd3e\U0000fd3f', u'\U00000f3c\U00000f3d'],
    1, [1, 0.7, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])[0]
    return (close[0] if close != '' else '') + (whisker[0] if whisker != '' else '') + eye + mouth + eye + (whisker[1] if whisker != '' else '') + (close[1] if close != '' else '')


def matchCase(match, replacement):
    match = match.group()
    for i, char in enumerate(match):
        replacement = list(replacement)
        if char.upper() == char:
            replacement[i] = replacement[i].upper()
    return ''.join(replacement)
re1 = re.compile(r'per',flags=re.I)
re2 = re.compile(r'awesome',flags=re.I)
re3 = re.compile(r'awful',flags=re.I)
re4 = re.compile(r'clause',flags=re.I)
re5 = re.compile(r'kidding',flags=re.I)
re6 = re.compile(r'familiar',flags=re.I)
re7 = re.compile(r'for',flags=re.I)
re8 = re.compile(r'whisk',flags=re.I)
re9 = re.compile(r'you',flags=re.I)
re10 =re.compile(r'per',flags=re.I)
re11 =re.compile(r'par',flags=re.I)
re12 =re.compile(r'very',flags=re.I)
re13 =re.compile(r'ver',flags=re.I)
re14 =re.compile(r'now',flags=re.I)
re15 =re.compile(r'(?:(?<=^)|(?<=\W))wow(\W|$)',flags=re.I)
re16 =re.compile(r'(?:(?<=^)|(?<=\W))whoa(\W|$)',flags=re.I)
re17 =re.compile(r'(?:(?<=^)|(?<=\W))woah(\W|$)',flags=re.I)
re18 =re.compile(r'pause',flags=re.I)
re19 =re.compile(r'poss',flags=re.I)
re20 =re.compile(r'pall',flags=re.I)
re21 =re.compile(r'friend',flags=re.I)
re22 =re.compile(r'(?:(?<=^)|(?<=\W))hys(\w+)',flags=re.I)
re23 =re.compile(r'(?:(?<=^)|(?<=\W))at(\w+)',flags=re.I)
re24 =re.compile(r'feeling',flags=re.I)
re25 =re.compile(r'bark',flags=re.I)
re26 =re.compile(r'byte',flags=re.I)
re27 =re.compile(r'rough',flags=re.I)
re28 =re.compile(r'(?:(?<=^)|(?<=\W))(n|N)([aeiou])')
re29 =re.compile(r'(?:(?<=^)|(?<=\W))N([AEIOU])')
re30 =re.compile(r'ozone',flags=re.I)
re31 =re.compile(r'([.]\s)')
re32 =re.compile(r'([\?!]\s)')
re33 =re.compile(r'(?<!​)[lr]',flags=re.I)
def owo(input):
    input = re.sub(re1, lambda match: matchCase(match, u"pu​r​r"), input)
    input = re.sub(re2, np.random.choice([lambda match: matchCase(match, u"pawesome"), lambda match: matchCase(match, u"c​lawsome")]), input)
    input = re.sub(re3, np.random.choice([lambda match: matchCase(match, u"pawfu​l"), lambda match: matchCase(match, u"c​lawfu​l")]), input)
    input = re.sub(re4, lambda match: matchCase(match, u"claws"), input)
    input = re.sub(re5, lambda match: matchCase(match, u"kitten"), input)
    input = re.sub(re6, lambda match: matchCase(match, u"fu​rmilia​r"), input)
    input = re.sub(re7, lambda match: matchCase(match, u"fu​r"), input)
    input = re.sub(re8, lambda match: matchCase(match, u"whiske​r"), input)
    input = re.sub(re9, lambda match: matchCase(match, u"mew"), input)
    input = re.sub(re10, lambda match: matchCase(match, u"pu​r​r"), input)
    input = re.sub(re11, lambda match: matchCase(match, u"pu​r​r"), input)
    input = re.sub(re12, lambda match: matchCase(match, u"fu​r​ry"), input)
    input = re.sub(re13, lambda match: matchCase(match, u"fu​r​"), input)
    input = re.sub(re14, lambda match: matchCase(match, u"meow"), input)
    input = re.sub(re15, 'owo' + r"\1", input)
    input = re.sub(re16, 'owo' + r"\1", input)
    input = re.sub(re17, 'owo' + r"\1", input)
    input = re.sub(re18, lambda match: matchCase(match, u"paws"), input)
    input = re.sub(re19, lambda match: matchCase(match, u"paws"), input)
    input = re.sub(re20, lambda match: matchCase(match, u"paw"), input)
    input = re.sub(re21, lambda match: matchCase(match, u"fu​r-end"), input)
    input = re.sub(re24, lambda match: matchCase(match, u"fe​line"), input)
    input = re.sub(re25, lambda match: matchCase(match, u"bork"), input)
    input = re.sub(re26, lambda match: matchCase(match, u"bite"), input)
    input = re.sub(re27, lambda match: matchCase(match, u"ruff"), input)
    input = re.sub(re30, lambda match: matchCase(match, u"owozone"), input)
    input = re.sub(re28, r"\1y\2", input)
    input = re.sub(re29, r"NY\1", input)
    input = re.sub(re31, lambda match: (" " + getOwO() if random.random() > 0.6 else "") + match.group(1), input)
    input = re.sub(re32, lambda match: " " + getOwO() + match.group(1), input) ##FIGURE OUT WHAT THIS POST NONSENSE IS ABOUT
    input = re.sub(re33, lambda match: matchCase(match, "w"), input)
    return input
