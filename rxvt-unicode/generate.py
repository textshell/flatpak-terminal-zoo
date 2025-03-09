#! /usr/bin/env python3

from string import Template

URXVT_TEMPLATE = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.urxvt${urxvt_version}",
    "runtime": "org.freedesktop.Platform",
    "runtime-version": "18.08",
    "sdk": "org.freedesktop.Sdk",
    "command": "urxvt",
    "finish-args": ["--socket=x11", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
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
            "name": "rxvt-unicode",
            "buildsystem": "simple",
            "build-commands": [
                "./configure LDFLAGS='-Wl,--copy-dt-needed-entries -L/app/lib' CPPFLAGS='-fpermissive -I/app/include' --with-res-name=urxvtTZ --with-res-class=URxvtTZ --prefix=/app --enable-256-color --enable-combining --enable-fading --enable-font-styles --enable-iso14755 --enable-keepscrolling --enable-lastlog --enable-mousewheel --enable-next-scroll --enable-pixbuf --enable-pointer-blank --enable-rxvt-scroll --enable-selectionscrolling --enable-slipwheeling --enable-smart-resize --enable-transparency --enable-unicode3 --enable-warnings --enable-xft --enable-xim --enable-xterm-scroll --with-term=rxvt-unicode-256color --disable-perl",
                "make",
                "make install"
            ],
            "sources": [
                {
                    "type": "archive",
                    "url": "http://dist.schmorp.de/rxvt-unicode/Attic/${urxvt_file}",
                    "sha512": "${urxvt_sha}"
                }${urxvt_patch}
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


CPP11_TYPE_PATCH = """,
                {
                    "type": "patch",
                    "path": "cpp11-typo-fix.patch"
                }
"""


URXVT_TEMPLATE2 = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.urxvt${urxvt_version}",
    "runtime": "org.freedesktop.Platform",
    "runtime-version": "18.08",
    "sdk": "org.freedesktop.Sdk",
    "command": "urxvt",
    "finish-args": ["--socket=x11", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
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
            "name": "libptytty",
            "buildsystem": "cmake",
            "sources": [
                {
                    "type": "archive",
                    "url": "http://dist.schmorp.de/libptytty/libptytty-2.0.tar.gz",
                    "sha512": "9cca5fddbcc4025c2bbe043e3367ac902d0024a34301258dafcf0de70935c055279d88227168d112d0e4c0dc37f1f49e1ea587bd6bddf0b9d92400657bc7be08"
                }
            ]
        },
        {
            "name": "rxvt-unicode",
            "buildsystem": "simple",
            "build-commands": [
                "./configure LDFLAGS='-Wl,--copy-dt-needed-entries -L/app/lib' CPPFLAGS='-fpermissive -I/app/include' --with-res-name=urxvtTZ --with-res-class=URxvtTZ --prefix=/app --enable-256-color --enable-combining --enable-fading --enable-font-styles --enable-iso14755 --enable-keepscrolling --enable-lastlog --enable-mousewheel --enable-next-scroll --enable-pixbuf --enable-pointer-blank --enable-rxvt-scroll --enable-selectionscrolling --enable-slipwheeling --enable-smart-resize --enable-transparency --enable-unicode3 --enable-warnings --enable-xft --enable-xim --enable-xterm-scroll --with-term=rxvt-unicode-256color --disable-perl",
                "make",
                "make install"
            ],
            "sources": [
                {
                    "type": "archive",
                    "url": "http://dist.schmorp.de/rxvt-unicode/Attic/${urxvt_file}",
                    "sha512": "${urxvt_sha}"
                }${urxvt_patch}
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


urxvt_versions = (
    ('9_0',  'rxvt-unicode-9.0.tar.bz2',  '', 'bf556b1572056a2e531ba0d5789f7ecc1de8ea7657b13ec5b699e894bf7dd8e27b5341635a1bbc8ee287b170b8af943c1cce257bfd4412e6ed44449d29a853ab'),
    ('9_01', 'rxvt-unicode-9.01.tar.bz2', '', 'f93da5d4ef15319c3b3f19acbc5d9e078978496ca56659d983eedfaa88bb93d4030ca9553096c270fcedae04b00fe6c1641af7b4c9859deca8eaf9764092de25'),
    ('9_02', 'rxvt-unicode-9.02.tar.bz2', '', '4dc3806fa4fb8ef928321ba44fb1a318b37ce3507fa63527e9de74a7494c4d4f9381070a88511efb114c58412881af7c41163f0c242a829691a4cedfebeab6ab'),
#   9.03 does not exist
#   9.04 does not exist
    ('9_05', 'rxvt-unicode-9.05.tar.bz2', '', '37169a0f28fec20c268fc92c5c588cc8457b048e1fa5e663475f3d4ef9be631f61967fe1a269f233af69e147cbf9b613105804638fec902c604811fcff07ab5e'),
    ('9_06', 'rxvt-unicode-9.06.tar.bz2', '', 'fa3754c92f2c06a467b1c1ff78f2ba5ea723239efb54dec0a004490d82e8d55e8734e3abedcd800f769d3c13f99046de87a5abd916d24818915092de902a943c'),
    ('9_07', 'rxvt-unicode-9.07.tar.bz2', '', '1acdaa6863aeb7f9a861860a898a036900897cd351ed66db006b3612f8750ece042c913b08a125100bd4daad6525cf56246741fc37a49df5bf38b4382f8bd152'),
#   9.08 does not exist
    ('9_09', 'rxvt-unicode-9.09.tar.bz2', '', '80827a77ff8710f85f32adf9749af8e30315406929f95a1892d645371f2520ad5b60c44dd5a10bd18baeed0850b5dcf532007124b8aae60d916f83a0581edc02'),
    ('9_10', 'rxvt-unicode-9.10.tar.bz2', '', 'e19cb074d5c279858d3bb68930a56d8f4d9c2eb77fa163a4c5609c491965135dee473230823a9823f59a74cbcc2ad2efc9836c26c96bea76778ae6cad281ec50'),
    ('9_11', 'rxvt-unicode-9.11.tar.bz2', '', '10738bb7f10c4bea077b8844268155a54febf88bbbd9a87fc29153faeaf4d991020f716fa1e2b6fcc5759a440c523a8f9afb36dc726196e10dded8421ffe65cd'),
    ('9_12', 'rxvt-unicode-9.12.tar.bz2', '', 'd2307b87f2cf2b63f42f575a72becf637e0455e1ff9aed5ecfba1d8f9991ea8f21654ee34afe16610deda83f39f02d339e59cba1a578cf92c5551735d0a683b0'),
#   9.13 does not exist
    ('9_14', 'rxvt-unicode-9.14.tar.bz2', '', '913a1ad8a518da798882caaf6edcd34681a8e36fe8a1b9c768a9ee05cd8ddefaf44b3c58a92f89e812f473458666f5221c7952067a67daaf9cf7812fdf42c74e'),
    ('9_15', 'rxvt-unicode-9.15.tar.bz2', '', '1095fb88502377fa669746bbe9a5597f0c748e2c01a468ce382e91236ed0e6f720f3ca7631f7105aa390afac09588b92cebd70589096b6a20f174c4297463b71'),
    ('9_16', 'rxvt-unicode-9.16.tar.bz2', CPP11_TYPE_PATCH, 'c22feec33176120944c58abb21c1e0508b5682bec4bde645e9c68735f9cf93e14e1a3b804374c6fd58f9032faa4cbf4fb2122a2307d0f2204e4b9b5a11427092'),
    ('9_17', 'rxvt-unicode-9.17.tar.bz2', CPP11_TYPE_PATCH, 'e7ba2614cf7f8027170a6adfddedd3fc7a63f219a76f92901b49b5a26295d5191200ac7c1dad1f1e7c90225c8fa2dced3022317e8e876425a57d067c3c0d84ee'),
    ('9_18', 'rxvt-unicode-9.18.tar.bz2', CPP11_TYPE_PATCH, '8d1abf38c6ad47129fafc22c3996a7e2cd0f0cf4982d441ee30076d64d191637942307efd12cc05dfef6b65136530973be9da89e6769c5967d4e523f33309237'),
    ('9_19', 'rxvt-unicode-9.19.tar.bz2', CPP11_TYPE_PATCH, '357f2b9a299b816264e8cece3200338369399e4f760622daec1520d05c75e93d44e2dee3351c8e31765ab8f2218dbb9d239960ae8112e2f75d988785373d7f26'),
    ('9_20', 'rxvt-unicode-9.20.tar.bz2', CPP11_TYPE_PATCH, '39e1574f7b7034c07ab2e836bb77e0fb0536830df873cc54e6c7583be5e20d36dea3fe0fc889283f163530c77534a3a55de227ee0a8f03564d0f030e60461ff9'),
    ('9_21', 'rxvt-unicode-9.21.tar.bz2', '', 'd50adf6b1e6ae3b13492b4f40455d3a56bb174a7c6db4d4525a1277736994adfb74a2cd1e7d3e8a8cfdc4509a9ae32c05a627829e295dc1bd4a5ba7cc2f80776'),
    ('9_22', 'rxvt-unicode-9.22.tar.bz2', '', 'b39f1b2cbe6dd3fbd2a0ad6a9d391a2b6f49d7c5e67bc65fe44a9c86937f8db379572c67564c6e21ff6e09b447cdfd4e540544e486179e94da0e0db679c04dd9'),
# does not build, missing ev_iouring.c
#    ('9_25', 'rxvt-unicode-9.25.tar.bz2', '', '5df3293c9b091af0577ef967285b8b3c072b0c64338b686be8e762824b163e45f7c5653f5482a4af942ca36aefba2d690831c414a046602862c6b86ee59509fe'),
    ('9_26', 'rxvt-unicode-9.26.tar.bz2', '', '35560b57730e17c9542ea4a615fd86ce703c4e6421323e8fe1570007737a880fde90d17943e5af9e170be4111b9769f4aa7e57efca5428421fdc1c299112f8e0'),
    ('9_29', 'rxvt-unicode-9.29.tar.bz2', '2', '8af7f1e8c3f2c6bf5fa131b6ef61e836ac7c83ac2b31ccb183d7481191f55a8e87e7f9f6d93f2ae1855ca339f71b2d682471ee41ef706b7ccc21c6c8ea4b44f9'),
    ('9_30', 'rxvt-unicode-9.30.tar.bz2', '2', '048d5f635a61bc1a739d5cbc09e7a9f77cee18c81df468ce1ff0a62866ced06fc4ec258bb015d2484a7e7bad2339f0bdd79bd824d649c2553a80bdef9f199e99'),
    ('9_31', 'rxvt-unicode-9.31.tar.bz2', '2', '4d14ecbbb62de1b1c717277f5aae5cfb536e11392f2d4b82c884c1713f437fce8e9dd69a328fa353a55d068d8ee4121a31900f45191acec172d5dc76652b6255'),
)


for urxvt_version, urxvt_file, urxvt_patch, urxvt_sha in urxvt_versions:
    with open('de.uchuujin.fp.termzoo.urxvt{}.json'.format(urxvt_version), "w") as f:
        if urxvt_patch == "2":
            f.write(URXVT_TEMPLATE2.substitute(urxvt_version=urxvt_version, 
                    urxvt_file=urxvt_file, urxvt_patch="",
                    urxvt_sha=urxvt_sha))
        else:
            f.write(URXVT_TEMPLATE.substitute(urxvt_version=urxvt_version, 
                    urxvt_file=urxvt_file, urxvt_patch=urxvt_patch,
                    urxvt_sha=urxvt_sha))


