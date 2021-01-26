# import builtins
# builtins.__import__ = print

# from ..cat import behaviour
_temp = __import__('cat', globals(), locals(), ('behaviour',), 2)
behaviour = _temp.behaviour
behaviour.run()





def dance():
    print('某人在跳舞...')


