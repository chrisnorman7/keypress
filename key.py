"""Play / pause."""

import win32con
from win32api import MapVirtualKey, keybd_event
from argparse import ArgumentParser

keys = {}

for x in dir(win32con):
    if x.startswith('VK_'):
        keys[x[3:].lower()] = getattr(win32con, x)

parser = ArgumentParser()

parser.add_argument(
    'key',
    nargs='?',
    choices=keys.keys(),
    help='The key to press.'
)

args = parser.parse_args()

if args.key is None:
    print('Keys I know about:')
    for key, value in keys.items():
        print('%s => %d' % (key, value))
else:
    v = keys[args.key]
    c = MapVirtualKey(v, 0)
    keybd_event(v, c)
