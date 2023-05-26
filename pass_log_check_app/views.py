from django.db.models import Q
from django.http import HttpResponse, JsonResponse

from .models import Passwords, Logins

ALLOWED_HASHES = ['sha256', 'sha512', 'md4', 'md5', 'crc32', 'keccak256']


def get_list_from_objects(query_set, attribute_name):
    return [getattr(data_object, attribute_name) for data_object in query_set]


def home(request):
    return HttpResponse('HELLO')
    # return render(request, 'pass_log_check_app/Home _ My Site 7.html')


def check_raw_url(request):
    get_request_keys = request.GET.keys()
    if 'hash_type' not in get_request_keys:
        return HttpResponse('No hash type')
    else:
        hash_type = request.GET['hash_type']
    if 'login' not in get_request_keys and 'password' not in get_request_keys:
        return JsonResponse({'logins': [], 'passwords': []})
    else:
        if 'login' in get_request_keys:
            login = request.GET['login']
        else:
            login = '-----'
        if 'password' in get_request_keys:
            password = request.GET['password']
        else:
            password = '-----'
    print(login, 'aaa')
    if len(login) <= 4 or len(password) <= 4 or hash_type not in ALLOWED_HASHES:
        return JsonResponse({'logins': [], 'passwords': []})
    return check_hash(request, hash_type, login, password)


def check_hash(request, hash_type, login, password):
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
    if login == '-----':
        return JsonResponse({'passwords': passwords_list})
    elif password == '-----':
        return JsonResponse({'logins': logins_list})
    else:
        return JsonResponse({'logins': logins_list, 'passwords': passwords_list})
