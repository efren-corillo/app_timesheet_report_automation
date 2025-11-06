"""Base Database Seeder Module."""
from masoniteorm.seeds import Seeder

from .user_table_seeder import UserTableSeeder
from .user_type_table_seeder import UserTypeTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(UserTableSeeder)
        self.call(UserTypeTableSeeder)
