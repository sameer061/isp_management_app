#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

# based on original package export.__version__ = "0.1.2" https://pypi.org/project/export/

# TODO: come up with something less lame
print("import export")

# FIX: hold my beer hommie
print("Do a barrel roll!")


from sys import modules


def export(o):
    """powered by finite state machine inside
    
    :o: function - what decorate
    """

    # 1.
    if o is None:
        # @TODO export(None)
        # __all__ = tuple()
        # modules[o.__module__].__all__ = tuple()
        return

    # 2.
    if __name__ == o.__name__ == o.__module__:
        # @sugar import export
        modules[o.__module__] = o
        return o

    modules[o.__module__].__dict__.setdefault('__all__', [])
    mod = modules[o.__module__]

    if type(mod.__all__) == tuple and len(mod.__all__) == 0:
        # 1.bis
        pass
    else:
        # 3. common way
        mod.__all__ = list(mod.__all__)
        mod.__all__.append(o.__name__)

    return o


# 2.bis
export(export)

##
# this the end
export.__version__ = "0.2.67.dev6"
