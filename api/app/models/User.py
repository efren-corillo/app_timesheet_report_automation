"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates
from .UserType import UserType
from .Contractor import Contractor

class User(Model, SoftDeletesMixin, Authenticates):
    __table__ = "users"
    __fillable__ = ["fname","mname","lname","email","password","user_type_id","contractor_id"]
    __hidden__ = ["password", "remember_token"]
    __auth__ = "email"
    __with__ = ("user_type", "contractor")

    def user_type(self):
        return self.belongs_to(UserType)

    def contractor(self):
        return self.belongs_to(Contractor)
