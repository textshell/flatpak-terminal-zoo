#! /usr/bin/env python3

from string import Template

VTE_TEMPLATE = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.vte${vte_version_b}",
    "runtime": "org.gnome.Platform",
    "runtime-version": "${vte_runtime}",
    "sdk": "org.gnome.Sdk",
    "command": "vte${vte_api}",
    "finish-args": ["--socket=x11", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "vte",
            "buildsystem": "autotools",
            "build-options": {
                "cxxflags-override": true,
                "cxxflags": ""
            },
            "sources": [
                {
                    "type": "archive",
                    "url": "https://download.gnome.org/core/${vte_file}",
                    "sha512": "${vte_sha}"
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

VTE_MESON_TEMPLATE = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.vte${vte_version_b}",
    "runtime": "org.gnome.Platform",
    "runtime-version": "${vte_runtime}",
    "sdk": "org.gnome.Sdk",
    "command": "vte${vte_api}",
    "build-options" : {
        "cxxflags": "-fno-exceptions"
    },
    "finish-args": ["--socket=x11", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "vte",
            "buildsystem": "meson",
            "sources": [
                {
                    "type": "archive",
                    "url": "https://download.gnome.org/core/${vte_file}",
                    "sha512": "${vte_sha}"
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

VTE_MESON_TEMPLATE2 = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.vte${vte_version_b}",
    "runtime": "org.gnome.Platform",
    "runtime-version": "${vte_runtime}",
    "sdk": "org.gnome.Sdk",
    "command": "vte${vte_api}",
    "finish-args": ["--socket=x11", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "vte",
            "buildsystem": "meson",
            "build-options": {
                "config-opts": ["--libdir=/app/lib/"]
            },
            "sources": [
                {
                    "type": "archive",
                    "url": "https://download.gnome.org/core/${vte_file}",
                    "sha512": "${vte_sha}"
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

vte_versions = (
    ('0.28.0', '', '', '3.0/3.0.0/sources/vte-0.28.0.tar.bz2', '5f9549ee09dd1d100bf0e90f81b12e8237ba4cedd79cf2fc33edb81edb5796ff23a88563a12ae808cdc057ae2ef508999426b36a4985fef6dc008431f1aa38f0'),
    ('0.28.1', '', '', '3.1/3.1.5/sources/vte-0.28.1.tar.xz', 'f76d5d10da069ee2a6235abc5a7db883dd2f582a58b935e8cd8150b4af8215db3bfddef103485a07c0d23608e5eba8e462d73e177d2a61a7bd97a69dd3cbf2af'),
    ('0.30.0', '', '2_90', '3.2/3.2.0/sources/vte-0.30.0.tar.xz', 'bcd35227100f326b5260db31239537f19604ce2ac7f735c4d39485640fd4f5c18bbc2298ccefcca657b8707e51e1028e145d0f367b67102ee89ddf2a6a7b914d'),
    ('0.30.1', '', '2_90', '3.2/3.2.2/sources/vte-0.30.1.tar.xz', 'b7e601f207fe87c56826b093904a27f90e51e8992707d5978ec058fb91c1c790287af8bc2594b8149f4a69223cff2f2c73bf13a43507f4ac37df7c3faee69e60'),
    ('0.32.0', '', '2_90', '3.4/3.4.0/sources/vte-0.32.0.tar.xz', '729e1dd7261fd0394a7a4a566b2076c49ae9f90505c701e663cbcd6833891a20b9a2120b4334694aaa2757312e7f973488bde6c02b3d2681eb4e116fc2842ee0'),
    ('0.32.1', '', '2_90', '3.4/3.4.1/sources/vte-0.32.1.tar.xz', '8c4d63f33ba99e8c39ee5fe6b0998dd89aa7415d35765cee4c42116e7cdb8aabc958471b68cc88a35c937949a9043678ce4ae74541476b36d5617491e8da6224'),
    ('0.32.2', '', '2_90', '3.5/3.5.5/sources/vte-0.32.2.tar.xz', '0346a3a85de8bfc84fce37f073154ee7af746b8872e7970f4f58e11cf261311def714100370c2eb371beecba5d22207dfdada7b0df7fee00f32035e93b9e8808'),
    ('0.34.0', '', '2_90', '3.6/3.6.0/sources/vte-0.34.0.tar.xz', '80c2f1c6b310324c05fe1c2373583280a7c32950ce4601151a9e81f24bf0636260ec2f02979437c99e5e9f916301ea694f2d40083f974fe92b8624618c2c0a73'),
    ('0.34.1', '', '2_90', '3.6/3.6.1/sources/vte-0.34.1.tar.xz', 'a80f74a9699c2c06b4bf269adf16298724c07d749fffc1c1dd7f3f5a89d3bb08f4d3db3aa888dbc3dea4be75846eb5ab6c794e661cc5c192fca9235aff293cbb'),
    ('0.34.2', '', '2_90', '3.6/3.6.2/sources/vte-0.34.2.tar.xz', '4a89f149e9c101ed31b76086de1a05287d9c2a750ee098792fa9508b8712fa065a63e60d50cfb4a060991c2f6f182ddb91d3f21d4c7baf61337f08dc1a960a35'),
    ('0.34.3', '', '2_90', '3.8/3.8.0/sources/vte-0.34.3.tar.xz', '6eecde8d4f03eabd5710850b4f559d1f55ab98a201b6611428025579a6d43d52faa80d6f6607a6b93e42b5efda597f2b8507312113b939574ff7b73a3bd134ef'),
    ('0.34.4', '', '2_90', '3.8/3.8.1/sources/vte-0.34.4.tar.xz', '2f1dce6ed47835b098c37351fa665ddbfd8719a4275672925d8030655cd96412ec7f3edc23e9d94a3e035a36969c74c5186d1689dcf1e1111071158e64d2360f'),
    ('0.34.5', '', '2_90', '3.8/3.8.2/sources/vte-0.34.5.tar.xz', 'bf49cffe9f5bf243aada353adda1d8f86d75883bed343792a16d69d8956e9fc6f846cd1c317c7b2b03ba446de9c645cba52384190d5343f5d000a4557b40fb53'),
    ('0.34.6', '', '2_90', '3.9/3.9.3/sources/vte-0.34.6.tar.xz', '185703bdb8d4d46c1f340af8daa41194fcd28fdffafc77f190e776350f4bd875000e94b6cc481da19cb1f8da26ae2d757f4a29b703833e71fa20fcc5ccb329fd'),
    ('0.34.7', '', '2_90', '3.9/3.9.5/sources/vte-0.34.7.tar.xz', 'a122814f7fee4202c0bc4862798c98b078e5b185eb8c3c11959001b33bd5e029579f7337f85bdffb3f8a7b22af3a6763a2353ecff16a8e5c8b941431adabc5e0'),
    ('0.34.8', '', '2_90', '3.10/3.10.0/sources/vte-0.34.8.tar.xz', 'e4a7b691d0affcb05c463e0eeeab42591e13679f8b8cd042869b2b91aaa82c24222734f68767e3246f2554f8fca481b35383239ecfdb39e5865fc9b8b3b8479b'),
    ('0.34.9', '', '2_90', '3.10/3.10.2/sources/vte-0.34.9.tar.xz', '57fff7d5916bcd8a8a13e3cf050f85ed78e9154fdf2510a6d6f594f938c6d56f512089c6bc3e06c9123d35d17f2eb3b3814a5407635027ec0116c25f73034688'),
    ('0.36.0', '', '2_90', '3.12/3.12.1/sources/vte-0.36.0.tar.xz', '7666fdb2d3458390b154add7da781cb973498b019d859a3396797102dc4840d9bdbae44c83257a3c67609e658173dc0d5ff382b0343a5bf3c6db43e04392893c'),
    ('0.36.2', '', '2_90', '3.12/3.12.2/sources/vte-0.36.2.tar.xz', 'fafd368b95918024e6324c81f4fa6c35ad15138ad44af2f92164492d9773b127202d11824c9def4a26e17de44336f42e9c8906330dd300795c280ca068381632'),
    ('0.38.0', '', '-2.91', '3.14/3.14.0/sources/vte-0.38.0.tar.xz', '624d8c9e7d4429c21830d4bdbd325d3b9a75e35ecad0494fe6051ae339745c59ab656af4989d632e638402bc1fedf4c4f69387d39bf731bd6eabaccf682b1bc0'),
    ('0.38.1', '', '-2.91', '3.15/3.15.1/sources/vte-0.38.1.tar.xz', 'd6e616d2f327ac6c28ad9ac11f0e7a081a5659b9ad90dd3246fa4240a8642ed1ffe87502ab4307527e03789195103cc33d3f783f2d89e7c866c0cc8d5cd0e24c'),
    ('0.38.2', '', '-2.91', '3.14/3.14.2/sources/vte-0.38.2.tar.xz', '4c493e18cca4b50d66640d282d7d33a471d1ac4bd2dd929b059b829a42fed852d202669751b266adf7291502203e26c513b6852b3035458d41a433b900b0c6bb'),
    ('0.40.0', '', '-2.91', '3.16/3.16.1/sources/vte-0.40.0.tar.xz', 'f7ff28cdefc80e7fa5d876b8cba5d396fd98aa13c21a6cd320ac4042a8747e67ebf7a7c13ddab7bebb6b839231aebcc4fc25be9f0cc6c55859886c7948d4ac79'),
    ('0.40.2', '', '-2.91', '3.16/3.16.2/sources/vte-0.40.2.tar.xz', '06d1c9a34e8e82e1bd54810d245d908ebb837538ba19fbaabe683cdf3b96b7cb1630516ddeabf18b0294922b8d98d2b9a2f5028c171fac2ad913974d94555eb2'),
    ('0.42.0', '', '-2.91', '3.18/3.18.0/sources/vte-0.42.0.tar.xz', 'e2b2c00c81af05cdd5d99fd2de4fcb9019cffc5bd8b59878b7676cf7104c79a0c095b28d9a62586e3a531e00b80ba70062352ca1d4e96a902fef8d8f1121df49'),
    ('0.42.1', '', '-2.91', '3.18/3.18.1/sources/vte-0.42.1.tar.xz', '4cf917d3f343973dcb816a341276bfab7784a9f4dc6f8fb402193e9a9062503ac192ccc274fe92bb20a17ac182d21fd2268bf9c1ddea817f730db5612e3b21c0'),
    ('0.43.0', '', '-2.91', '3.18/3.18.2/sources/vte-0.43.0.tar.xz', 'fabe336996fd49ac08fc347f87e2b6169a875bff5570c3e0276271e0efcb215d206c6663d961ae604ee23ea668cbcacdc0664c06ec626e0a5ee7120cc57417fc'),
    ('0.44.0', '', '-2.91', '3.20/3.20.0/sources/vte-0.44.0.tar.xz', 'c190ba6cd4785fc16b1982517a0fcfe2935e50082acec095bdb5d56467b4952fdd48340776c2a4ecef4da847a668a56bca4599801b00f5090927a0e5f31d2c3a'),
    ('0.44.1', '', '-2.91', '3.20/3.20.1/sources/vte-0.44.1.tar.xz', '1fd352ea111cc13f8e7b2acae374e2fbd9d5025f6cb28b193164024594a5df12c9418bcdff11ff3247a9b785d6584c484a242c22df6a98afc3f0dfa1f716499c'),
    ('0.44.2', '', '-2.91', '3.20/3.20.2/sources/vte-0.44.2.tar.xz', '98db3c1528d5f458164e2d30056cd816e5943d9c569551878119e79d4fbca1865e52667393bf298f32fd54710d1b268a5aac125222ecb29ce854522be3776356'),
    ('0.46.0', '', '-2.91', '3.22/3.22.1/sources/vte-0.46.0.tar.xz', '543cdba5c51c5384e54fc372924c2667ded952cbc8ffafb7ff62f8643c6a7e2440439109eb12378ed70b0e0a256d3ef97d6da004dd8088d36bccdd7fa16593f9'),
    ('0.46.1', '', '-2.91', '3.22/3.22.2/sources/vte-0.46.1.tar.xz', '04b3f8ce922c4326d92bef605a0dbe195764946cd5f1acf28fd6d69c0cdb2ee661cc7e424436c72380da5d0250790ae658ac49d761b567dea88d92157285889d'),
    ('0.47.90', '', '-2.91', '3.24/3.24.0/sources/vte-0.47.90.tar.xz', 'c36310486b0575b26330879d2ca222ce4ca36af7659ec13113b209a897371da7ce0ff758f2c0fc5a9d42b7fd60caae8603aa564a2a5f58159979e4a9388a688b'),
    ('0.48.2', '', '-2.91', '3.24/3.24.1/sources/vte-0.48.2.tar.xz', 'cbb2835618c554d72a790e16f1ac5b3c06a8a810d8d517c475ed7ca46eeb56d7c9f9226918e13c5c84c04ce1ccb5467e62af7c4453f317a0aad197a4c179d76a'),
    ('0.48.3', '', '-2.91', '3.24/3.24.2/sources/vte-0.48.3.tar.xz', '3037b61a759cfcf56838bc7804df5a211da416bff9ddc5791f8a8d5157b90926985cfe57d7edbab42de64945d5e668470fe4129a218fb9c7af546648e1660c72'),
    ('0.50.0', '', '-2.91', '3.26/3.26.0/sources/vte-0.50.0.tar.xz', 'ac05622ecf92115cf6aef1ef7805b0ef19856d65d2dfc9792b149443aeee4c9bbfb871c600c9be8b0f4baac4a143e70412208d0a510cb53f13b2caf2caa33587'),
    ('0.50.1', '', '-2.91', '3.27/3.27.1/sources/vte-0.50.1.tar.xz', 'd5e9c7990ddb6ee789d4f4f8df05c23d794791e8381266551cf6574658ee8fd6adc4c7b9ac6aadcf957887b0ba13f7f89002fd820c8d35c789bba918414bd330'),
    ('0.50.2', '', '-2.91', '3.27/3.27.3/sources/vte-0.50.2.tar.xz', 'a1b12c74bedb167bf2a470294c566198c224c90be9b5c50366ef18d9542921f6cb2dc2329afd82f7342279c3eebd4ef5dfd753b4feb9d4e3e194cb878b48a7a2'),
    ('0.52.0', '', '-2.91', '3.28/3.28.0/sources/vte-0.52.0.tar.xz', '2f8b1efc7c73c4e74070d3bfcb33e61672d6ed70a352eed2c43198f8c3ffb513f6ed98dcf822dbd55d31d914c7f9dc157b29f8e4781705ee2c9ddb0e43c6e5fa'),
    ('0.52.1', '', '-2.91', '3.29/3.29.1/sources/vte-0.52.1.tar.xz', 'a1de54950cdcac9afccc1b13bd71b65ad1d6f93055d0b005b4a15b6f84f55029848cf8f2f9155cf3e6edc69fe973529fd4313f59af74fc1035aebd4c0b85655f'),
    ('0.54.0', '', '-2.91', '3.30/3.30.0/sources/vte-0.54.0.tar.xz', '69dd0caae4eacc179f84eccf98625a31140286beca4244a8f06420bd36ac62dcaddf9e9d8b114549ca97927e94b562df3e7daa9fad971484f05ebdd1c0f7b787'),
    ('0.54.1', '', '-2.91', '3.30/3.30.1/sources/vte-0.54.1.tar.xz', '5cb866e75c35e1b5728d17b0433641ceb4837495d59185a04fde9dd8c9849ab905a6b2718a50b27cc70323c7a6c5db31a808816576c30d7f18ece889a329fb61'),
    ('0.54.2', '', '-2.91', '3.30/3.30.2/sources/vte-0.54.2.tar.xz', '214ec69110d6ad6caa9bc41fb741874bfcf27f20f34d3ae745b13903c574f9c854f7e0dadbae3dbc8ce04c5a6eb818a433c50569c1ef802501a9a078385f23fc'),
    ('0.55.0', '', '-2.91', '3.31/3.31.2/sources/vte-0.55.0.tar.xz', '972bb4e616bc9436482dc938c31dcf62e8e00eba375554e4049485fbd1dc2f31f657fc6cd83777788781decb3b50559ee982684c8c50a139743e239dbfe078b1'),
    ('0.56.0', '', '-2.91', '3.32/3.32.0/sources/vte-0.56.0.tar.xz', 'f366ed4a28a896ba919184b50a55ee110eae43127847f34c049684bcb9b81327d1b72e9d871b2a5b7f7fa12f3f4aa721ac3d770770b600dca9c433cb2c674915'),
    ('0.56.3', '', '-2.91', '3.32/3.32.2/sources/vte-0.56.3.tar.xz', 'f78b3d532ca47e53c1bb51db6780697ce4692d493c0030d2dc4beb63a2595e44a43eb409ee31b94e4551eae259ac1baa8f06825a02fd66df8352e192f4ea1988'),
    ('0.57.0', '', '-2.91', '3.33/3.33.2/sources/vte-0.57.0.tar.xz', '87788ed44b39d57cf6d0ff99046ab575c8a410a0713e8f7404ada1239a1691f687b689a0b692f1bfe84ba7c38308382da409bab0780b1168d0ba99bbc0eb7b4f'),
    ('0.57.3', '', '-2.91', '3.33/3.33.4/sources/vte-0.57.3.tar.xz', 'f5496fd2b24af8d8eb895adaea59ee5ed4250c12a97745e025aacebca2d709901ae84befca58a3c5f1a54014a97af460ea53f844b1b1b9e32e192cc5883ecfed'),
    ('0.58.0', '', '-2.91', '3.34/3.34.0/sources/vte-0.58.0.tar.xz', '4d0fc725e0c71921b3d235d434600ad3c0807d5c0e7bd62fb782d857254db334bb851b75382c9613a5af753b5d6a1c05b174731427a8560b9b14101b3cc38c06'),
    ('0.58.1', '', '-2.91', '3.34/3.34.1/sources/vte-0.58.1.tar.xz', '1f795731fbb7ee76c4274562d5a55668c3b8ecad5a00ff83c762b0a2517ccffb85e796e937407d46e6bdb64327759eabc5878455d1d66cb1b8ff8b6060a4b1b7'),
    ('0.59.9', '', '-2.91', '3.35/3.35.1/sources/vte-0.59.0.tar.xz', '533d1e87a699137a33a6ddb82bf0f010925ba578974e1f6c87bae0b497309dd84c3cb2f5f6884f34f7fbcfad94fbaa07eb3a80387ee9f16b5f3f0ea2679e7376'),
    ('0.60.0', '', '-2.91', '3.36/3.36.0/sources/vte-0.60.0.tar.xz', '8c1a80ba90fa1c1f4b5ec1a1d3793af79c04fbbad4acecba094db79771555b1689017864bd81bee4366f9ef363f629f20731bac998d994b9bfa37ee59e9e58b0'),
    ('0.60.1', '', '-2.91', '3.36/3.36.1/sources/vte-0.60.1.tar.xz', '123a8fcc14f4dba450411f95f43eb60108fee95c328d0e7331c9366d96ba2caa548dece3e95a8b779dda19d322d6879d02abc6ac68e36450e4e72f17a0963c30'),
    ('0.60.2', '', '-2.91', '3.36/3.36.2/sources/vte-0.60.2.tar.xz', '801ac727cab33d2c3f4ba4d86bf7f19a82628acd2739196f24c85d038ba6bcc6a67239aac09141b8e0119a67f199ff8a8c653641a8e9aea1e8ab68bfd16017db'),
    ('0.60.3', '', '-2.91', '3.36/3.36.3/sources/vte-0.60.3.tar.xz', '3694fe711e0b3eb9d6ba37ad8036f5d3cca4265635ed7afcde750a8445b17f820d1c55b557d0ea1c8a5a45e5408915d8da2ffd65b4d397c6582f288812ae1f18'),
    ('0.61.90', '3.36', '-2.91', '3.37/3.37.90/sources/vte-0.61.90.tar.xz', 'a52d9afc0c60f4d3d6724d3e196c58fa40aec0bb5c4650affdc103abe02ecd452cccb4b8f7dfb2f6f041033cea96fd84018b7727f83a4764ec90cc7987d6245b'),
    ('0.62.0', '3.36', '-2.91', '3.38/3.38.0/sources/vte-0.62.0.tar.xz', '8942809d20ff845142dce8cf48b4eb6f9e4f333dc2647cceb0538112d5e10096ff836f24da1f0c34cc4bbee4f6c585c3feab33934c257887a82d6c67bce11402'),
    ('0.62.1', '3.36', '-2.91', '3.38/3.38.2/sources/vte-0.62.1.tar.xz', '2f8f76953e0ea6c604357ab08630d3822a252051d8997cf7714553fec1688735468726bfd74e03f122dd1c8d0717e511ec7ec1e5463a086bd407afc6f7df91cf'),
    ('0.62.2', '3.36', '-2.91', '3.38/3.38.4/sources/vte-0.62.2.tar.xz', '61ea130d43d60531dcaa8bddfecacfd4a934a2e868da69b598fad0a2feb04885fc0b5dd520dac4b0d3a4daf11ea70c5357066ed15759e36436346dae498e8ef8'),
    ('0.62.3', '3.36', '-2.91', '3.38/3.38.5/sources/vte-0.62.3.tar.xz', '0475e2813b305bf1b5d48ece5959f2feb10e89b589fa3b75032ae466fd5254bf5c2fc6085dc296d65c5df84790a38892534ff401109843bf964ae62a8c540a81'),
    ('0.63.91', '3.36', '-2.91', '40/40/sources/vte-0.63.91.tar.xz', 'f14b655ccb6429eaaf064bbbdc12f2322b7c646b8f2808e7fc42101cb459829fe688adeeaff11e699932882fb7a8185de57010e41b5ab957ce6d727e489f74f5'),
    ('0.64.1', '40', '-2.91', '40/40.2/sources/vte-0.64.1.tar.xz', '46a066a73929ba7aa31defc9e2a6e9c531375484a845b9b1e3d9760abd4e5864a66e83b50d72907743fc6afc59c88c4097f433c0b89539f1428be500779350b6'),
    ('0.64.2', '40', '-2.91', '40/40.8/sources/vte-0.64.2.tar.xz', '67facea1f2507183aa5fd51215a404d6e754be5694e49c8511d7dd841192178a583e9416b2611dc6b5f635555ac2fb9f48a8a6e68e6e4673c4d93422b7555061'),
    ('0.66.0', '40', '-2.91', '41/41.1/sources/vte-0.66.0.tar.xz', '68f71a695fa935d6aac0018d683d7d467543caff3164e86243067de493cfbc8f6b4759a181d99a1a67da518ba60d30f80a36a85556f58330cc4c5cd53adc4eaf'),
    ('0.66.2', '40', '-2.91', '41/41.3/sources/vte-0.66.2.tar.xz', '6e89947f22c866a79270c700f761ec393ed8337557d4c6a90f3b7ba61caf7189406ab7731142754c99f121add6b483063d1b21e7791d2db148ad37abb7b525b9'),
    ('0.67.90', '47', '-2.91', '42/42.0/sources/vte-0.67.90.tar.xz', '867a3dfe9300a7ff691185e72195e3550c29d52022dc87428036d69f36710747ba2d76f26f989a9ed9b5c18ddb30464f4d42041e06264154143684ffb6949c10'),
    ('0.68.0', '47', '-2.91', '42/42.1/sources/vte-0.68.0.tar.xz', 'c5bd53cc449bf7296f2288f788770d439254c4b220d51dc136f0660f932fff84b1c2a288febf0040b9630f15dea34ab2fdf6b2696283cb8bc7285840eb91fe63'),
    ('0.69.90', '47', '-2.91', '43/43.alpha/sources/vte-0.69.90.tar.xz', 'fc5506cc6c089c1dd7cd6917318b338e8f374340ac73046856f5dd0c2d99b6cc9654a8b578b1137766ed35a5352b7a4a2865639e63add7d845ab99c3b7d385e6'),
    ('0.69.92', '47', '-2.91', '43/43.beta/sources/vte-0.69.92.tar.xz', '0c49219b26e3a2802ea458ad2bb4dffd0dc43ee67f4006cc33e55a1c5e0108cf42f3121cea1164b7466ec67ded174d27d2e97477d8b591b82989033bb758676e'),
    ('0.69.99', '47', '-2.91', '43/43.rc/sources/vte-0.69.99.tar.xz', '22dee0f196912e48e26434316728175ee4851faef6b9056eb56c1ef9427ffa139a75243a3c1b79dfdd3df252a542bf467add062b4a5498f1c037989e44f59ee9'),
    ('0.70.0', '47', '-2.91', '43/43.0/sources/vte-0.70.0.tar.xz', '9058a844b68a16e9b3f7a5808e46b7adea0743063bee33a4d6239d42d2e6b2c26820254e3ac1615d00865e5a6dd71737fa6bd4ce604977a18fdafa7178303e99'),
    ('0.70.2', '47', '-2.91', '43/43.2/sources/vte-0.70.2.tar.xz', 'ca54686a3e6cd8166be7f2d7fe93aaecde0845764911b56a6ea48918041b39d13da1ad9e2660cfac27564bda3236be001ca7dc87ab4576339c50fc2d3b0238b5'),
    ('0.70.3', '47', '-2.91', '43/43.5/sources/vte-0.70.3.tar.xz', 'c7aa25365e8f4fa0a8a1a102ec31b2dd215151cc0d84a5087cd5f40977b903ab6aa580b2223cf0c0d76be4a8f1669369f2986fcb7fe62235e903ed805d60cdf5'),
    ('0.70.5', '47', '-2.91', '43/43.7/sources/vte-0.70.5.tar.xz', '05a385de143c8ae5ee5e3c2dac479b258c042a2928d6d4412df8ae1d15d35a5182ad794d260cb7c4c89054a48fca3285cc333d7d533e296865f466f93e84b20c'),
    ('0.70.6', '47', '-2.91', '43/43.8/sources/vte-0.70.6.tar.xz', 'b842c45975d4dc0c339fb00189ed33d13539428dc03e153a513994155feef3aaa47efab7d590449aa44633f09e1412fd57ada7c3b9dde16825b42ba3a8643ab9'),
    ('0.71.92', '47', '-2.91', '44/44.rc/sources/vte-0.71.92.tar.xz', '7711607b4a0a28bdcf0d73be46dff206c40baa4b5e0b32c32b517114e9fbe2050a76150d5da48429644dc7765172101a910cdd74166c7c28cea07e0af6ca56a3'),
    ('0.72.0', '47', '-2.91', '44/44.0/sources/vte-0.72.0.tar.xz', 'df6713b260491e55c6c9f92842d62020711d77c81ee67f41f79182e436f83c588e8fb87b6d2d07e33ba561f6544274cae895a9d5a0977fcbf48bece55579a42f'),
    ('0.72.1', '47', '-2.91', '44/44.1/sources/vte-0.72.1.tar.xz', 'c3c3b6e00953b08ef2eb089fda7b5d0f04db9b8a7993fe6bff3790f6f436916afbf7fa5970e7dfbecdaedc5c12107e5787a6c4e272a9b2ec99baa0c95b7ef386'),
    ('0.72.2', '47', '-2.91', '44/44.3/sources/vte-0.72.2.tar.xz', '40562ca7c925d9b1f6937d5aceb1d0d8852339d3455569aaf92a684fe7c785f0c4023dbbc0f6f60ceb17a5e70ca41587ae0bd153bdc2d3cb27951f8b20598f44'),
    ('0.72.3', '47', '-2.91', '44/44.6/sources/vte-0.72.3.tar.xz', '53e5d382c57ceb528ba4c8e73f2ba02cfd6844ef7cb6014e77781c582475e8b3e6acbcf8b25aa5ddfefc7a96b4337117b285d00ce0be435361a583afa78b145f'),
    ('0.72.4', '47', '-2.91', '44/44.8/sources/vte-0.72.4.tar.xz', '945b07512efe4e3ad8fdbaf54ac65d7a0d2a345862c4fb1248dfc5a9ea29452a253df7a02c8314507e460daa35597d4d7fc918e4d5838a09b710ffb681e7e15d'),
    ('0.73.93', '47', '-2.91', '45/45.beta/sources/vte-0.73.93.tar.xz', 'c9ad855876a85885d9d4a7a1a2b7f4e193e3473314c28a492b47778cf3f418864a50f677757760f602e603daa44fc143d645f082cfa65ab6302d11192c7e0abf'),
    ('0.73.99', '47', '-2.91', '45/45.rc/sources/vte-0.73.99.tar.xz', '97897d62ba74aef1401930a92d6cddc9a929a2b631f05ec3887997cb2b96f3b53c1b6a855f870684b17ab91598fab73bca7abbc9cbae88cf0a9d20b7f3dba101'),
    ('0.74.0', '47', '-2.91', '45/45.0/sources/vte-0.74.0.tar.xz', '4e33c0545641e553ec5b8b2fe0a953f1b4ee28e4e9598753eef3a4a72e7ee19bbae788cc31b7473ed14eb494eb5f5b32f186591339f213af194ce4b6b20b5929'),
    ('0.74.1', '47', '-2.91', '45/45.1/sources/vte-0.74.1.tar.xz', 'e193422d4ba197a733033d0e10d1b6906798e165fb85b73e66c8941d0b85ff8aaac56c1cfcb1cb7da598fd2e54d3850368c6ea323c97a9f59cb048a03042eecb'),
    ('0.74.2', '47', '-2.91', '45/45.3/sources/vte-0.74.2.tar.xz', 'a4f9cf8560a062d05eeac41d3a97ae58ea3b9b136faece0e8d16dacebd0f5d9ed7a91f724c643ce7377aad130268a71cbe611909977717d0f3af7601112d67f5'),
    ('0.75.0', '47', '-2.91', '46/46.alpha/sources/vte-0.75.0.tar.xz', '1b87cce6992a4c33a95e6e16e8156c1decb3b7869277529572e5c79b8798b3587ec0841e613c0dcb37e82e6179feb6ebe2c53bc3840edcf32eb65b02be09f127'),
    ('0.75.91', '47', '-2.91', '46/46.beta/sources/vte-0.75.91.tar.xz', 'b77739270996dc7ae70b02fff66741e37191b50ab8e618b77bbb14ab27190686dc4aa6f01b443445ac3c6a7e1cafbbbeeb464bf5f05c719c1a4cba62d25959f7'),
    ('0.75.92', '47', '-2.91', '46/46.rc/sources/vte-0.75.92.tar.xz', 'db41d19c42eb27d26632fb5d406fc279212064ce4b1b920628fdbf061b2782e221653112b726c06b732a134b1aaf463a77a1cbe7293ca03eb2c960cb2cdb2033'),
    ('0.76.0', '47', '-2.91', '46/46/sources/vte-0.76.0.tar.xz', '4eccdac2eeb33ae76c67000081b3ae26b0872ac3c1b89517db87a1574dc1121992ad708a0ffced34e30a0fd351166552215cf897d722b53d2313d5b8deed2385'),
    ('0.76.2', '47', '-2.91', '46/46.2/sources/vte-0.76.2.tar.xz', '206e2706c926972d4f389cf0418b840345ba6eb0336a3cae8b0d604f773b8b86746ef4986c94cfd6b0716449351ecb51a62f3ba08885b9cc8c8a8580e75f7fbf'),
    ('0.76.3', '47', '-2.91', '46/46.3/sources/vte-0.76.3.tar.xz', '59cf3241f59b7ce795098814a04816d150330e4464a2438c974ac03cfd6aa05e7e037121a6a21929d6b12eb17fb1a4bf48c936604f0e0b770e3f125adb5a4c50'),
    ('0.76.4', '47', '-2.91', '46/46.5/sources/vte-0.76.4.tar.xz', '99490ab0117418a2fb472578f06835f6d2440a4469047af02519e98f2d636ce6646e6656e8c2ba84f509de185ad490c58f39d4b85fd340ea70605377cd5f25fc'),
    ('0.77.91', '47', '-2.91', '47/47.beta/sources/vte-0.77.91.tar.xz', '9aa3dd3d56fc3d7e383ebd9b14f88b217f0bf08f78de7894cc3f9fb57d22625a1cb0aa10dd2ebcc83041994732e2bc7e0cd59b215206afa05736c7715e563361'),
    ('0.77.92', '47', '-2.91', '47/47.rc/sources/vte-0.77.92.tar.xz', '7001ec463d8201027191cb8eaa7c8db031b045b9790e23030e80945d74fbea2c346fa275c8470596d68d832067aa73768a02094daec44a77b7dee1864b42466c'),
    ('0.78.0', '47', '-2.91', '47/47.0/sources/vte-0.78.0.tar.xz', '730f92f67cc896382c666f99f01ced4ff3192007e39a7c5701478de780df1399bdd6634c7c9300ff06df6574b1dff5af7d3d3bc1e395e9c7be311212d3bb313f'),
    ('0.78.1', '47', '-2.91', '47/47.1/sources/vte-0.78.1.tar.xz', 'e709cf1d721c8082b9758e34d7ee5a553145886719311cff25243d7bfd734002a7b7ccfb9c98870a600eda726568a11728934974a1fc31ce22072d43302bbcf1'),
    ('0.78.2', '47', '-2.91', '47/47.2/sources/vte-0.78.2.tar.xz', '70c1e7d4bcab89a4b537d4575166c62063d6f722dd53c0970b6dcc277ff731bc05854f1ccb45d9679ad195bc31f2e7ee89cbf022109b8030bf01a2100c5dcb4e'),
)


for vte_version, rt, vte_api, vte_file, vte_sha in vte_versions:
    vte_version_b = vte_version.replace('.', '_')
    with open('de.uchuujin.fp.termzoo.vte{}.json'.format(vte_version_b), "w") as f:
        if vte_version[:3] in ('0.2', '0.3', '0.4', '0.5') and not vte_version in ('0.57.0', '0.57.3', '0.58.0', '0.58.1', '0.59.9'):
            vte_runtime = '3.30'
            if vte_api == '':
                vte_runtime = '3.28'
            f.write(VTE_TEMPLATE.substitute(vte_version=vte_version, vte_api=vte_api, vte_runtime=vte_runtime,
                      vte_version_b=vte_version_b, vte_file=vte_file, vte_sha=vte_sha))
        else:
            if rt == '':
                vte_runtime = '3.36'
                f.write(VTE_MESON_TEMPLATE.substitute(vte_version=vte_version, vte_api=vte_api, vte_runtime=vte_runtime,
                          vte_version_b=vte_version_b, vte_file=vte_file, vte_sha=vte_sha))
            else:
                vte_runtime = rt
                f.write(VTE_MESON_TEMPLATE2.substitute(vte_version=vte_version, vte_api=vte_api, vte_runtime=vte_runtime,
                          vte_version_b=vte_version_b, vte_file=vte_file, vte_sha=vte_sha))

