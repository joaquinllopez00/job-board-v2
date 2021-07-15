import random
from mimesis import Person, Text, Address
from django.core.management.base import BaseCommand
from user.models import User
from job.models import CATEGORY_TYPE, JOB_TYPE, Listing, SALARY_TYPE


class Command(BaseCommand):
    help = "Creates or adds a db w/ pseudo users & listings"

    def handle(self, *args, **options):
        person = Person()
        text = Text()
        address = Address("EN")

        self.stdout.write(f"Creating test objects...")

        try:

            if not User.objects.filter(username="test"):

                user = User.objects.create_user(
                    username="test",
                    password="asdf",
                    bio=text.text(),
                    email=f"{text.word()}@{text.word()}.com",
                    name="ThisIsThe TestUser"
                )

                self.stdout.write(self.style.SUCCESS(
                    "Sucessfully created test user!"))

                self.stdout.write(f"Creating test listing...")

                if not Listing.objects.filter(title="testListing"):

                    Listing.objects.create(
                        user=user,
                        title="testListing",
                        description=text.text(),
                        location=f"{address.city()}, {address.state()}",
                        category=random.choice(CATEGORY_TYPE)[0],
                        compensation=random.choice(SALARY_TYPE)[1][0][0],
                        job_type=random.choice(JOB_TYPE)[0]
                    )

                    self.stdout.write(self.style.SUCCESS(
                        "Sucessfully created test listing!"))
            else:
                self.stdout.write(self.style.WARNING(
                    "Test user or listing already present! Skipping..."))

        except Exception as error:
            self.stdout.write(self.style.ERROR(
                f"Bootstrap_db encountered error \"{error}\" and will not create a test user."))
            return

        self.stdout.write("Creating many users & listings...")

        for _ in range(20):

            try:

                user = User.objects.create_user(
                    username=person.username(),
                    password=person.password(),
                    bio=text.text(),
                    email=f"{text.word()}@{text.word()}.com",
                    name=person.full_name()
                )

                Listing.objects.create(
                    user=user,
                    title=person.occupation(),
                    description=text.text(),
                    location=f"{address.city()}, {address.state()}",
                    category=random.choice(CATEGORY_TYPE)[0],
                    compensation=random.choice(SALARY_TYPE)[1][0][0],
                    job_type=random.choice(JOB_TYPE)[0]
                )

                self.stdout.write(self.style.SUCCESS(
                    "Sucessfully created many users & listings!"))

            except Exception as error:
                self.stdout.write(self.style.ERROR(
                    f"Bootstrap_db encountered error \"{error}\" and will not create any objects."))
                return
