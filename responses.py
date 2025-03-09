import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'hey!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help': 
        return 'why are you looking for help'