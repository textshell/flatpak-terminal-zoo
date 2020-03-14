#! /usr/bin/python3

import os
import subprocess
import tempfile


installed = set()
available = {}

r = subprocess.run(['flatpak', 'list', '--columns=application'], stdout=subprocess.PIPE, check=True)
for name in r.stdout.decode().split('\n'):
    if name.startswith('de.uchuujin.fp.termzoo.'):
        installed.add(name)


for path, dirs, files in os.walk('.'):
    for file in files:
        if file.startswith('de.uchuujin.fp.termzoo.') and file.endswith('.json'):
            available[file[:-5]] = path


installed_only = installed - available.keys()
if installed_only:
    print('installed by no build manifest', sorted(installed_only))


to_build = available.keys() - installed
if to_build:
    print('build manifest but not yet installed', sorted(to_build))

for name in sorted(to_build):
    with tempfile.TemporaryDirectory(dir='.') as tmp:
        cmd = ['flatpak-builder', '--install', '--user', tmp, available[name] + '/' + name + '.json']
        print('running: ', cmd)
        subprocess.run(cmd, check=True)

