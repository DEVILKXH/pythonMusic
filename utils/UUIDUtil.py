# -*- coding: UTF-8 -*-
# -*- author: kexiaohong -*-
import uuid


def getuuid():
    UUID = uuid.uuid1()
    return str(UUID)