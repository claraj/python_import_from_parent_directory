# Example main module, this could be a flask app or whatever.

from api import park_api

park = park_api.get_park()   # note that we don't need to import the Park class to do this.

print(park.name)