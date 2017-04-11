# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
import types


def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g=g.next()
    return g