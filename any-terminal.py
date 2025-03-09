#! /usr/bin/env python3

import sys
import os
import subprocess
import json
import binascii

list_of_terminals_that_use_dash_c = ['vte']
list_of_terminals_that_use_xterm = ['screen', 'tmux', 'mosh']
list_of_terminals_that_use_no_dash = ['screen']

fixed_argv = sys.argv

if '+++anyterm+++' in fixed_argv:
    # konsole (at least in version 24_12_3) internally calls flatpak-spawn
    # but somehow shuffels --env=... parameters meant for flatpak-spawn
    # after the name of the executable to run in host.
    # Filter them out here.
    fixed_argv = [arg for arg in fixed_argv if not arg.startswith('--env')]

if len(fixed_argv) == 3 and fixed_argv[1] == '+++anyterm+++':
    args_cmd = json.loads(binascii.a2b_base64(fixed_argv[2]).decode())
    if not args_cmd:
        os.execvp("sh", ["sh"])
    else:
        os.execvp(args_cmd[0], args_cmd)
    sys.exit(0)


args_term = []
args_cmd = []

args = fixed_argv[1:]

script_path = os.path.realpath(__file__)


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
    inv_args = [*prefix, 'flatpak', 'run', term, '-c', 'run-in-host' + ' ' + script_path + ' +++anyterm+++ ' + encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)
elif any((term.startswith('de.uchuujin.fp.termzoo.' + x) for x in list_of_terminals_that_use_no_dash)):
    inv_args = [*prefix, 'flatpak', 'run', term, 'run-in-host', script_path, '+++anyterm+++', encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)
elif term.startswith('de.uchuujin.fp.termzoo.tmux'):
    inv_args = [*prefix, 'flatpak', 'run', term, 'new-session', 'run-in-host' + ' ' + script_path + ' +++anyterm+++ ' + encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)
elif (term.startswith('de.uchuujin.fp.termzoo.konsole1')
      or term.startswith('de.uchuujin.fp.termzoo.konsole20')
      or term.startswith('de.uchuujin.fp.termzoo.konsole21')
      or term.startswith('de.uchuujin.fp.termzoo.konsole22_03_')
      or term.startswith('de.uchuujin.fp.termzoo.konsole22_04_')):

    inv_args = [*prefix, 'flatpak', 'run', term, '-e', 'run-in-host', script_path, '+++anyterm+++', encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)
elif (term.startswith('de.uchuujin.fp.termzoo.konsole22_08_')
      or term.startswith('de.uchuujin.fp.termzoo.konsole22_12_')):
    # konsole automatically runs commands in host (since 22.08)
    # But fails to run commands not also in flatpak with "Could not find binary: " "/path/to/binary"
    inv_args = [*prefix, 'flatpak', 'run', term, '-e', '/bin/bash', '-c', script_path + ' +++anyterm+++ ' + encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)
elif term.startswith('de.uchuujin.fp.termzoo.konsole'):
    # konsole automatically runs commands in host (since 22.08)
    # since 23.04 it correctly handles executables not also in the flatpak
    inv_args = [*prefix, 'flatpak', 'run', term, '-e', script_path + ' +++anyterm+++ ' + encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)
    subprocess.check_call(inv_args)
elif term.startswith('de.uchuujin.fp.termzoo.mosh'):
    inv_args = [*prefix, 'flatpak', 'run', term, '--local', '--', '127.0.0.1', 'run-in-host', script_path, '+++anyterm+++', encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)
else:
    inv_args = [*prefix, 'flatpak', 'run', term, '-e', 'run-in-host', script_path, '+++anyterm+++', encoded]
    #print(inv_args)
    subprocess.check_call(inv_args)

