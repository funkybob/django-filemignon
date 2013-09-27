from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponseNotAllowed

storage = settings.FILEMIGNON_STORAGE

def delete(request, filename):
    try:
        storage.delete(filename)
        return HttpResponse(status_code=204)
    except NotImplementedError as ex:
        return HttpResponseNotAllowed(str(ex))
