#! /usr/bin/env python3

from string import Template

KITTY_TEMPLATE = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.kitty${kitty_version_b}",
    "runtime": "org.freedesktop.Platform",
    "runtime-version": "18.08",
    "sdk": "org.freedesktop.Sdk",
    "command": "kitty",
    "finish-args": [ "--socket=x11", "--socket=wayland", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "kitty",
            "buildsystem": "simple",
            "build-commands": [
                "python3 setup.py linux-package",
                "cp -r linux-package/* /app"
            ],
            "sources": [
                {
                    "type": "archive",
                    "url": "https://github.com/kovidgoyal/kitty/releases/download/v${kitty_version}/kitty-${kitty_version}.tar.xz",
                    "sha512": "${kitty_sha}"
                }
            ]
        },
        {
            "name": "scripts",
            "buildsystem": "simple",
            "build-commands": [
                "install -D run-in-host /app/bin/run-in-host"
            ],
            "sources": [
                {
                    "type": "file",
                    "path": "../run-in-host"
                }
            ]
        }
    ]
}
""")


kitty_versions = (
    ('0.13.3', '9ce803469057245f9e1c50b53e03d48d3f2483b01f9441be6eadbfea8edcba01652177cbff11d1dd2b35e9415db6822fd72a0494f00ee3be30f58c1f1991c37b'),
)


for kitty_version, kitty_sha in kitty_versions:
    kitty_version_b = kitty_version.replace('.', '_')
    with open('de.uchuujin.fp.termzoo.kitty{}.json'.format(kitty_version_b), "w") as f:
        f.write(KITTY_TEMPLATE.substitute(kitty_version=kitty_version, kitty_version_b=kitty_version_b, kitty_sha=kitty_sha))


