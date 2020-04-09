import json
import os
import sys

import yaml
from django.core.management.base import BaseCommand

import os
from apps.users.models import User


class Command(BaseCommand):
    
    help = 'Manage users'

    def add_arguments(self, parser):
        
        parser.add_argument(
            '--email',
            required=False,
            dest='email',
        )

        parser.add_argument(
            '--username',
            required=False,
            dest='username',
        )

        parser.add_argument(
            '--password',
            required=False,
            dest='password',
        )

        parser.add_argument(
            '--db',
            required=False,
            choices=["flush", "select"],
            dest='database',
            help='specify database action, flush or select'
        )

    

    def handle(self, *args, **options):

        database = options['database']
        if str(database) == "flush":
            self.db_flush()
        if str(database) == "select":
            self.db_select()


        email = options["email"]
        username = options["username"]
        password = options["password"]
        if email and username and password:
            self.db_create_superuser(username, email, password)


    def db_flush(self):
        User.objects.all().delete()


    def db_select(self):
        users = User.objects.all()
        self.stdout.write("Found %s users" %(len(users)))
        for p in users:
            self.stdout.write(str(p))

    def db_create_superuser(self, username, email, password):
        User.objects.create_superuser(username, email, password)