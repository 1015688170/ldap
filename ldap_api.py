#!/usr/bin/python3
# -*- coding:utf-8 -*-

from ldap3 import Server, Connection, SAFE_SYNC, ALL, HASHED_SALTED_SHA, MODIFY_REPLACE
from ldap3.utils.hashed import hashed
import time
import json
import re

# ldap info
ldap_server = '10.0.0.77'
ldap_user = 'cn=Manager,dc=xxx,dc=org,dc=cn'
ldap_pwd = '123456'
ldap_search_base = 'ou=People,dc=xxx,dc=org,dc=cn'


def search_user(user_name):
    conn = Connection(ldap_server, ldap_user, ldap_pwd, auto_bind=True)
    conn.search(ldap_search_base, '(cn=%s)' % user_name, attributes=['*'])
    entry = conn.entries
    print(json.loads(entry[0].entry_to_json()))


def add_user(user_name, user_passwd):
    conn = Connection(ldap_server, ldap_user, ldap_pwd, auto_bind=True)
    passwd = hashed(HASHED_SALTED_SHA, '%s' % user_passwd)
    conn.add('uid=%s,ou=People,dc=suweipeng,dc=org,dc=cn' % user_name, ['inetOrgPerson'],
             {'cn': '%s' % user_name, 'sn': '%s' % user_name, 'mail': '%s@mail.com' % user_name,
              'userPassword': '%s' % passwd})
    print(conn.result)


def modify_user(user_name, user_passwd):
    conn = Connection(ldap_server, ldap_user, ldap_pwd, auto_bind=True)
    passwd = hashed(HASHED_SALTED_SHA, '%s' % user_passwd)
    conn.modify('uid=%s,ou=People,dc=suweipeng,dc=org,dc=cn' % user_name,
                {'userPassword': [(MODIFY_REPLACE, ['%s' % passwd])]})
    print(conn.result)

