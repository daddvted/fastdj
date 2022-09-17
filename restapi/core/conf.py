# Use command below to generate secret key:
# openssl rand -hex 32
SECRET_KEY = '52b0d5c1d8d1418ce615ecab1795a31b808040731d349f85a4c0135b3e910643'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60


PROJECT_TITLE = 'Project FastDJ'
PROJECT_DESC = 'FastAPI and Django Mixin'
API_PREFIX = '/api'

LOG_MAX_BYTES = 1024*1024*10 # 10M
LOG_BACKUP_COUNT= 10
LOG_FORMAT = "%(asctime)s [%(levelname)s] [%(process)d] [%(filename)s:%(lineno)s - %(funcName)s()] %(message)s"