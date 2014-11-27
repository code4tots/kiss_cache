KISS Cache
==========

Step 1: Save data

```python

from kiss_cache import cache

cache.my_thing = [1, 2, 3, 4]

```

Step 2: Load data

```python

from kiss_cache import cache

print(cache.my_thing) # [1, 2, 3, 4]

```

Like `shelve` but even simpler.
