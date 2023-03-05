from environs import Env

# Using enviorns library
env = Env()
env.read_env()

# .env file we read the following
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # Admins list
IP = env.str("ip")  # Host IP adress
