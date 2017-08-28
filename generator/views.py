from django.http import HttpResponse
import random

kilo = bytearray([random.randint(0, 255) for r in range(1024**1)])
mega = bytearray([random.randint(0, 255) for r in range(1024**2)])
giga = bytearray([random.randint(0, 255) for r in range(1024**3)])


def main(request):
    if request.method != 'GET':
        return HttpResponse(400)

    size = request.GET.get('size', -1)

    if size < 0:
        return HttpReponse(400)
    elif size > 1024**3:
        return HttpResponse(500)
    
    # Generar data
    data = b''
    while size > 1024**3:
        data += giga
        size -= 1024**3
    while size > 1024**2:
        data += mega
        size -= 1024**2
    while size > 1024**1:
        data += kilo
        size -= 1024**2
    data += bytearray([random.randint(0, 255) for r in range(size)])

    response = HttpResponse(data, content_type='application/octet-stream')

    return response
