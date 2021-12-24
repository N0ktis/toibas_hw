from django.db.models import Q

from .models import Passwords, Logins
from django.http import HttpResponse

def home(request):
    return HttpResponse


def check_hash(request, hash_type, login, password):
    if hash_type == 'sha256':
        passwords = Passwords.objects.get(Q(sha256__startswith=password))
        logins = Logins.objects.get(Q(sha256__startswith=login))
    elif hash_type == 'sha512':
        passwords = Passwords.objects.get(Q(sha512__startswith=password))
        logins = Logins.objects.get(Q(sha512__startswith=login))
    elif hash_type == 'md4':
        passwords = Passwords.objects.get(Q(md4__startswith=password))
        logins = Logins.objects.get(Q(md4__startswith=login))
    elif hash_type == 'md5':
        passwords = Passwords.objects.get(Q(md5__startswith=password))
        logins = Logins.objects.get(Q(md5__startswith=login))
    elif hash_type == 'crc32':
        passwords = Passwords.objects.get(Q(crc32__startswith=password))
        logins = Logins.objects.get(Q(crc32__startswith=login))
    elif hash_type == 'keccak256':
        passwords = Passwords.objects.get(Q(keccak256__startswith=password))
        logins = Logins.objects.get(Q(keccak256__startswith=login))
    else:
        return None
    print(logins)
    print(passwords)
    return None
