"""CreateUserTypeTable Migration."""

from masoniteorm.migrations import Migration


class CreateUserTypeTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("user_types") as table:
            table.increments("id")
            table.enum("type", ["superadmin","admin","supervisor","contractor"]).default("contractor")
            table.boolean("active").default(True)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("user_types")
