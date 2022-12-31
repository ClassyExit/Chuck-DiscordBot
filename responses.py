from API import *


def handle_response(message):
    message = message.lower()

    if 'quit' in message:
        return "A lot of times people look at the negative side of what they feel they can't do. I always look on the positive side of what I can do."

    if message == 'hello chuck':
        return "Hello there"

    if 'chuck' in message:
        return get_fact()
