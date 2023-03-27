from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili

DB_USER = env.str("DB_USER")  # Postgres user
DB_PASS = env.str("DB_PASS")  # Postgres parol
DB_HOST = env.str("DB_HOST")  # Postgres host
DB_NAME = env.str("DB_NAME")  # Postgres nomi
