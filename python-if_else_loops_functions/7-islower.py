#!/usr/bin/python3

def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
