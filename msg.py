# import logging

def msg(*args, skip_before=True, skip_after=False):
    for thing in enumerate(args):
        m = "BETS-package:" + args

        if skip_before:
            k = "\n" + m

        if skip_after:
            k = m + "\n"

        print(k)
