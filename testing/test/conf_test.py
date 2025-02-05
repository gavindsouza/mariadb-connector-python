#!/usr/bin/env python -O
# -*- coding: utf-8 -*-

import os

def glob():
    dm = {
        "module": os.environ.get('TEST_MODULE', 'mariadb'),
        }
    return dm

def conf():
    d = {
        "user": os.environ.get('TEST_DB_USER', 'root'),
        "host": os.environ.get('TEST_DB_HOST', 'localhost'),
        "database": os.environ.get('TEST_DB_DATABASE', 'testp'),
        "port": int(os.environ.get('TEST_DB_PORT', '3306')),
    }
    if os.environ.get('TEST_REQUIRE_TLS'):
        if os.environ.get('TEST_REQUIRE_TLS') == "1":
            d["ssl"] = True
    if os.environ.get('TEST_RESET_SESSION'):
        d["pool_reset_connection"] = int(os.environ.get('TEST_RESET_SESSION', '1'))
    if os.environ.get('TEST_DB_PASSWORD'):
        d["password"] = os.environ.get('TEST_DB_PASSWORD')
    return d
