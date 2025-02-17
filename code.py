from django.contrib import admin​
​
from django.urls import path, include​
from django.conf import settings​
​
from django.conf.urls.static import static​
urlpatterns = [​
    path('', include('ml_app.urls')),​] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)​
​
import os​
​
from django.core.asgi import get_asgi_application​
​
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_settings.settings’)​
​
application = get_asgi_application()​
​
import os​
import sys​
​
def main():​
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_settings.settings')​
    try:​
        from django.core.management import execute_from_command_line​
    except ImportError as exc:​
        raise ImportError(​
            "Couldn't import Django. Are you sure it's installed and "​
            "available on your PYTHONPATH environment variable? Did you "​
            "forget to activate a virtual environment?"​
        ) from exc​
    execute_from_command_line(sys.argv)​
​
if __name__ == '__main__':​
    main()​
​
​
​
​
