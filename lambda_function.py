import talib


def lambda_handler(event, context):
    return talib.get_functions()
