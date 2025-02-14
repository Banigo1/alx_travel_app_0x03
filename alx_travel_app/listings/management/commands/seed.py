from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Sample data for seeding
        listings_data = [
            {
                'title': 'Cozy Cottage',
                'description': 'A cozy cottage in the woods.',
                'price_per_night': 100.00,
                'location': 'Forest Area',
            },
            {
                'title': 'Beachfront Villa',
                'description': 'A beautiful villa by the beach.',
                'price_per_night': 250.00,
                'location': 'Beach City',
            },
            {
                'title': 'Downtown Apartment',
                'description': 'An apartment located in the heart of the city.',
                'price_per_night': 150.00,
                'location': 'City Center',
            }
        ]

        # Create sample listings in the database
        for listing in listings_data:
            Listing.objects.create(**listing)

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
