#! /usr/bin/env python3

import sys
import os
import subprocess
import json
import binascii

list_of_terminals_that_use_dash_c = ['vte']
list_of_terminals_that_use_xterm = ['screen', 'tmux', 'mosh']
list_of_terminals_that_use_no_dash = ['screen']

if len(sys.argv) == 3 and sys.argv[1] == '+++anyterm+++':
    args_cmd = json.loads(binascii.a2b_base64(sys.argv[2]).decode())
    if not args_cmd:
        os.execvp("sh", ["sh"])
    else:
        os.execvp(args_cmd[0], args_cmd)
    sys.exit(0)


args_term = []
args_cmd = []

args = sys.argv[1:]

if '--' in args:
    args_term = args[:args.index('--')]
    args_cmd = args[args.index('--') + 1:]
else:
    args_term = args
    
if not args_term:
    print('Missing terminal id to run')
    print('Usage: any-terminal.py <terminal id> [-- <command> [<arg>]*]')
    sys.exit(1)
else:
    term = args_term.pop(0)
    
encoded = binascii.b2a_base64(json.dumps(args_cmd).encode()).decode().strip()

if '.' not in term:
    term = 'de.uchuujin.fp.termzoo.' + term

prefix = []

if any((term.startswith('de.uchuujin.fp.termzoo.' + x) for x in list_of_terminals_that_use_xterm)):
    prefix = ['xterm', '-e']
    
if any((term.startswith('de.uchuujin.fp.termzoo.' + x) for x in list_of_terminals_that_use_dash_c)):
    inv_args = [*prefix, 'flatpak', 'run', term, '-c', 'run-in-host' + ' ' + __file__ + ' +++anyterm+++ ' + encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)
elif any((term.startswith('de.uchuujin.fp.termzoo.' + x) for x in list_of_terminals_that_use_no_dash)):
    inv_args = [*prefix, 'flatpak', 'run', term, 'run-in-host', __file__, '+++anyterm+++', encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)
elif term.startswith('de.uchuujin.fp.termzoo.tmux'):
    inv_args = [*prefix, 'flatpak', 'run', term, 'new-session', 'run-in-host' + ' ' + __file__ + ' +++anyterm+++ ' + encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)
elif term.startswith('de.uchuujin.fp.termzoo.mosh'):
    inv_args = [*prefix, 'flatpak', 'run', term, '--local', '--', '127.0.0.1', 'run-in-host', __file__, '+++anyterm+++', encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)
else:
    inv_args = [*prefix, 'flatpak', 'run', term, '-e', 'run-in-host', __file__, '+++anyterm+++', encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)

