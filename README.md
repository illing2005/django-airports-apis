django-airports-apis
=====
Airport data for Django. Using different API Endpoints

Basic setup
-
Install django-airports-apis via [PyPI][]
```
pip install django-airports-apis
```

Add airports to installed apps and configure your preferred API:
```
# settings.py
INSTALLED_APPS = (
    ...
    'airports'
    ...
)

AIRPORT_API = {'openflights': ('airports.openflights.OpenFlights',{})}
```

Then run `/manage.py migrate` to sync your database. 

Call the management command to fetch airports from the selected API (this may take a while):
```
/manage.py load_airports
```

Provided API Backends
-
[openflights.org][]

Openflights provides free English airport data. 
You don't need to register to use this API:
```
# settings.py
AIRPORT_API = {'openflights': ('airports.openflights.OpenFlights',{})}
```

[flightstats.com][]

Go to [flightstats.com] and register for an account. As soon as your account is active you can use the multilingual airport data. At the moment it supports 8 different languages:
English, Simplified Chinese, Japanese, German, Spanish, French, Portuguese, and Arabic
```
# settings.py
AIRPORT_API = {'flighstats': ('airports.flightstats.Flightstats',
                              {'app_id' : '1234asdfc',
                               'app_key' : 'asg5j67hzergrgevwe'}),}
```

[flightstats.com]: http://www.flightstats.com
[openflights.org]: http://openflights.org/data.html
[PyPI]: https://pypi.python.org/pypi/murcss
