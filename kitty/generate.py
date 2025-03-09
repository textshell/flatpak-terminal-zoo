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

KITTY_TEMPLATE2 = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.kitty${kitty_version_b}",
    "runtime": "org.gnome.Platform",
    "runtime-version": "40",
    "sdk": "org.gnome.Sdk",
    "command": "kitty",
    "finish-args": [ "--socket=x11", "--socket=wayland", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "librsync",
            "buildsystem": "cmake",
            "sources": [{
                "type": "archive",
                "url": "https://github.com/librsync/librsync/releases/download/v2.3.4/librsync-2.3.4.tar.gz",
                "sha256": "a0dedf9fff66d8e29e7c25d23c1f42beda2089fb4eac1b36e6acd8a29edfbd1f"
            }]
        },
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


KITTY_TEMPLATE3 = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.kitty${kitty_version_b}",
    "runtime": "org.gnome.Platform",
    "runtime-version": "42",
    "sdk": "org.gnome.Sdk",
    "sdk-extensions": [
        "org.freedesktop.Sdk.Extension.golang"
    ],
    "command": "kitty",
    "finish-args": [ "--socket=x11", "--socket=wayland", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "librsync",
            "buildsystem": "cmake",
            "sources": [{
                "type": "archive",
                "url": "https://github.com/librsync/librsync/releases/download/v2.3.4/librsync-2.3.4.tar.gz",
                "sha256": "a0dedf9fff66d8e29e7c25d23c1f42beda2089fb4eac1b36e6acd8a29edfbd1f"
            }]
        },
        {
            "name": "kitty",
            "buildsystem": "simple",
            "build-options": {
                "append-path": "/usr/lib/sdk/golang/bin",
                "build-args": ["--share=network"]
            },
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


KITTY_TEMPLATE4 = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.kitty${kitty_version_b}",
    "runtime": "org.gnome.Platform",
    "runtime-version": "45",
    "sdk": "org.gnome.Sdk",
    "sdk-extensions": [
        "org.freedesktop.Sdk.Extension.golang"
    ],
    "command": "kitty",
    "finish-args": [ "--socket=x11", "--socket=wayland", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "librsync",
            "buildsystem": "cmake",
            "sources": [{
                "type": "archive",
                "url": "https://github.com/librsync/librsync/releases/download/v2.3.4/librsync-2.3.4.tar.gz",
                "sha256": "a0dedf9fff66d8e29e7c25d23c1f42beda2089fb4eac1b36e6acd8a29edfbd1f"
            }]
        },
        {
            "name": "kitty",
            "buildsystem": "simple",
            "build-options": {
                "append-path": "/usr/lib/sdk/golang/bin",
                "build-args": ["--share=network"],
                "cflags-override": true
            },
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

KITTY_TEMPLATE5 = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.kitty${kitty_version_b}",
    "runtime": "org.gnome.Platform",
    "runtime-version": "45",
    "sdk": "org.gnome.Sdk",
    "sdk-extensions": [
        "org.freedesktop.Sdk.Extension.golang"
    ],
    "command": "kitty",
    "finish-args": [ "--socket=x11", "--socket=wayland", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "librsync",
            "buildsystem": "cmake",
            "sources": [{
                "type": "archive",
                "url": "https://github.com/librsync/librsync/releases/download/v2.3.4/librsync-2.3.4.tar.gz",
                "sha256": "a0dedf9fff66d8e29e7c25d23c1f42beda2089fb4eac1b36e6acd8a29edfbd1f"
            }]
        },
        {
            "name": "simde",
            "buildsystem": "meson",
            "build-options": {
                "config-opts": ["-Dtests=false"]
            },
            "sources": [{
                "type": "archive",
                "url": "https://github.com/simd-everywhere/simde/archive/refs/tags/v0.8.2.tar.gz",
                "sha256": "ed2a3268658f2f2a9b5367628a85ccd4cf9516460ed8604eed369653d49b25fb"
            }]
        },
        {
            "name": "kitty",
            "buildsystem": "simple",
            "build-options": {
                "append-path": "/usr/lib/sdk/golang/bin",
                "build-args": ["--share=network"],
                "cflags-override": true
            },
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


KITTY_TEMPLATE6 = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.kitty${kitty_version_b}",
    "runtime": "org.gnome.Platform",
    "runtime-version": "45",
    "sdk": "org.gnome.Sdk",
    "sdk-extensions": [
        "org.freedesktop.Sdk.Extension.golang"
    ],
    "command": "kitty",
    "finish-args": [ "--socket=x11", "--socket=wayland", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "librsync",
            "buildsystem": "cmake",
            "sources": [{
                "type": "archive",
                "url": "https://github.com/librsync/librsync/releases/download/v2.3.4/librsync-2.3.4.tar.gz",
                "sha256": "a0dedf9fff66d8e29e7c25d23c1f42beda2089fb4eac1b36e6acd8a29edfbd1f"
            }]
        },
        {
            "name": "simde",
            "buildsystem": "meson",
            "build-options": {
                "config-opts": ["-Dtests=false"]
            },
            "sources": [{
                "type": "archive",
                "url": "https://github.com/simd-everywhere/simde/archive/refs/tags/v0.8.2.tar.gz",
                "sha256": "ed2a3268658f2f2a9b5367628a85ccd4cf9516460ed8604eed369653d49b25fb"
            }]
        },
        {
            "name": "kitty",
            "buildsystem": "simple",
            "build-options": {
                "append-path": "/usr/lib/sdk/golang/bin",
                "build-args": ["--share=network"],
                "cflags-override": true
            },
            "build-commands": [
                "python3 setup.py linux-package",
                "cp -r linux-package/* /app"
            ],
            "sources": [
                {
                    "type": "archive",
                    "url": "https://github.com/kovidgoyal/kitty/releases/download/v${kitty_version}/kitty-${kitty_version}.tar.xz",
                    "sha512": "${kitty_sha}"
                },
                {
                    "type": "archive",
                    "strip-components": 0,
                    "dest": "fonts",
                    "url": "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/NerdFontsSymbolsOnly.tar.xz",
                    "sha256": "8b5ecbe2612cb37d75e2645f7644876bc38960574909b1c01c002d0e8d33deb3"
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
    ('0.13.3', '', '9ce803469057245f9e1c50b53e03d48d3f2483b01f9441be6eadbfea8edcba01652177cbff11d1dd2b35e9415db6822fd72a0494f00ee3be30f58c1f1991c37b'),
    ('0.14.0', '', '5a5e4125cb82a4f3efd6e987ae0b6f49f6a1f2985094ea4729c607e327e1faea72d450f16ad73fdb21ea9f884031691008f04e795d6100f0bfd0bb4967a07775'),
    ('0.14.1', '', 'a19501967cc04c816452ee7a1a7526ff5c04ff96c88456ff901b7ea3099497ff997a23871265fd645eb9e6dd0c23cc19cb7dda70d61b108ca4b4b4b141b5ac6e'),
    ('0.14.2', '', '191a37424c51776d271008c6b4b0cb43b60cd2abea3ea7b2a08cca9a8d44c4932ca11470f3efb8debc0e2ef3641bb68c05374401073b23cf81042af467b1dbf4'),
    ('0.14.3', '', 'bf0c725b111dfc8fb356b85698f660ad048dd677cf57dab43537fb4340b822a1f73c5b25b1bb980aa4284502f328069e73f79ac6bef7187395c4fc9daeff3a0f'),
    ('0.14.4', '', '1550883232bff21217fc0d294598d6d828e67a944fc69b324079e87bf2505344c58ade75cec8bff1dca7821c4f490c066f2645281cee0e71792d317ef7df3779'),
    ('0.14.5', '', '9c433ac3b606dcfbf85ddb17e8e13846e99daf5904aa85ae70599e9a09aa09a67caf5a95a2584ef25dcc0bb7ab16b50541cce72e5ddd12b60f1e02fd96b97477'),
    ('0.14.6', '', '889bfce732f2a36d338c9c41b28e0770d98c15530b56a9f037cef610593b50453f1bde60e89560472035fc250dec0431a9776de1449f77e4c6988aca157eea12'),
    ('0.15.0', '', '4e546fb9ad0cf34df8aa5ef3787224e8dd820fadb474faddc5f47b987bbc46fb62350a64bcacbdccd7e7cd287df22045ed742b89f613e402f033dc8bb73d8688'),
    ('0.15.1', '', 'e32fe719b4fc7c45b324e4372e0dca3e482f81b245b8bf4eb2b643dccc8541a8d1f93b0f73d5777a7b51cd62a720468036bcb848797e0cba2dad71bba005f9e1'),
    ('0.16.0', '', '24dedfc58c5d33aa18da85f904952129f39cd54afb70282c7572b57514b1deebfb532414913e0efc3a5c0352a81406cd7ddef99490dbd9186dc61eab7af3975b'),
    ('0.17.0', '', '48f3eb939362bc6a1eb5692917e2da2c123b83708a27de610cab520270eda2550ed8e2ffcbce10e162ce85d92cba11780935a4e0451ee91ae2cda227cd6eca25'),
    ('0.17.1', '', 'adaa1a4b597782f0763cbe56aab7d86889b2c162190af0ee10949b4b050d74e791f903a688434a65848805bdf73c34301cc7e67667042dad905261c6366936a0'),
    ('0.17.2', '', 'bccf1c1d60d1149bc5f849b82db1af80a2d9a7a11c5f2df853daae5700550eef98da389a30f015d67be796f39deacb31f3ee245eb37ba1a41ba377c70cd26d61'),
    ('0.17.3', '', 'dc14ba35e77e0ebd1978fde0731b00e726e75137f900952dfa6b06add1f46e3a3f42e8e886ce8c689e4e3500f2d2216a66225d5211522a41d09ef61265065e2d'),
    ('0.17.4', '', '4ea954a59f44b04a1540d814892b08c93e37c07d7dd32b5db3f50806fa6f39a8a89957c216e47b43bf7aa9571dd0200de7dc12266cc672c9e70e39b2133da0d7'),
    ('0.18.0', '', '4b8b6d6549ff12ecc7a9216b11e7c03077ba50fed62c1e9847611c7b7d1a1283143ede29252ff5dd4b58de6afd2d2f87b7985d878897bc69ae83fef4e369f8ce'),
    ('0.18.1', '', 'd1870fa8c1c42c9a20251ba7819fb649760a98070653cff6bbc0ef86160d6b20070bbfe4e549b80d75d7a78b37cb3c1153e4be246709cf630129cd4d09a76604'),
    ('0.18.2', '', '12b17f241884347e841b597cc86ac7dec9f509350af33de4e790f586b1cb8a5b89222f25f710f1f5ab82ea09cb1c7b0fa9ffee869cbae497e2a2ab0c6ef1b5a0'),
    ('0.18.3', '', '77636c4d1c21157e86cae3a88bca8b161207c1f1112ce60d11d04e79cf6e8ed331085f99e0caa20b7b4f297d8bf193aeb7afa8679c871085cc9d328ed8da3ad7'),
    ('0.19.0', '', '7e9b0304fc42c839a4a7bec568364d47a8a2c4d6ad1ab5ee7ca3d89cd9c162505cdfb01b75b1fea40c894c27ca008ebfd3d909a0421f9acd960e7596ae760b04'),
    ('0.19.1', '', '3a61d15598f32634646cbf0be596e9023420452130be1b9a718d2ce7daf3edeee6d2ba3abfe91c768758b043ed46423a2382680f9dd65fd6a6c57dbcd0fc1fd3'),
    ('0.19.2', '', '86b6a08c7f5282587967ff7e3509d6ac4ef556b3bbeae1a9529a584f804f204d54f5031a90dcd08af735eb16a283938fa9e49c8d767dca12e945b7493f0e76da'),
    ('0.19.3', '', 'd1eea7f909c9492542650a83a149fd279c44380cf10387759f10caad57cd4dbabeac1ce84e8142bfa47266ec2562dfa3766ce08e2aee4d8e0ebacea165f101e4'),
    ('0.20.0', '', '0a240780dba941f1e4ed41b5ba87ab9524ba0b58ac73717d4d1e57226382aa1c535a5fff0d1c7da99ad7fcda200d69da424892353667cf8496cf4239af02b37a'),
    ('0.20.1', '', '19dfa66eb2a2115877b25fbff0ba7a81071bff00c732236f20342aeb619cca88ae4a4e8ce4e73908ac7d7d12fca5232a76e0167754f2e658af02e442cf5ba0cd'),
    ('0.20.2', '', '6f82f7c2346886513a8129131083a755a9c622a4bf29ab82d027b7cc7812f437fe6cb98d962a3e98ba0871e69c68d5f65a1d27d4301448275bebf01895071dfb'),
    ('0.20.3', '', '9e9d81696bcb0d3894c04b08bc52ccf7aaf533125b3ecfb4c894b8d42dbf8511239c49f1c977d81872ce49fc6b3aa8e8c92b9c944bd31fe59fce6e3750295e58'),
    ('0.21.0', '', '6b942ffb9381548750525de8d8641fa315eb2ab4b954af5fe6222aabb8b4f778a540c8ff8d57857739a22f99aa09e5522d8827e4077111a4a42dbf687b5bc39e'),
    ('0.21.1', '', '86b1e03f8227375cc46dabffd972a131c8a33d55d87888b2cf67d97da6749144408778b8ac126dbc29fe3850f272e5ae0c4313194ebb130ae3417b04b76cb987'),
    ('0.21.2', '', '0ae41dfd61fc70746e8ec2d37c043dea7ceb70205aca056fd156348d4b9a2f6aac520c60de08fb5a3cd9bb908efdd2ad8129bbc01b69e5908f2976e5393269df'),
    ('0.22.0', '', '081d065cc91f65c8e79559cad63208c5a4b2f64aa4b975722bd94d4e1530622e441c8ee73a549f83c64e381a3c9368d7848fa6487c488bc48821b154392fe7d0'),
    ('0.22.1', '', '8c561103cad181cb1d2a716d70cffd82bc0ad9db5a92434d17e3f4a70d6803cbe99edd8e87eca3912db4a8cd2c3e46d38bed833ea85ad4d190c50f0aa0461812'),
    ('0.22.2', '', '6736ec643444b262d2b6fa0d1c1c69df91f97fe157c066187a5da0ab91db2ab254c2ab5003d68044252787ff88c6696b96c5109ee5fb62c5b4d8799155aed650'),
    ('0.23.0', '', 'c9f3c51b312c4bd329241c6e58709bf558e6319f56f5e8489730d77612eafcbe880c67752b589b22bfa257e651c86a37c09bec3c1f82d8206bae1ee024f1ed6f'),
    ('0.23.1', '', '2d0c822e6bfca41b0a5e5e71e62f5073792b10c236287a509a6c790e19d098205c8719dbcb4aa630abbbaa3d44d6c9986c13efde7a9556772a89709383a0fe94'),
    ('0.24.0', '2', 'b851ed56d16f9a39d47810bf27c2bc8cbb52d476376c4090045db90c1ad0bc7db6fd9e97edd6ce50a6d69e716671e1e909aab889ecac368857ad5c07f68a76af'),
    ('0.24.1', '2', 'e590a3abd4ed38ce956ee1e1b9d3679150c83b80df5ed9daf9773d7a278f63dc8a3a563058906d322f9186bece7d479036a502864fd80f45593c4970c056f389'),
    ('0.24.2', '2', '6d49b20dbd96ed0a1ed49a4523b65593c547ea2fec46f4c2557e26cdb5048ebaadb2c2118c7a2dd346f83ecab2d0a341d2322ae37ebe49184e22055581c631e7'),
    ('0.24.3', '2', '2b1482164fb1aabfa2f775f24d0ffbbbd1e8a85cf114a2daa411379ea8dbcea6ae5f361997132fb4d773fed8adeec4c04ffb4e615a470cefeb794d8a39c94c0a'),
    ('0.24.4', '2', '28b1e2415b5c73ad8922d4ed17a63638c497a91c9aedba71c2f53e77fc89ed49951a2e873bba5bbe85c8eda22107d9ff4e4321010ac33a2d289c2fbd5d3a5b8f'),
    ('0.25.0', '2', 'fed8d66a9f7f2117f4b495305db0d56d8b85ef03bf7ef24a7dca31e63e16fc90e026aa8022237ad45678efb026f11fdd8aa377eb53917fd8ec885f2ccea721f8'),
    ('0.25.1', '2', '6d9862f8411372e0cf692114d6e29eb92db3a2e324282a21ca35b2ca5229c9d87ab988e802e44d47e98b6e64ae7abc5ff0cc677c082eb287e14ee68cd1a4c31e'),
    ('0.25.2', '2', 'ac858b525abbdeb137989a7971c51651d46bffedde048ed572bbb4c31119a4e0f9f424edbdbfd14fe2e043b4a7c8a1a1f8ee6591906e40a655d9f783b21f31a6'),
    ('0.26.0', '2', 'e8e041cb8cbe8560e35126d9f717111e0094ef9dd260ade07017f36d8e8e18fd4198cf186198b78089b8a05baa98a512d273b24b7f3f0d4f9f6d06107eb76c58'),
    ('0.26.1', '2', 'ed270c84078acb33921506296c476ada5f19fb33344047c7dad5b2d7b697c2111e2925dc391eb4927a05ef82ae583b35db5eee53e148e3e4d71ce942a1deade2'),
    ('0.26.2', '2', '4bfb3d9438bb018dc10503be610df4e6e8bb1f9459b5131f46fde6279ba5423e44dbbcb86a2dc2602ee208266edc78074f6496e99761cf43f7081ea9e88175f7'),
    ('0.26.3', '2', '77a518cd3ec4bb059907f16d01068914951cadbbcf803dcbfae13cc9ce144f65a886d7e986c7191019a0be9ccf902f086c72a24287458d083cbd3fd136d2c589'),
    ('0.26.4', '2', '4d3ef5ba2ca54d0f5cd84ece771297c19c05bd276fc235f92c76d469ad17e55b54de696dce38c9039ae9825c7609e03e937536261c4fb680e936865ee0e4441e'),
    ('0.26.5', '2', '086ae03d0e382afbe3001e357ef51388c7a8e81fa5b4bf9ce8b123a7fc8bfff3bd68d074e926f540a1f2b83062baa831e44d29c017cabfe8221bebe49b64e808'),
# 0.27.0 is unbuildable because something in the go dependencies does not match up.
#    ('0.27.0', '3', '8063008df261747a7089c69ad9ae3a3d3c24286014f02d04faee9f0b5b6f452172cf99ff8a520ca8e314ba0009e0009701292656db913c23d84b6a2311085813'),
    ('0.27.1', '3', '484d451b418defc7256319730d623224e3744d6200989d92839c40c951fdb213fe2ef472ddf968f695e499aa6c35d994ad76bb0eb28bca80ec8644b2ead40d56'),
    ('0.28.0', '3', 'd133dab019c67367e90cc2e2dce7e614a65400b079cdcfa854f2e1cb7399af7b1ba0f3ef4d30867ae588c9919a772c03ee12457b6dc5922f58c034a6da927127'),
    ('0.28.1', '3', 'a8863c8bf5a3c385671d98bd50481ffcd3984e45ee051173eb38de9aac79643e69a312e08b8f655759f3ecdfab4efe38dca39167f5590e482748b5e85dea5537'),
    ('0.29.0', '3', 'd8d13dea92d21ad113e3f6b056b2ea31514e0893b04c2bac2665821bb66ec10fdadacbf19e22980e0e744ef9d272f2fc2b4981016b182509af2040b6f4267d3c'),
    ('0.29.1', '3', 'ce09342ed3cbb0a518dde8d33606468ee5a2a164f18ff4c8addbd33b05459407d4a935b93acb0e98df8d618aa832c93f91e9ac060e7f87c1e4567484adc46c9c'),
    ('0.29.2', '3', 'a34d8b5bc817dd9d27f1afa190856d916576f52458ede2253655b294358b6b89b1f103acb90d8d66a494b346420ddedc9fcf1a3399f561268ded82e7b1954b06'),
    ('0.30.0', '4', '05438de8752057d7c419da41621b4d8fcfa6e7189530efc32c7c8a0bf2e6dae0332dd1b661206f9dea5bf374713e86ea5e69f640b0e73fe617f528bc963a8792'),
    ('0.30.1', '4', 'e5fd68b8acf3eae8f53a2c27101d998eb0d8eff1571de1b03ab431bceafcab0efae821590684ec48b5ed6e3d86fb984d9e04784022ba50c0378d37a68598f9ed'),
    ('0.31.0', '4', '3868431003f9f1a3907415124c1d8282b077985a9d104615d48f9d309f6fbf1a11119546674508649aa35f2b6e66aa5638024e8127f92ae7b043da367c7b3363'),
    ('0.32.0', '4', 'd64f36c20d484724b0215a2ffc9044b83ddaa476926377e6c79226d7d6bd5deffda9964291a99c0df174640fb2fa7df0464435d2cef19304eab7b1d135cc1847'),
    ('0.32.1', '4', '4be50093b2da7a6536548f8bf36ea86ab47238a1f346e10d4384a90d2d0d0e02f8d98dc6a463ffa7c7a93268202b5a4109f28e2b7ece1d9593f590691e5e1af8'),
    ('0.32.2', '4', '245d399366c0b2174bb80d557c08edf49e96a034a3cf33d2027180ef418581cc9bea2566d9ead9f96094bdc01655aeddd251b07b1bc444e7af59c864eb2bcd01'),
    ('0.33.0', '5', '5dad29e7ff0f83dd14138fd32ee3d556214251a5617ef9bd0c8a8b4032e26cf8973752d0b4221e06afd745ae4a12967fc1194f3d053b0e8451cb7ca97360fa35'),
    ('0.33.1', '5', '5fa2421baf9fac41d4a8ff89bb5e44d1820012e8c960e25980d597dcebbb44ffa97c03818e8a91015691321eedb9d9f53139a97cbb6bd673053fbfd73c77739b'),
    ('0.34.0', '5', '310084af59fb5832c9b87961d278601a8408fdcf4500083ffa5d4980ae600a2122a7477be23bfe0c374dec7955707894cb74cfd550ae577d66e39ed2e8b9c0f8'),
    ('0.34.1', '5', '1b361823741c8c2a6ce3c5d56d0cbbd51bd0a0d2574312ef5c05f359c70862e0889a9636e4b95865750cbd239b517763315ed0cf4ec46e1feaffc27cf20e0e66'),
    ('0.35.0', '5', 'b8c310237b1f0e48c1490f1bcfa009490d1592557bd81d6593a2a3ce71696ab03b3d91bb1dc32212adea70a4e6b5491ea6604d43517e679151df49e11b8de604'),
    ('0.35.1', '5', 'aecda31410b8d52ec7df5a9947f29be04249fadb6af24ee7e0cbb649f09a9e510d9fe6913d24d10c36ef7227187c96a1e3f25a8da840a16ed0bcb8cb46f1f089'),
    ('0.35.2', '5', 'edc78046f942965c823a1202a6d7c85cc2d2acb376824a0f5224d4ba6f48ed0978a00eb7a3e1e6053622a7d5fdcf80009ecfb61a63272cf407dd30f828f47b56'),
    ('0.36.0', '6', '910864d9f7d1015f42a641200a3bd3f8b682c108c6732a189098072e83bc263d53589e2dfb6e3383abc635f19d4476f3ab22bd24914c316416a8c9fd89d48b2f'),
    ('0.36.1', '6', '503ecfc83e367b3f2aacc1bf7849345ef4a50cae69e496325b573660d1fe592cc778d0f9d0d06d5e46210659f4b65b3a7be7dfe1e219565b7371c1848643e111'),
    ('0.36.2', '6', '14efd609f87aa50adc26585e80d3fa80328cbda7b0352eb1689ea585c24cc03fec06424e28d1278b4db6aa8f98ef1faf132ea602637d7781947b72bed53d4784'),
    ('0.36.3', '6', '290ce8d1d64ed431221ecdc9f942218ee375d7c065193186ad3d2a58bb936ff206b6df3379cd0d4d233cbf3433f9fbeb16d0459704e343cb32305de841828513'),
    ('0.36.4', '6', '3ffabb181903495d6a11a8b790e75331a5ab0986de0b7a7958ea7dfee724c29aee88c31672e2f7711d3fc51a81e1a3c84e4469228872aa62df840ded2c0d5218'),
    ('0.37.0', '6', '786b3361147c988e7bbafcc0706940b8dbd172b07b88c1d6b49ae4a3caefba2cb72a05bf4f173ac963989be6d435bef60d6f8e8abb76362f8a07c231cfa04e31'),
    ('0.38.0', '6', 'a7c462b92e5ec4db95ec233963010d20a091cdc0660a6ee250863f9fb8ce07dbc6287075c41ee19e3455933991f77273da90814a5178775f00a5364553809c81'),
    ('0.38.1', '6', '273a9fc959973ad73105f5d589e420df9360bb20818165b05e14981c42f7146cec6cbb17539a91089a5af9b94dbb3f416421671bbe20cdb0b876cde5043b784c'),
    ('0.39.0', '6', '765f1c4bd6aa8fe751c4e0d4a44b924858ed1eb97b37beaa60e5a90b16df353e9b7db32990aa93bc960e8f01ae3de88381fe4cbc1a4dc69c0bdf655077fdf3ab'),
    ('0.39.1', '6', '50d8e083e63fb5ccee5d6a4d7a3d07e775fe609307ad724527cd50ab33a7023d4e6694dd08ce322e643806fdcf92c0e990f14212ad168dbf4f39b8a666634000'),
)


for kitty_version, template_ver, kitty_sha in kitty_versions:
    kitty_version_b = kitty_version.replace('.', '_')
    with open('de.uchuujin.fp.termzoo.kitty{}.json'.format(kitty_version_b), "w") as f:
        if template_ver == '2':
            f.write(KITTY_TEMPLATE2.substitute(kitty_version=kitty_version, kitty_version_b=kitty_version_b, kitty_sha=kitty_sha))
        elif template_ver == '3':
            f.write(KITTY_TEMPLATE3.substitute(kitty_version=kitty_version, kitty_version_b=kitty_version_b, kitty_sha=kitty_sha))
        elif template_ver == '4':
            f.write(KITTY_TEMPLATE4.substitute(kitty_version=kitty_version, kitty_version_b=kitty_version_b, kitty_sha=kitty_sha))
        elif template_ver == '5':
            f.write(KITTY_TEMPLATE5.substitute(kitty_version=kitty_version, kitty_version_b=kitty_version_b, kitty_sha=kitty_sha))
        elif template_ver == '6':
            f.write(KITTY_TEMPLATE6.substitute(kitty_version=kitty_version, kitty_version_b=kitty_version_b, kitty_sha=kitty_sha))
        else:
            f.write(KITTY_TEMPLATE.substitute(kitty_version=kitty_version, kitty_version_b=kitty_version_b, kitty_sha=kitty_sha))


