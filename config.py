import configparser


def get_cognito_properties():
    config = configparser.RawConfigParser()
    config.read('config.properties')
    cognito_properties = dict(config.items('cognito'))
    return cognito_properties
