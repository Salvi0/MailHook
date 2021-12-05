import os
from dotenv import load_dotenv

load_dotenv()


class Emojis:
    def __init__(self):
        self.staff = '<:staff:884477446018199552>'
        self.yes = '<:yes:891993755786293298>'
        self.no = '<:no:891993740116381718>'
        self.loading = '<a:Loading:892010799994929192>'


class Logs:
    def __init__(self):
        self.cmds: int = 794621421162201108
        self.cmd_errs: int = 794621421162201108
        self.event_errs: int = 794621421162201108
        self.add_remove: int = 794621421162201108


class Config:
    def __init__(self):
        self.emojis = Emojis()
        self.logs = Logs()
        self.prefixes = ['<', '?']
        self.status = 'my dms'
        self.owners = [506513851576221706]
        self.client_secret = os.environ.get('CLIENT_SECRET')
        self.bot_lists = [733135548566470726, 333949691962195969]
        self.transcript_db_channel = 812094808213946399
