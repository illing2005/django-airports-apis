django-airports-apis
=====
Airport data for Django. Using different API Endpoints

Features
-
1. Fetch Airport data from different API's
2. django-modeltranslation support
3. Basic views and serializers for django-rest-framework

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
/manage.py load_airports            #fetches airport data from API
/manage.py load_airports --flush    #deletes all airport records
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

Modeltranslation
-
The package supports [django-modeltranslation][] out of the box. If the API supports different languages (like flightstats.com), the management command will automatically fetch the languages specified in your settings.py.

Rest Framework
-
The package also includes some basic support for [django-rest-framework][]. To activate the views simply include the urls in your urls.py:
```
#urls.py
urlpatterns = patterns('',
    ...
    url(r'api/',include('airports.urls'),),
    ...
)
```

Example Application
-
Please see the `example` application. This was used to test the developed features. It also serves as a nice quicklook into django-airport-apis. 

[django-rest-framework]: http://www.django-rest-framework.org/
[django-modeltranslation]: https://github.com/deschler/django-modeltranslation
[flightstats.com]: http://www.flightstats.com
[openflights.org]: http://openflights.org/data.html
[PyPI]: https://pypi.python.org/pypi/murcss
