import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, State, Region, Iso


def run():
    fhand = open('scripts/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    for row in reader:
        print(row[10])

        a = row[0]
        b = row[1]
        c = row[2]
        try:
            d = float(row[3])
        except:
            d = None
        e = row[4]
        f = row[5]
        try:
            g = float(row[6])
        except:
            g = None
        h, created = Category.objects.get_or_create(name=row[7])
        i, created = State.objects.get_or_create(name=row[8])
        j, created = Region.objects.get_or_create(name=row[9])
        k, created = Iso.objects.get_or_create(name=row[10])

        l = Site(name=a, description=b, justification=c, year=d, longitude=e, latitude=f, area_hectares=g, category=h,
                 state=i, region=j, iso=k)
        l.save()

