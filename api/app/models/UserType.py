""" UserType Model """
from masoniteorm.models import Model

class UserType(Model):
    """UserType Model"""

    __table__ = "user_types"
    __fillable__ = ["type", "active"]
    __hidden__ = ["created_at", "updated_at"]

    TYPE_CHOICES = ["superadmin", "admin", "supervisor", "contractor"]

    # Reverse relation
    def users(self):
        return self.has_many("app.models.User")
