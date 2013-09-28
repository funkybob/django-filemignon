
from django.http import HttpResponse, HttpResponseNotAllowed
from django.conf import settings

import os.path

storage = settings.FILEMIGNON_STORAGE

def dir_list(request, path):
    dirs, files = storage.listdir(path)

    return JsonResponse({
        'directories': [
            {
                'name': name,
            }
            for name in dirs
        ],
        'files': [
            {
                'name': name,
                # 'size': 
                'created': storage.created_time(os.path.join(path, name)),
                'modified': storage.modified_time(os.path.join(path, name)),
            }
            for name in files
        ],
    })

def delete(request, filename):
    try:
        storage.delete(filename)
        return HttpResponse(status_code=204)
    except NotImplementedError as ex:
        return HttpResponseNotAllowed(str(ex))

