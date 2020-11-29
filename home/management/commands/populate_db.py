from django.core.management.base import BaseCommand
from home.models import mk, vald, linn
import ast


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):
        # with open('home/management/commands/addresses.csv', "r") as data:
        #     dictionary = ast.literal_eval(data.read())
        #     for key in dictionary:
        #         mk.objects.create(maakond=key)

        # with open('home/management/commands/addresses.csv', "r") as data:
        #     dictionary = ast.literal_eval(data.read())
        #     for a in dictionary:
        #         for b in dictionary[a]:
        #             maakond_from_db = mk.objects.get(maakond=a)
        #             vald.objects.create(vald=b, maakond_id=maakond_from_db.id)


        with open("home/management/commands/addresses.csv", "r") as data:
            dictionary = ast.literal_eval(data.read())
            for a in dictionary:
                for b in dictionary[a]:
                    for c in dictionary[a][b]:
                        if " linn" in c:
                            vald_from_db = vald.objects.get(vald=b)
                            linn.objects.create(linn=c, vald_id_id=vald_from_db.id)

        # mk.objects.all().delete()

    def handle(self, *args, **options):
        self._create_tags()
