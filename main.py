import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'organ_donation_project.settings')
django.setup()

from organ_donation_app.models import Donor


new_donor = Donor(name='Sarang', age=20, blood_group='O+', organ_to_donate='Eyes',contact_number='9879879876',email='sarang@gmail.com')
new_donor.save()