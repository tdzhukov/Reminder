import datetime
import dateutil.parser
import re
import time

# pylint: disable=unused-wildcard-import
from init import *


def try_parse_timezone(message_text):
    """string -> int option"""
    global config
    try:
        if re.match(config["timezone_schema"], message_text) is None:    # UTC SHH:MM
            return None                                                  # 0123456789
        sign = 1 if message_text[4] == '+' else -1
        hours = int(message_text[5:7])
        minutes = int(message_text[8:10])
        if hours > 14:
            return None
        if minutes > 59:
            return None
        return sign * (hours * 60 + minutes)
    except TypeError:
        return None


def try_parse_datetime(message_text):
    """string -> datetime option"""
    global config
    try:
        return dateutil.parser.parse(message_text, ignoretz=True, dayfirst=True)
    except ValueError:
        print("oops :(")
        return None
