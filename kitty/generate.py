#! /usr/bin/env python3

from string import Template

KITTY_TEMPLATE = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.kitty${kitty_version_b}",
    "runtime": "org.gnome.Platform",
    "runtime-version": "3.36",
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
    ('0.15.0', '4e546fb9ad0cf34df8aa5ef3787224e8dd820fadb474faddc5f47b987bbc46fb62350a64bcacbdccd7e7cd287df22045ed742b89f613e402f033dc8bb73d8688'),
    ('0.15.1', 'e32fe719b4fc7c45b324e4372e0dca3e482f81b245b8bf4eb2b643dccc8541a8d1f93b0f73d5777a7b51cd62a720468036bcb848797e0cba2dad71bba005f9e1'),
    ('0.16.0', '24dedfc58c5d33aa18da85f904952129f39cd54afb70282c7572b57514b1deebfb532414913e0efc3a5c0352a81406cd7ddef99490dbd9186dc61eab7af3975b'),
    ('0.17.0', '48f3eb939362bc6a1eb5692917e2da2c123b83708a27de610cab520270eda2550ed8e2ffcbce10e162ce85d92cba11780935a4e0451ee91ae2cda227cd6eca25'),
    ('0.17.1', 'adaa1a4b597782f0763cbe56aab7d86889b2c162190af0ee10949b4b050d74e791f903a688434a65848805bdf73c34301cc7e67667042dad905261c6366936a0'),
    ('0.17.2', 'bccf1c1d60d1149bc5f849b82db1af80a2d9a7a11c5f2df853daae5700550eef98da389a30f015d67be796f39deacb31f3ee245eb37ba1a41ba377c70cd26d61'),
    ('0.17.3', 'dc14ba35e77e0ebd1978fde0731b00e726e75137f900952dfa6b06add1f46e3a3f42e8e886ce8c689e4e3500f2d2216a66225d5211522a41d09ef61265065e2d'),
    ('0.17.4', '4ea954a59f44b04a1540d814892b08c93e37c07d7dd32b5db3f50806fa6f39a8a89957c216e47b43bf7aa9571dd0200de7dc12266cc672c9e70e39b2133da0d7'),
    ('0.18.0', '4b8b6d6549ff12ecc7a9216b11e7c03077ba50fed62c1e9847611c7b7d1a1283143ede29252ff5dd4b58de6afd2d2f87b7985d878897bc69ae83fef4e369f8ce'),
    ('0.18.1', 'd1870fa8c1c42c9a20251ba7819fb649760a98070653cff6bbc0ef86160d6b20070bbfe4e549b80d75d7a78b37cb3c1153e4be246709cf630129cd4d09a76604'),
    ('0.18.2', '12b17f241884347e841b597cc86ac7dec9f509350af33de4e790f586b1cb8a5b89222f25f710f1f5ab82ea09cb1c7b0fa9ffee869cbae497e2a2ab0c6ef1b5a0'),
    ('0.18.3', '77636c4d1c21157e86cae3a88bca8b161207c1f1112ce60d11d04e79cf6e8ed331085f99e0caa20b7b4f297d8bf193aeb7afa8679c871085cc9d328ed8da3ad7'),
)


for kitty_version, kitty_sha in kitty_versions:
    kitty_version_b = kitty_version.replace('.', '_')
    with open('de.uchuujin.fp.termzoo.kitty{}.json'.format(kitty_version_b), "w") as f:
        f.write(KITTY_TEMPLATE.substitute(kitty_version=kitty_version, kitty_version_b=kitty_version_b, kitty_sha=kitty_sha))


