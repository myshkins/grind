"""OT catchup validation function with helper functions"""
from typing import Union
import json

def skip(stale: str, curr_pos: int, count: int) -> Union[int, bool]:
    """
    takes stale string, current cursor position, and skip count as args and
    returns new cursor position. Returns False for invalid position.
    """
    if curr_pos + count >= len(stale) or curr_pos + count < 0:
        return False
    return curr_pos + count

def delete(stale: str, curr_pos: int, count: int) -> Union[str, bool]:
    """
    takes stale string, current cursor position, and delete count as args and
    returns new string after deletions. Returns False for invalid operation.
    """
    if count > (len(stale) - curr_pos):
        return False
    return stale[0:curr_pos] + stale[curr_pos+count:]

def insert(stale: str, curr_pos: int, chars: str) -> tuple[str,int]:
    """
    takes stale string, current cursor position, and characters to insert as
    args, and returns tuple of new string after insert and new cursor position.
    """
    new_str = chars.join([stale[0:curr_pos], stale[curr_pos:]])
    new_pos = curr_pos + len(chars)
    return (new_str, new_pos)

def is_valid(stale: str, latest: str, otjson: str) -> bool:
    """
    validation function that takes arguments old string, latest string, and
    operations. verifies that operations performed on old string result in new
    string.
    """
    cursor = 0
    temp_str = stale
    ops = json.loads(otjson)
    for op in ops:
        if op["op"] == "skip":
            result = skip(temp_str, cursor, op["count"])
            if not result:
                return False
            else:
                cursor = result
        elif op["op"] == "delete":
            result = delete(temp_str, cursor, op["count"])
            if not result:
                return False
            else:
                temp_str = result
        elif op["op"] == "insert":
            result = insert(temp_str, cursor, op["chars"])
            temp_str, cursor = result
    if temp_str == latest:
        return True
    else:
        return False

