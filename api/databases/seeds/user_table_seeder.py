from masoniteorm.seeds import Seeder
from masonite.facades import Hash
from app.models.User import User
from app.models.UserType import UserType
from app.models.Contractor import Contractor

PEOPLE = [
    "Mary Price",
    "Nissant Browning",
    "Jennifer Bocanegra",
    "Alton R. Matthews",
    "Saul Salinas",
    "Mirtha Alexandra Garza",
    "Timothy Salas",
    "Jobsan Tovar",
    "Carlos Zapata",
]

DEFAULT_CONTRACTOR_NAME = "Default Contractor"
DEFAULT_PASSWORD = "welcome"  # will be hashed

def split_name(full):
    parts = full.strip().split()
    if len(parts) == 0:
        return "", "", ""
    if len(parts) == 1:
        return parts[0], "", ""
    if len(parts) == 2:
        return parts[0], "", parts[1]
    # 3+ parts: treat the middle as mname (join if multiple)
    fname = parts[0]
    lname = parts[-1]
    mname = " ".join(parts[1:-1])
    return fname, mname, lname

def make_email(full):
    import re
    base = re.sub(r"[^a-z0-9]+", ".", full.lower()).strip(".")
    return f"{base}@local.test"

class SeedUsersAndContractor(Seeder):
    def run(self):
        # ensure 'member' user type exists (fallback to first if missing)
        member = UserType.where("type", "member").first()
        if not member:
            # create minimal set if table is empty
            for t in getattr(UserType, "TYPE_CHOICES", ["member"]):
                UserType.update_or_create({"type": t}, {"active": True})
            member = UserType.where("type", "member").first()

        contractor = Contractor.update_or_create(
            {"name": DEFAULT_CONTRACTOR_NAME},
            {"active": True},
        )

        for full in PEOPLE:
            fname, mname, lname = split_name(full)
            email = make_email(full)
            User.update_or_create(
                {"email": email},
                {
                    "fname": fname,
                    "mname": mname,
                    "lname": lname,
                    "password": Hash.make(DEFAULT_PASSWORD),
                    "user_type_id": member.id if member else None,
                    "contractor_id": contractor.id,
                },
            )
