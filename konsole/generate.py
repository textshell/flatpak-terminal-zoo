#! /usr/bin/env python3

from string import Template

KONSOLE_TEMPLATE = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.konsole${konsole_version_b}",
    "runtime": "org.kde.Platform",
    "runtime-version": "5.12",
    "sdk": "org.kde.Sdk",
    "command": "konsole",
    "finish-args": ["--socket=x11", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "konsole",
            "buildsystem": "cmake",
            "sources": [
                {
                    "type": "archive",
                    "url": "https://download.kde.org/${konsole_dldir}/applications/${konsole_version}/src/konsole-${konsole_version}.tar.xz",
                    "sha512": "${konsole_sha}"
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


KONSOLE_OLD_TEMPLATE = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.konsole${konsole_version_b}",
    "runtime": "org.kde.Platform",
    "runtime-version": "5.12",
    "sdk": "org.kde.Sdk",
    "command": "wrapper",
    "finish-args": ["--socket=x11", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "kdelibs4support",
            "buildsystem": "cmake",
            "sources": [
                {
                    "type": "archive",
                    "url": "https://download.kde.org/stable/frameworks/5.65/portingAids/kdelibs4support-5.65.0.tar.xz",
                    "sha512": "5d41561a28999d460099fc97e69ba76340f9f46e67725dd9a66a5f8fdf5e6395f17908f997ecf84656d3fb7712490772df561a4122da946041f2c85d2053f341"
                }
            ]
        },
        {
            "name": "konsole",
            "buildsystem": "cmake",
            "config-opts": ["-DBUILD_TESTING=0"],
            "sources": [
                {
                    "type": "archive",
                    "url": "https://download.kde.org/${konsole_dldir}/applications/${konsole_version}/src/konsole-${konsole_version}.tar.xz",
                    "sha512": "${konsole_sha}"
                }
            ]
        },
        {
            "name": "wrapper",
            "buildsystem": "simple",
            "build-commands": [
                "install -D wrapper-isolated-dbus /app/bin/wrapper"
            ],
            "sources": [
                {
                    "type": "file",
                    "path": "wrapper-isolated-dbus"
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


konsole_versions = (
    ('14.12.3', True, 'Attic', '382710cee174c33c2db405b6c0ff399df657a5c9c7ad448899ba5176ed354a500f95e555058a5cd484b464dcb3260b28ce6665c1daaf6532dd66d9f4d273edff'),
    ('15.04.3', True, 'Attic', '71a4381e89821be3aa287d9de13533f54ef94ca7d5ef11bec190d338d9e35226fc042a7dde998fc317cf707c3d905b59bc27d373b7cc43caf018dc755ff4fb5a'),
    ('15.08.3', True, 'Attic', '7e32d239769684884737f7c2f3a9597a1107eccbae0208d7b4f1521a1b9b88fb88759099ec34b37f008f3ca6d4dbb727332915b07910a34f98f518e803694ba8'),
    ('15.12.3', True, 'Attic', 'c6adbf6b7e5817a8d374f34f9310d0946baa245736c93d80493f6b50d77157f037619368f22fe27a6facdb2d0256f50126fac220592d4b1e6a6f74f1130019fa'),
    ('16.04.3', True, 'Attic', '2658791533e8ea83a4fdd2cacbcddbde7a6dc17e6302b54b5341c1f5c3e83557980ff90fc3417ef4e5d6d54a9979d58581cef6fa1037db8abb95662052fd706c'),
#    ('16.08.3', False, 'Attic', 'cc0b2b12efebc002fc731bb00943835d383c881206bf56708dacc84a830b285af44b38cff9683521bc3fca13196c40e210f866eb6bae1ebd6a44386ddb0d2de6'),
#     ^^^^^^^ does not compile
    ('16.12.3', False, 'Attic', 'c6ce7e10434949cb90183361780322a44f720e304ed14203522d1ae3ad843460186b0abb11432ce99b1299a03ec590f4af4f90aa13238b7e457ed7517c8f2934'),
    ('17.04.3', False, 'Attic', '698ea2bd7ccfb280b5909f88a65e46b9feda6e251e25e86b198e68c178fcd46498466f1e63457ac32342dde4abac512433c9ceb7489cc413843015a1828aab48'),
    ('17.08.3', False, 'Attic', '1d2723ba3dd988b3b1deaadf5ccf10455bf48d9c5961e9d614342bd5c0dbb7b42b461b529f4eb6a5ba855951f5b2d7d1d4f93170091ea3b47f02ac70c2583f4b'),
    ('17.12.3', False, 'stable', '973c47341ebe729442ba8f8a7523eccaf5da28afbfe236fd4ec2897f710c3967f22ed5cd8f2f997f631a5369625c830f7a4540cdf6953874c2f556f547c413a0'),
    ('18.04.3', False, 'stable', '0809cf4db6e10e672a4a976609045fb88879fe615b48e452f140da0a6c44971f31a7b4606124ed3b7642ee3f3556ace45b31e0b5c466df611fea98a9cf702066'),
    ('18.08.3', False, 'stable', '3dcc5111e7a7fa389dda862b4a895379ffdb7a39d6568b3b958bf36631e3b3424a6abf2b9166f8567fcdf2d2d6f305a2e13f7575ce63549b0ebb4ebc27b33a82'),
    ('18.12.3', False, 'stable', '9fecd316a9bc7adaca9a3fac38a57d293286b6328e88d96ac1cf8967fcb67ef8e9a5b085e185c4373599eafd0eaa18f0d73df70df16b98a1badd9efb689e1f7c'),
    ('19.04.3', False, 'stable', '20ec8ae12268110f00999b9f1197aff667ee2af7d7c2747b4d142c9db48fceaca7c01ab8f12fbc541cfc79eaebcbd704e166610f263c46083ad9fefb3c5da848'),
    ('19.08.2', False, 'stable', 'b781e1e6a19b81a49722fa04d568a53dda2c22f72ee197ebf7bacb9142d260ce3071a12cfada905d029dc2ab43a047205175cde5906a4033fb8bdd20876c1af5'),
    ('19.08.3', False, 'stable', '140a34b8f73786557b71ac5b23b500950c598ef88795e660c7fde3077c9f5d842ae1eed73966eb14dfb54d2833fa63c310fa2cb340a81c30f31fdd77e9f263dc'),
)


for konsole_version, konsole_old, konsole_dldir, konsole_sha in konsole_versions:
    konsole_version_b = konsole_version.replace('.', '_')
    with open('de.uchuujin.fp.termzoo.konsole{}.json'.format(konsole_version_b), "w") as f:
        template = KONSOLE_TEMPLATE if not konsole_old else KONSOLE_OLD_TEMPLATE
        f.write(template.substitute(konsole_version=konsole_version, 
                konsole_dldir=konsole_dldir,
                konsole_version_b=konsole_version_b, konsole_sha=konsole_sha))


