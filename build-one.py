#! /usr/bin/python3

import subprocess
import sys
import tempfile


with tempfile.TemporaryDirectory(dir='.') as tmp:
    cmd = ['flatpak-builder', '--install-deps-from=flathub', '--install', '--user', tmp, sys.argv[1]]
    print('running: ', cmd)
    subprocess.run(cmd, check=True)

