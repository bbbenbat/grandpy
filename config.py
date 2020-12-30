"""  Uses it to protect web forms against a nasty attack
called Cross-Site Request Forgery or CSRF """

import os


class Config(object):
    """ Use a secret key as a cryptographic key. """
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'hpkjjyuj5948Hj2'
