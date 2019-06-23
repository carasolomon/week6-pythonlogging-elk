import logging
import logstash
import sys
import time

t_logger = logging.getLogger('python-logstash-logger')
t_logger.setLevel(logging.INFO)
t_logger.addHandler(logstash.LogstashHandler('52.14.84.187', 5959, version=1))

t_logger.error('python-logstash: test error')
t_logger.info('python-logstash: test info')
t_logger.warning('python-logstash: test warning')

extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b':'c'},
    'test_float': 3.90,
    'test_integer': 30,
    'test_list': [100, 200, 300],
}
t_logger.info('python-logstash: test extra fields', extra=extra)