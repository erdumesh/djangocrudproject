from django.db import models, connection

# Create your models here.

class User(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Phone_Number = models.CharField(max_length=15, unique=True)
    Email_ID = models.EmailField(unique=True)
    Address = models.CharField(max_length=100)
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            # Use DELETE FROM instead of TRUNCATE for SQLite
            if connection.vendor == 'sqlite':
                print('I am using Sqlite Database')
                cursor.execute(f'DELETE FROM {cls._meta.db_table}')
            else:
                print("I am using MySql Database")
                cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table}')
