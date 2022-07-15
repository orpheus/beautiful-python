"""
Beautiful is better than Ugly.
"""
import io
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


