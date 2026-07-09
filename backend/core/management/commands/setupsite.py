from pathlib import Path

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from decouple import config

User = get_user_model()


class Command(BaseCommand):
    help = "Initial project setup."

    def handle(self, *args, **kwargs):

        username = config("ADMIN_USERNAME", default="admin")
        email = config("ADMIN_EMAIL", default="admin@example.com")
        password = config("ADMIN_PASSWORD", default="ChangeMe123!")

        # Create admin
        if not User.objects.filter(username=username).exists():

            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )

            self.stdout.write(
                self.style.SUCCESS(
                    "✓ Admin user created."
                )
            )

        else:

            self.stdout.write(
                self.style.WARNING(
                    "✓ Admin already exists."
                )
            )

        # Load initial data
        fixture = Path("initial_data.json")

        if fixture.exists():

            try:

                call_command("loaddata", "initial_data.json")

                self.stdout.write(
                    self.style.SUCCESS(
                        "✓ Initial data loaded."
                    )
                )

            except Exception as e:

                self.stdout.write(
                    self.style.WARNING(
                        f"Initial data not loaded: {e}"
                    )
                )

        else:

            self.stdout.write(
                self.style.WARNING(
                    "No initial_data.json found."
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                "\nProject setup completed successfully."
            )
        )