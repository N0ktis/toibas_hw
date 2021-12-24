from django.db import models


# Create your models here.
class Passwords(models.Model):
    sha256 = models.CharField(max_length=64)
    sha512 = models.CharField(max_length=128)
    md4 = models.CharField(max_length=32)
    md5 = models.CharField(max_length=32)
    crc32 = models.CharField(max_length=8)
    keccak256 = models.CharField(max_length=64)


class Logins(models.Model):
    sha256 = models.CharField(max_length=64)
    sha512 = models.CharField(max_length=128)
    md4 = models.CharField(max_length=32)
    md5 = models.CharField(max_length=32)
    crc32 = models.CharField(max_length=8)
    keccak256 = models.CharField(max_length=64)
