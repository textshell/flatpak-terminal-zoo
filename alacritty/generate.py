#! /usr/bin/env python3

from string import Template

ALACRITTY_TEMPLATE = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.alacritty0_2_9",
    "runtime": "org.freedesktop.Platform",
    "runtime-version": "18.08",
    "sdk": "org.freedesktop.Sdk",
    "command": "alacritty",
    "finish-args": [ "--socket=x11", "--socket=wayland", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "xmu",
            "buildsystem": "autotools",
            "sources": [
                {
                    "type": "archive",
                    "url": "https://www.x.org/releases/individual/lib/libXmu-1.1.2.tar.bz2",
                    "sha512": "eba4e3d10f7d75ba8464881fb69f295a89774a4b37793197d75f3312e3a342b2df8b7e13e3f5c887962704329b5347ff2f3395e229af9dadf46a93b1e8613cfc"
                }
            ]
        },
        {
            "name": "xclip",
            "buildsystem": "autotools",
            "sources": [
                {
                    "type": "archive",
                    "url": "https://github.com/astrand/xclip/archive/0.13.tar.gz",
                    "sha512": "191a86194a1503a47c6641a55855dc4aaa8c2c99d2e6f1d46e727feec85a6639041f37ec2265c05c178c0c7d791d3e88bde89223f879effa878812f078485ed2"
                }
            ]
        },
        {
            "name": "alacritty",
            "buildsystem": "simple",
            "build-commands": [
                "install -D alacritty /app/bin/alacritty"
            ],
            "sources": [
                {
                    "type": "archive",
                    "strip-components": 0,
                    "url": "https://github.com/jwilm/alacritty/releases/download/v${alacritty_version}/Alacritty-v${alacritty_version}-x86_64.tar.gz",
                    "sha512": "${alacritty_sha}"
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


alacritty_versions = (
    ('0.2.9', '5c646eb3577f10449c33d91b31eae59f3c773fad4eac6dc62c2fe6af4d7f3cdbc1572fba3e0799331ec1e51e31fd585c0dfce4b69872cde24140581c1da005b1'),
)


for alacritty_version, alacritty_sha in alacritty_versions:
    alacritty_version_b = alacritty_version.replace('.', '_')
    with open('de.uchuujin.fp.termzoo.alacritty{}.json'.format(alacritty_version_b), "w") as f:
        f.write(ALACRITTY_TEMPLATE.substitute(alacritty_version=alacritty_version, alacritty_version_b=alacritty_version_b, 
                    alacritty_sha=alacritty_sha))


