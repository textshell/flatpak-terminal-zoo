#! /usr/bin/env python3

from string import Template

KITTY_TEMPLATE = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.kitty${kitty_version_b}",
    "runtime": "org.gnome.Platform",
    "runtime-version": "3.35",
    "sdk": "org.gnome.Sdk",
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
    ('0.14.0', '5a5e4125cb82a4f3efd6e987ae0b6f49f6a1f2985094ea4729c607e327e1faea72d450f16ad73fdb21ea9f884031691008f04e795d6100f0bfd0bb4967a07775'),
    ('0.14.1', 'a19501967cc04c816452ee7a1a7526ff5c04ff96c88456ff901b7ea3099497ff997a23871265fd645eb9e6dd0c23cc19cb7dda70d61b108ca4b4b4b141b5ac6e'),
    ('0.14.2', '191a37424c51776d271008c6b4b0cb43b60cd2abea3ea7b2a08cca9a8d44c4932ca11470f3efb8debc0e2ef3641bb68c05374401073b23cf81042af467b1dbf4'),
    ('0.14.3', 'bf0c725b111dfc8fb356b85698f660ad048dd677cf57dab43537fb4340b822a1f73c5b25b1bb980aa4284502f328069e73f79ac6bef7187395c4fc9daeff3a0f'),
    ('0.14.4', '1550883232bff21217fc0d294598d6d828e67a944fc69b324079e87bf2505344c58ade75cec8bff1dca7821c4f490c066f2645281cee0e71792d317ef7df3779'),
    ('0.14.5', '9c433ac3b606dcfbf85ddb17e8e13846e99daf5904aa85ae70599e9a09aa09a67caf5a95a2584ef25dcc0bb7ab16b50541cce72e5ddd12b60f1e02fd96b97477'),
    ('0.14.6', '889bfce732f2a36d338c9c41b28e0770d98c15530b56a9f037cef610593b50453f1bde60e89560472035fc250dec0431a9776de1449f77e4c6988aca157eea12'),
)


for kitty_version, kitty_sha in kitty_versions:
    kitty_version_b = kitty_version.replace('.', '_')
    with open('de.uchuujin.fp.termzoo.kitty{}.json'.format(kitty_version_b), "w") as f:
        f.write(KITTY_TEMPLATE.substitute(kitty_version=kitty_version, kitty_version_b=kitty_version_b, kitty_sha=kitty_sha))


