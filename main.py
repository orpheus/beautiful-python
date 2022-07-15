"""
Beautiful is better than Ugly.
"""
import io
import os
import sys
import threading
from collections import defaultdict, ChainMap, namedtuple, deque
from contextlib import contextmanager
from functools import partial

"""
Looping over a range of  numbers:
    previously was `xrange()` (python2)
    currently creates an iterator over the range, producing the values
        one at a time
"""
for i in range(6):
    print(i)

"""
Looping over a collection:
    'C' way: "while i=0;i<n;i++"
        colors = ['red', 'blue', 'green']
        for i in range(len(colors)):
            print colors[i]
"""
colors = ['red', 'blue', 'green']
for c in colors:
    print(c)

"""
Looping backwards:
    'C' way: "while i=n-1;n>-1;n--"
        colors = ['red', 'blue', 'green']
        for i in range(len(colors)-1, -1, -1,):
            print colors[i]
"""
colors = ['red', 'blue', 'green']
for c in reversed(colors):
    print(c)

"""
Looping over a collection and indices:
    'C' way: "already using the iterator""
        colors = ['red', 'blue', 'green']
        for i in range(len(colors)):
            print(i, '->', colors[i])
"""
colors = ['red', 'blue', 'green']
for i, color in enumerate(colors):
    print(i, '->', color)

"""
Looping over two collections at once:
    'C' way: take the shorter array length and loop by index
        colors = ['red', 'blue', 'green']
        names = ['ryan', 'erik', 'luna', 'drew']
        n = min(len(names), len(colors))
        for i in range(len(colors)):
            print(name[i], '->', colors[i])
"""
colors = ['red', 'blue', 'green']
names = ['ryan', 'erik', 'luna', 'drew']
for color, name in zip(colors, names):
    print(color, '->', name)

"""
Looping in sorted order:
"""
colors = ['red', 'blue', 'green']
for c in sorted(colors):
    print(c)

"""
Looping in custom sort order:
    Old way: use custom compare function (`cmp`)
    New way: using `key` function. Called once per key.
"""
colors = ['red', 'blue', 'green']
for c in sorted(colors, key=str):
    print(c)

"""
Call a function until a sentinel value
    Old way:
        f = io.StringIO("some initial text data")
        blocks = []
        while True:
            block = f.read(32)
            if block == '':
                break
            blocks.append(block)
    New way:
        Using iter allows you to pass in a function that gets called
        over and over until it hits the sentinel value. `iter`` takes a 
        function with no arguments, so we use `partial`.
        
        "Partial takes a function of many arguments and makes a function
        of fewer arguments"
        
        "The moment you've made something iterable, you've done something 
        magic with your code."
        
        You can feed it to set, sorted, min, max, heap, queue, sum, etc.
        
        As soon as you've made something iterable, it works with the rest
        of the python toolkit.
    
    Note:
        Can use `iter` for any functionality that needs to be called multiple
        times until some value is returned.
"""
# Reading 32 bytes at a time
f = io.StringIO("some initial text data")
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

# More obvious stop
f = io.StringIO("Break my Loop")
for letter in iter(partial(f.read, 1), 'L'):  # Stops at `L`
    print('Break an iter Loop: ', letter)

# Looping over an iterable made with iter and f.read
f = io.StringIO('Ryan')
for i in iter(f.read(4)):
    print('Loop over Iterable: ', i)


def no_break(seq):
    """
    Multiple Exit Points in Loops:
        the for-else construct
    """
    for index, value in enumerate(io.StringIO('Ryan').read(4)):
        if value == seq:
            break
    else:
        return 'no_break found'
    return 'break found', index


print(no_break('x'))
print(no_break('n'))

"""
Dictionaries

"There are two types of people in this world:
Those who've mastered dictionaries and total goobs." - Raymond Hettinger
"""

"""
Looping over dictionary keys
"""
d = {'ryan': 'blue', 'erik': 'green', 'shane': 'red'}
for k in d:
    print(k)

"""
You cannot mutate an object while iterating over it, if you do, 
"you're living in a tatue of sin".

d.keys() in python2 would make a copy of the keys into a list that you
could iterate over and mutate the original object.

In python3, you use `list(some_dict)` to return a copy of the keys.
"""
for k in list(d):
    if k.startswith('r'):
        del d[k]

"""
Looping over keys and values at the same time:
"""
d = {'ryan': 'blue', 'erik': 'green', 'shane': 'red'}
for k in d:
    print(k, '->', d[k])  # d[k]: Not fast. Has to re-hash every key and do a look-up on it

for k, v in d.items():  # .items(): provides an iterable set on a view of the items
    print(k, '-> ', v)

"""
Construct a Dictionary From Pairs:
    zip again!
        see how beautifully the python functions work together?
"""
colors = ['red', 'blue', 'green']
names = ['ryan', 'erik', 'luna', 'drew']
zip_dict = dict(zip(colors, names))
print('dict(zip( ', zip_dict)

# noinspection PyTypeChecker
enum_dict = dict(enumerate(names))
print('dict(enumerate( ', enum_dict)

"""
Counting with Dictionaries:
    Do not teach beginners this. Have them start off with looping 
    and learning the .get(key, defaultValue) fn or checking for keys first
"""
colors = ['red', 'blue', 'green', 'red', 'red', 'green']
d = defaultdict(int)  # `int` can be called with 0 arguments results in 0
for c in colors:
    d[c] += 1
print(dict(d))  # defaultdict has to be converted back

"""
Grouping with dictionaries:
"""
# Beginner Way
names = ['ryan', 'erik', 'luna', 'drew', 'jordan', 'bri', 'molly', 'sarah']
d = {}
for n in names:
    l_key = len(n)
    if l_key not in d:
        d[l_key] = []
    d[l_key].append(n)
print(d)

# setdefault
names = ['ryan', 'erik', 'luna', 'drew', 'jordan', 'bri', 'molly', 'sarah']
d = {}
for n in names:
    key = len(n)
    d.setdefault(key, []).append(n)  # returns value at key with default set to [] if None
print(d)

# defaultdict
names = ['ryan', 'erik', 'luna', 'drew', 'jordan', 'bri', 'molly', 'sarah']
d = defaultdict(list)  # sets the default value for any key to a list
for n in names:
    key = len(n)
    d[key].append(n)
print(dict(d))

"""
Atomic popitem():
    popitem() is atomic and can be safely used between threads to 
    pull tasks
    
    Doesn't seem to guarantee which one it pops?
"""
d = {'one': 1, 'two': 2, 'three': 3}
while d:
    key, value = d.popitem()
    print(key, '->', value)

"""
Linking Dictionaries:
    Old way that copies a bunch of data:
        d = defaults.copy()
        d.update(env_vars)
        d.update(cmd_line_args)
"""
defaults = {"name": "ryan", "age": 23, "city": "Utah"}
env_vars = {"age": 26}
cmd_line_args = {"name": "roark", "city": "San Diego"}
d = ChainMap(cmd_line_args, env_vars, defaults)
print(dict(d))

"""
Improving Clarity

1. Use named keywords. Reduces obscurity, leads to less bugs.
"""
namedtuple(typename='TypeName', field_names=['wins', 'losses'])

"""
2. Use NamedTuples for return values. Increases Readability.
"""
score_board = (0, 3)
print(score_board)
ScoreBoard = namedtuple('NamedTuple', ['wins', 'losses'])
score_board = ScoreBoard(3, 0)
print(score_board)

"""
3. Unpacking sequences
"""
p = 'Ryan', 'Andrew', 'Chacon'
first, middle, last = p  # vs p[0], p[1], etc
print(first, middle, last)

"""
4. Updating Multiple State Values
"""


def fib_bad(n):
    x = 0
    y = 1
    for _ in range(n):
        print(x)
        t = y
        y = x + y
        x = t


def fib_good(n):
    x, y = 0, 1
    for _ in range(n):
        print(x)
        x, y = y, x + y


fib_bad(5)
fib_good(5)

"""
Joining strings:
"""
names = ['ryan', 'erik', 'luna', 'drew']
print(', '.join(names))

"""
Updating Sequences:
"""
# Slow
names = ['ryan', 'erik', 'luna', 'drew']
del names[0]
print(names)

names.pop(0)
print(names)

names.insert(0, 'copper')
print(names)

# Fast

names = deque(['ryan', 'erik', 'luna', 'drew'])
del names[0]
print(names)

names.popleft()
print(names)

names.appendleft('copper')
print(names)

"""
Decorators and Context Managers:
    1. Helps separate business logic from administrative logic
    2. Clean, beautiful tools for factoring code and improving code reuse
    3. Good naming essentials
"""

"""
Making a lock:
    Old Way:
        lock = threading.Lock()
        lock.acquire()
        try:
            print("Lock 1")
        finally:
            lock.release()
"""

lock = threading.Lock()
with lock:
    print('Lock Ctx Manager')

"""
Ignoring try/except exceptions:
    Old Way:
        try:
            os.remove('tmpfile')
        except OSError:
            pass
"""


@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass


with ignored(OSError):
    os.remove('tmpfile')

"""
Redirecting StdOut
    Old Way:
        with open('help.txt', 'w') as f:
            oldstdout = sys.stdout
            sys.stdout = f
            try:
                help(pow)
            finally:
                sys.stdout = oldstdout

"""


@contextmanager
def redirect_stdout(file_obj):
    oldstdout = sys.stdout
    sys.stdout = file_obj
    try:
        yield file_obj
    finally:
        sys.stdout = oldstdout


with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)

"""
List Comprehension and Generator Expressions:
    Old Way:
        results = []
        for i in range(10):
            results.append(i**2)
        print(sum(results))
"""
results = [x ** 2 for x in range(10)]
print(sum(results))

print(sum(x ** 2 for x in range(10)))
