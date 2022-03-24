import logging
logging.basicConfig(filename='app.log',encoding='utf-8', level=logging.DEBUG, format='%(clientip)s %(asctime)s %(levelname)s %(message)s')
#d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logging.debug('Before you')
# logging.warning('%s before you %s', 'Looks', 'leap')
# logging.info('This should show in log')

# import logging
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This is debug message')