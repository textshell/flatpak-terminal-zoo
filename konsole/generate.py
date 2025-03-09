#! /usr/bin/env python3

from string import Template

T2 = Template(r"""
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
                    "url": "https://download.kde.org/${konsole_dldir}/${konsole_version}/src/konsole-${konsole_version}.tar.xz",
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

T3 = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.konsole${konsole_version_b}",
    "runtime": "org.kde.Platform",
    "runtime-version": "5.15-21.08",
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
                    "url": "https://download.kde.org/${konsole_dldir}/${konsole_version}/src/konsole-${konsole_version}.tar.xz",
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

T4 = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.konsole${konsole_version_b}",
    "runtime": "org.kde.Platform",
    "runtime-version": "5.15-21.08",
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
                    "url": "https://download.kde.org/${konsole_dldir}/${konsole_version}/src/konsole-${konsole_version}.tar.xz",
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

T5 = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.konsole${konsole_version_b}",
    "runtime": "org.kde.Platform",
    "runtime-version": "6.8",
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
                    "url": "https://download.kde.org/${konsole_dldir}/${konsole_version}/src/konsole-${konsole_version}.tar.xz",
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

T1 = Template(r"""
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
                    "url": "https://download.kde.org/${konsole_dldir}/${konsole_version}/src/konsole-${konsole_version}.tar.xz",
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
    ('14.12.3', T1, 'Attic', '382710cee174c33c2db405b6c0ff399df657a5c9c7ad448899ba5176ed354a500f95e555058a5cd484b464dcb3260b28ce6665c1daaf6532dd66d9f4d273edff'),
    ('15.04.3', T1, 'Attic', '71a4381e89821be3aa287d9de13533f54ef94ca7d5ef11bec190d338d9e35226fc042a7dde998fc317cf707c3d905b59bc27d373b7cc43caf018dc755ff4fb5a'),
    ('15.08.3', T1, 'Attic', '7e32d239769684884737f7c2f3a9597a1107eccbae0208d7b4f1521a1b9b88fb88759099ec34b37f008f3ca6d4dbb727332915b07910a34f98f518e803694ba8'),
    ('15.12.3', T1, 'Attic', 'c6adbf6b7e5817a8d374f34f9310d0946baa245736c93d80493f6b50d77157f037619368f22fe27a6facdb2d0256f50126fac220592d4b1e6a6f74f1130019fa'),
    ('16.04.3', T1, 'Attic', '2658791533e8ea83a4fdd2cacbcddbde7a6dc17e6302b54b5341c1f5c3e83557980ff90fc3417ef4e5d6d54a9979d58581cef6fa1037db8abb95662052fd706c'),
#    ('16.08.3', False, 'Attic/applications', 'cc0b2b12efebc002fc731bb00943835d383c881206bf56708dacc84a830b285af44b38cff9683521bc3fca13196c40e210f866eb6bae1ebd6a44386ddb0d2de6'),
#     ^^^^^^^ does not compile
    ('16.12.3', T2, 'Attic/applications', 'c6ce7e10434949cb90183361780322a44f720e304ed14203522d1ae3ad843460186b0abb11432ce99b1299a03ec590f4af4f90aa13238b7e457ed7517c8f2934'),
    ('17.04.3', T2, 'Attic/applications', '698ea2bd7ccfb280b5909f88a65e46b9feda6e251e25e86b198e68c178fcd46498466f1e63457ac32342dde4abac512433c9ceb7489cc413843015a1828aab48'),
    ('17.08.3', T2, 'Attic/applications', '1d2723ba3dd988b3b1deaadf5ccf10455bf48d9c5961e9d614342bd5c0dbb7b42b461b529f4eb6a5ba855951f5b2d7d1d4f93170091ea3b47f02ac70c2583f4b'),
    ('17.12.3', T2, 'Attic/applications', '973c47341ebe729442ba8f8a7523eccaf5da28afbfe236fd4ec2897f710c3967f22ed5cd8f2f997f631a5369625c830f7a4540cdf6953874c2f556f547c413a0'),
    ('18.04.3', T2, 'Attic/applications', '0809cf4db6e10e672a4a976609045fb88879fe615b48e452f140da0a6c44971f31a7b4606124ed3b7642ee3f3556ace45b31e0b5c466df611fea98a9cf702066'),
    ('18.08.3', T2, 'Attic/applications', '3dcc5111e7a7fa389dda862b4a895379ffdb7a39d6568b3b958bf36631e3b3424a6abf2b9166f8567fcdf2d2d6f305a2e13f7575ce63549b0ebb4ebc27b33a82'),
    ('18.12.3', T2, 'Attic/applications', '9fecd316a9bc7adaca9a3fac38a57d293286b6328e88d96ac1cf8967fcb67ef8e9a5b085e185c4373599eafd0eaa18f0d73df70df16b98a1badd9efb689e1f7c'),
    ('19.04.3', T2, 'Attic/applications', '20ec8ae12268110f00999b9f1197aff667ee2af7d7c2747b4d142c9db48fceaca7c01ab8f12fbc541cfc79eaebcbd704e166610f263c46083ad9fefb3c5da848'),
    ('19.08.0', T2, 'Attic/applications', '9f1b17c62236fd28615cc083d5d33b2360e8a9c903d4076628018064b3240b012f6bd719fe1697f7d52c68a14f88fcfc6281986e251b62cf2571fbfdc777a412'),
    ('19.08.1', T2, 'Attic/applications', 'e68d51f6307c68f3e0ac2df9f2ab6eedac4984e04154bbc29d67ad6955c6210ebfb659488aac44a797e7e26d4cef0fa0e069e25a1d17a250b73a8cf0aca01696'),
    ('19.08.2', T2, 'Attic/applications', 'b781e1e6a19b81a49722fa04d568a53dda2c22f72ee197ebf7bacb9142d260ce3071a12cfada905d029dc2ab43a047205175cde5906a4033fb8bdd20876c1af5'),
    ('19.08.3', T2, 'Attic/applications', '140a34b8f73786557b71ac5b23b500950c598ef88795e660c7fde3077c9f5d842ae1eed73966eb14dfb54d2833fa63c310fa2cb340a81c30f31fdd77e9f263dc'),
    ('19.12.0', T2, 'Attic/release-service', '3a9bcbc9c07eafe178406d4ea5eab06c24ede5fcb7ad43dc8b0a46776cdd64ce6d2033ea1083f648370cdb50eda4e93ec1cdd76e318a2d7ec44f46b4be75e89d'),
    ('19.12.1', T2, 'Attic/release-service', 'f838d68733935f7e082ebb0c09036987bf2c13fc27bbd75ff3dbca2cd67bc4c5f9d63b52d032e3f4f5205079711d4f57eaab2133f5fe56a956ddb0aba204f5cd'),
    ('19.12.2', T2, 'Attic/release-service', '90d0bcf53a6721fb9bc7391be961cd6ed83fdb4c6ad1517fcaf1685e0aa2c9d4a3a7755c8036b6e54f35fa087dc13d4effb076c8218e7be5c9e13da63e12b9f9'),
    ('19.12.3', T2, 'Attic/release-service', '980a7eab4efb219acdda8873318980ba14cf7d3fc4f78ac171f8ed1e11400b3028150140aac192820771a0ac8e596fc0f6497c4a44d74bbd1c421f72a39da289'),
    ('20.04.0', T2, 'Attic/release-service', 'eb260752cf62c418349a8a2ee91e5a9a8f0450190f6d8ffe3c6ac4d7131e858e84f0f520c447588f60143564eaac9b5f340d90562fe507ec27846a82d0bc73f4'),
    ('20.04.1', T2, 'Attic/release-service', '608bc4e9652e1129b219867c01b40ea2aba4044b9827b6b39ef0d2fed436dfd091c3cd4f568673122761ceb3106e8304d490b0ad5b73210d1890a5ec9e516fa3'),
    ('20.04.2', T2, 'Attic/release-service', '0f998c6f69bac905385b51c2d2af3b4ed1e835e1a33208c59238e3950c6c5cf3580a435ea5acacfbd031eecf2308e2c96e9df30f1ccf44154a2a637ca073906d'),
    ('20.04.3', T2, 'Attic/release-service', '37607f7aab099b48478179eeb7e40e25a75c3c0b1b20496ae34ccd883d6f30644206d7ee95ebd56e9620b88b80700a03157671dfecf538767e6cad476632d813'),
    ('20.08.0', T2, 'Attic/release-service', '4e9640ba8888d520c07ce57f838782c874b89972acb3cc8253ae72f1d2d92d074bd5e10c7a579206fcf7ab6589ac709391a593dc7335e6a85f3d17cc8c247877'),
    ('20.08.1', T2, 'Attic/release-service', '3321b97ee738eee10a7bc7f1085b1180a4cbbad67c587149a9acacd96439b89ec5e463028a44f9b9590308614d2c37acca7b31748e290274021031528ec7b995'),
    ('20.08.2', T2, 'Attic/release-service', 'fec5065d1708a1a45894fe658eb7600cc074343e0173e08496346718db6225368c39a5d7c32fe172ecd5414b7d3ef3a1d859078540051ec72aa4861c606a5cf8'),
    ('20.08.3', T2, 'Attic/release-service', '8025548b02523c58d4f98ea8950b1001a0223bb8c53d506928707f97d96a3ca4621c6fa6fbf14eb9ffdbe1cd171b4aa9ed2f8c8808eafa166d0f6764f590a5cf'),
# does not build
#    ('20.12.0', T3, 'Attic/release-service', 'a77127618167d451ec1ab6d6879a4949d5bd268cfdc827dd31f8bea0b69f71aec1c3e5ccb6d34767b5fd13cb9f9a6157acead23311c796adb9b72f6265e2b95e'),
    ('20.12.1', T3, 'Attic/release-service', 'c2791739afa2655eea9ee87d7513f5666540a1d3e488426af32a9033925732e04b2ccfd2036102f224220f3dbf3505af196857c5f9aa7340f11456fcee509f61'),
    ('20.12.2', T3, 'Attic/release-service', '022cbe43ae69480c17e7698e60b3f5a30256268aa650a476f2c69f5e8446b9d4ec9d60f1d57cef69f641c6026b7ef641d5bf4c88cc8642a8231cf46561a03700'),
    ('20.12.3', T3, 'Attic/release-service', 'a48eaa0080b26369f5f163f3ae345bca7f35aa06d581ecc0bbeca54fee2e9b900a4b648f940a67f506ecb00dba971220f1c1c7a699efcbb6e27ee0932c27e37a'),
    ('21.04.0', T3, 'Attic/release-service', '35cb9822c442bc3dcec0539451f2bd1672c27ea522a2dc412e7cffbd805497c58711a9035e2af3ba5cb804dc42da5563bb3a6017774d22000870bc9e7450402e'),
    ('21.04.1', T3, 'Attic/release-service', '7f0ebfc28ea804d9c4b20e4aebdf11d26156d6638674d1fe5a3e66b79b0479756e51102c65df742bda10746530d6e04e9f708b7a911d26abe887db0b18f515e1'),
    ('21.04.2', T3, 'Attic/release-service', '3845177f8fc3e7948e13812d6c14b1bc0964156b8dda9656b6a6929c40e2c45c7025ec3a8d6922500a5a9981cbfc550afd1827fa64c289d6d2591713ca1f721e'),
    ('21.04.3', T3, 'Attic/release-service', '490271a51304d5a64111f6ae74422a6b3143a5349359e55af0845c04a6e6d405fadd1f300dc4d866b7730c0cb852bebfddbb33b0ca9e68d22f264e379d1868e8'),
    ('21.08.0', T3, 'stable/release-service', '7b59b43e1dd1374001570c7bc611c00c7de738cdf7030954173a8d5b901412cb5653616c12f0b85af38a48e3598bf64d6bce9ca068b520a6683f5fb7bac3c38f'),
    ('21.08.1', T3, 'stable/release-service', 'ebac48f71bde793e39fc2f3c0dc39f8fc24e6f9ba8447988ee793ef33154bcbc7f97dfe863b708acc85c472e424c4190625fc8139417f4a98520c4c9a903903d'),
    ('21.08.2', T3, 'stable/release-service', '9702effe79c63564ab5eeff597ce5652259aeb4e8125762b119783697b5fe6616c7d31688f126d552d29ab5864fca1b1fabb4d598e9cf103d960852e7c418e60'),
    ('21.08.3', T3, 'stable/release-service', '9a01678b609ca0a9f74327bb315957c2d395f80d4da14442ee0b58ba3eef54c5c4ac49b5c4d6a8ef5914502395e8d0b730472b93dea7eaa7b69cc526d2feb6c5'),
    ('21.12.0', T3, 'stable/release-service', '67d0671e78bc8adbe52ed5afed6c2ba0a5e6f28f1f261bb02c5b0e7da876a5116dac4dea89bbb66e6ccce20464723cdd6871916baac3c9ef45c2bb36891c129a'),
    ('21.12.1', T3, 'stable/release-service', '26963b05937109615fb0963ed7a9367d95d4392b0fe0dc36c140b3fb71a092ef7380bc66000e6a122c571a57590d92151bdc29fbc9ce53cd7793392c7776fb77'),
    ('22.04.3', T4, 'Attic/release-service', '05728efc051ae76b395c7ece1599e654ce3bdae0c8b43d7f8e34c76f57041f7722e161147c4a5699377b764aa8b3799421d5c735967216c5420b6f92330c1338'),
    ('22.08.3', T4, 'Attic/release-service', '5f452cea9bf5cc609c89968eba3177b5a89103c7f160d1d41643140af98f95b74b1b4efcdea4119afbd745800922b66b7ab96a077d1c61096802e6e135d81bce'),
    ('22.12.3', T4, 'Attic/release-service', '8dd29a2b8dfdb62a096e924de617c0a028dfc3c018035140c50a63d564b8282fd702d4d8a265bd28f6b55bca5068b37dbaf3b047c2ba56eb43cb28887ac9c4f0'),
    ('23.04.3', T4, 'Attic/release-service', '9d332efe21dee41c6f34b91f373f4ac15798ad977e429f5f57995a619a9ebcad9e506c21ee811a1ccb595509cfd15a33cef721d01573b1245f2798a88d93c04b'),
    ('23.08.5', T4, 'Attic/release-service', 'dd227f0446b623839f984cfa2f00b94e16c929f35b4714e791a11baf90907ac87ed469f50980a07e6528fbcc1654192d2504676b73d7856b6389077a4ef01f88'),
    ('24.02.2', T5, 'Attic/release-service', 'de3154d198fb3e7bfd91e06faeafafcf75478c85af46443c04bd98e5a267bd0eea28e162cd7827858cb9c17880bd7f947983bf81e9ba8aa6647820691cf42042'),
    ('24.05.2', T5, 'Attic/release-service', '47b2fdfc4b79b1e8cef72aed9d77858347c0c89e7b0cd4106a2f0d362ea72a2d54b79385deb8525654a5b0da0fb19c8e1db370618a6f0ae2d8e1aab41e7261f3'),
    ('24.08.3', T5, 'stable/release-service', '39f012c233517b2185c440b03548502e044b0a6561587e40227ef339637e2fa6b8a635873da028e9356dc99fe2cc76d5dc8d957189f2a4b5eb561543c2ab5cba'),
    ('24.12.3', T5, 'stable/release-service', '11f24bfde9aa1bc8b26fd3faa5d9c49cc493ca24150236586e64177e003be6eac2226868b6bed283c4a02e5e5a5177b64dc27a1eb22acf524d403162968a17cc'),
)


for konsole_version, template, konsole_dldir, konsole_sha in konsole_versions:
    konsole_version_b = konsole_version.replace('.', '_')
    with open('de.uchuujin.fp.termzoo.konsole{}.json'.format(konsole_version_b), "w") as f:
        f.write(template.substitute(konsole_version=konsole_version,
                konsole_dldir=konsole_dldir,
                konsole_version_b=konsole_version_b, konsole_sha=konsole_sha))


