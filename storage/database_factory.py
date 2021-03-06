from peewee import MySQLDatabase
from environment import Environment
from discord.ext import tasks


class DatabaseFactory:
    def __init__(self):
        env = Environment()
        self.config = env.get_config()
        self._database = None
        # self.stay_alive.start()

    def get_database_connection(self):
        if self._database is None:
            self._database = MySQLDatabase(self.config.get("Database", "Database"),
                                           port=int(self.config.get("Database", "Port")),
                                           host=self.config.get("Database", "Host"),
                                           user=self.config.get("Database", "User"),
                                           password=self.config.get("Database", "Password"),
                                           charset='utf8mb4'
                                           )

        return self._database

    @tasks.loop(seconds=30)
    async def stay_alive(self):
        self.get_database_connection().connection().ping(True)
