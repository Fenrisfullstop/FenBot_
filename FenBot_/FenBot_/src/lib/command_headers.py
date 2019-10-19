from src.config.config import *
commands = {
	'!isthebotalive': {
		'limit': 30,
		'return': 'Probably'
	},
    '!spotify': {
        'limit': 30,
        'return': 'https://open.spotify.com/user/fenrisfullstop'
    },
}
for channel in config['channels']:
	for command in commands:
		commands[command][channel] = {}
		commands[command][channel]['last_used'] = 0
