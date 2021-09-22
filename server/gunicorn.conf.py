accesslog = '/tmp/gunicorn.log'

workers = 5
threads = 2

keyfile = '/etc/letsencrypt/live/voip.csie.org/privkey.pem'
certfile = '/etc/letsencrypt/live/voip.csie.org/cert.pem'
