from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect


def api_swagger(request):
    response =  HttpResponse()
    try:
        response["Content-Type"] = "text/plain"
        response['X-Accel-Redirect'] = '/media/' + "swagger.yaml"
    except Exception:
        raise Http404
    return response


