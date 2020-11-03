def log_to_file(message):
    pass


def log_to_screen(message):
    print(message)


def logger(target):
    if target == 'screen':
        return log_to_screen
    else:
        return log_to_file


log = logger('screen')

log('Testing')
