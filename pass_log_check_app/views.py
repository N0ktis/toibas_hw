from django.db.models import Q
from django.http import HttpResponse, JsonResponse

from .models import Passwords, Logins


def get_list_from_objects(query_set, attribute_name):
    return [getattr(data_object, attribute_name) for data_object in query_set]


def home(request):
    return HttpResponse('HELLO')


def check_hash(request, hash_type, login, password):
    if len(login) <= 4 or len(password) <= 4:
        return JsonResponse({'logins': [], 'passwords': []})
    if hash_type == 'sha256':
        passwords = Passwords.objects.filter(Q(sha256__startswith=password))
        logins = Logins.objects.filter(Q(sha256__startswith=login))
    elif hash_type == 'sha512':
        passwords = Passwords.objects.filter(Q(sha512__startswith=password))
        logins = Logins.objects.filter(Q(sha512__startswith=login))
    elif hash_type == 'md4':
        passwords = Passwords.objects.filter(Q(md4__startswith=password))
        logins = Logins.objects.filter(Q(md4__startswith=login))
    elif hash_type == 'md5':
        passwords = Passwords.objects.filter(Q(md5__startswith=password))
        logins = Logins.objects.filter(Q(md5__startswith=login))
    elif hash_type == 'crc32':
        passwords = Passwords.objects.filter(Q(crc32__startswith=password))
        logins = Logins.objects.filter(Q(crc32__startswith=login))
    elif hash_type == 'keccak256':
        passwords = Passwords.objects.filter(Q(keccak256__startswith=password))
        logins = Logins.objects.filter(Q(keccak256__startswith=login))
    logins_list = get_list_from_objects(logins, hash_type)
    passwords_list = get_list_from_objects(passwords, hash_type)
    if login == '?':
        return JsonResponse({'passwords': passwords_list})
    elif password == '?':
        return JsonResponse({'logins': logins_list})
    else:
        return JsonResponse({'logins': logins_list, 'passwords': passwords_list})
