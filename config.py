MODE = 'work' # 'debug' or 'work' or 'test'
OPENAI_KEY = 'YOUR_API_KEY_HERE'
OPENAI_URL= "https://api.openai.com/v1/engines/text-davinci-002/completions"
RBMQ = {
    'host': 'host.docker.internal',
    'port': 5672,
    'user': 'guest',
    'password': 'guest',
    'vhost': '/'
}
SCHEDULE = 60 * 60 * 24 # seconds