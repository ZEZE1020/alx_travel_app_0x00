from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_locations = ['Nairobi', 'Mombasa', 'Kisumu', 'Naivasha', 'Diani']
        titles = ['Cozy Cottage', 'Beachfront Villa', 'Urban Apartment', 'Mountain Cabin', 'Luxury Suite']

        for i in range(10):
            Listing.objects.create(
                title=random.choice(titles),
                description='A beautiful place to stay with all amenities.',
                location=random.choice(sample_locations),
                price_per_night=random.uniform(50, 300),
                available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings'))
