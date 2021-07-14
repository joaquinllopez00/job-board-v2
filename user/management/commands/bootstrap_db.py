from mimesis import Person, Text, Address, random
from django.core.management.base import BaseCommand
from user.models import User
from job.models import CATEGORY_TYPE, Listing, SALARY_TYPE


class Command(BaseCommand):
    help = "Creates or adds a db w/ pseudo users & listings"

    def handle(self, *args, **options):
        text = Text()
        address = Address("EN")

        self.stdout.write(f"Creating test user...")

        if not User.objects.filter(username='test'):

            User.objects.create_user(
                username="test",
                password="asdf",
                bio=text.text(),
                email=f'{text.word()}@{text.word()}.com',
                name='ThisIsThe TestUser'
            )

            self.stdout.write(self.style.SUCCESS(
                "Sucessfully created test user!"))
        else:
            self.stdout.write(self.style.WARNING(
                'Test user already present! Skipping...'))

        self.stdout.write(f"Creating test listing...")

        if not Listing.objects.filter(title='testListing'):

            Listing.objects.create(
                title="testListing",
                description=text.text(),
                location=f"{address.city()}, {address.state()}",
                category=random.get_random_item(CATEGORY_TYPE),
                compensation=random.get_random_item(SALARY_TYPE)
            )
            self.stdout.write(self.style.SUCCESS(
                "Sucessfully created test listing!"))
        else:
            self.stdout.write(self.style.WARNING(
                'Test listing already present! Skipping...'))
