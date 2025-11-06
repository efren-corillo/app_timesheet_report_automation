# databases/seeds/UserTypeSeeder.py
from masoniteorm.seeds import Seeder
from app.models.UserType import UserType

class UserTypeSeeder(Seeder):
    def run(self):
        for t in UserType.TYPE_CHOICES:
            UserType.update_or_create({"type": t}, {"active": True})
