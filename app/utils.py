import os
import re
import hashlib


def read_env(basedir=None):
    """
    Reads local default environment variables from a .env file located in the
    project root directory.
    """

    try:
        if basedir is None:
            envpath = '.env'
        else:
            envpath = os.path.join(basedir, '.env')
        with open(envpath) as hd:
            content = hd.read()
    except IOError:
        content = ''

    for line in content.splitlines():
        m1 = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
        if m1:
            key, val = m1.group(1), m1.group(2)
            m2 = re.match(r"\A'(.*)'\Z", val)
            if m2:
                val = m2.group(1)

            m3 = re.match(r'\A"(.*)"\Z', val)
            if m3:
                val = re.sub(r'\\(.)', r'\1', m3.group(1))

            os.environ.setdefault(key, val)
