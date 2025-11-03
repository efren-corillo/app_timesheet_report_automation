"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates


class User(Model, SoftDeletesMixin, Authenticates):
    """User Model."""

    __fillable__ = ["fname","mname","lname", "email", "password", "user_type_id"]
    __hidden__ = ["password"]
    __auth__ = "email"

    def type(self):
        """Relationship to UserType model."""
        return self.belongs_to("app.models.UserType", "user_type_id")