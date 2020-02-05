Getting started with objcache
**********************************

Install
=======

Install via::

    pip install objcache

Usage
=========

Some highlighted functionality.

This is a simple example::

    >>> from objcache import ObjectCache

    >>> cache = ObjectCache('cache.zodb', ('a', 'b'))
    >>> cache.store(5)

    # Later session
    >>> cache = ObjectCache('cache.zodb', ('a', 'b'))
    >>> result = cache.get()
    >>> print(result)
    5


