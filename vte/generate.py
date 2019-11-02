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
    ('0.28.0', '', '3.0/3.0.0/sources/vte-0.28.0.tar.bz2', '5f9549ee09dd1d100bf0e90f81b12e8237ba4cedd79cf2fc33edb81edb5796ff23a88563a12ae808cdc057ae2ef508999426b36a4985fef6dc008431f1aa38f0'),
    ('0.28.1', '', '3.1/3.1.5/sources/vte-0.28.1.tar.xz', 'f76d5d10da069ee2a6235abc5a7db883dd2f582a58b935e8cd8150b4af8215db3bfddef103485a07c0d23608e5eba8e462d73e177d2a61a7bd97a69dd3cbf2af'),
    ('0.30.0', '2_90', '3.2/3.2.0/sources/vte-0.30.0.tar.xz', 'bcd35227100f326b5260db31239537f19604ce2ac7f735c4d39485640fd4f5c18bbc2298ccefcca657b8707e51e1028e145d0f367b67102ee89ddf2a6a7b914d'),
    ('0.30.1', '2_90', '3.2/3.2.2/sources/vte-0.30.1.tar.xz', 'b7e601f207fe87c56826b093904a27f90e51e8992707d5978ec058fb91c1c790287af8bc2594b8149f4a69223cff2f2c73bf13a43507f4ac37df7c3faee69e60'),
    ('0.32.0', '2_90', '3.4/3.4.0/sources/vte-0.32.0.tar.xz', '729e1dd7261fd0394a7a4a566b2076c49ae9f90505c701e663cbcd6833891a20b9a2120b4334694aaa2757312e7f973488bde6c02b3d2681eb4e116fc2842ee0'),
    ('0.32.1', '2_90', '3.4/3.4.1/sources/vte-0.32.1.tar.xz', '8c4d63f33ba99e8c39ee5fe6b0998dd89aa7415d35765cee4c42116e7cdb8aabc958471b68cc88a35c937949a9043678ce4ae74541476b36d5617491e8da6224'),
    ('0.32.2', '2_90', '3.5/3.5.5/sources/vte-0.32.2.tar.xz', '0346a3a85de8bfc84fce37f073154ee7af746b8872e7970f4f58e11cf261311def714100370c2eb371beecba5d22207dfdada7b0df7fee00f32035e93b9e8808'),
    ('0.34.0', '2_90', '3.6/3.6.0/sources/vte-0.34.0.tar.xz', '80c2f1c6b310324c05fe1c2373583280a7c32950ce4601151a9e81f24bf0636260ec2f02979437c99e5e9f916301ea694f2d40083f974fe92b8624618c2c0a73'),
    ('0.34.1', '2_90', '3.6/3.6.1/sources/vte-0.34.1.tar.xz', 'a80f74a9699c2c06b4bf269adf16298724c07d749fffc1c1dd7f3f5a89d3bb08f4d3db3aa888dbc3dea4be75846eb5ab6c794e661cc5c192fca9235aff293cbb'),
    ('0.34.2', '2_90', '3.6/3.6.2/sources/vte-0.34.2.tar.xz', '4a89f149e9c101ed31b76086de1a05287d9c2a750ee098792fa9508b8712fa065a63e60d50cfb4a060991c2f6f182ddb91d3f21d4c7baf61337f08dc1a960a35'),
    ('0.34.3', '2_90', '3.8/3.8.0/sources/vte-0.34.3.tar.xz', '6eecde8d4f03eabd5710850b4f559d1f55ab98a201b6611428025579a6d43d52faa80d6f6607a6b93e42b5efda597f2b8507312113b939574ff7b73a3bd134ef'),
    ('0.34.4', '2_90', '3.8/3.8.1/sources/vte-0.34.4.tar.xz', '2f1dce6ed47835b098c37351fa665ddbfd8719a4275672925d8030655cd96412ec7f3edc23e9d94a3e035a36969c74c5186d1689dcf1e1111071158e64d2360f'),
    ('0.34.5', '2_90', '3.8/3.8.2/sources/vte-0.34.5.tar.xz', 'bf49cffe9f5bf243aada353adda1d8f86d75883bed343792a16d69d8956e9fc6f846cd1c317c7b2b03ba446de9c645cba52384190d5343f5d000a4557b40fb53'),
    ('0.34.6', '2_90', '3.9/3.9.3/sources/vte-0.34.6.tar.xz', '185703bdb8d4d46c1f340af8daa41194fcd28fdffafc77f190e776350f4bd875000e94b6cc481da19cb1f8da26ae2d757f4a29b703833e71fa20fcc5ccb329fd'),
    ('0.34.7', '2_90', '3.9/3.9.5/sources/vte-0.34.7.tar.xz', 'a122814f7fee4202c0bc4862798c98b078e5b185eb8c3c11959001b33bd5e029579f7337f85bdffb3f8a7b22af3a6763a2353ecff16a8e5c8b941431adabc5e0'),
    ('0.34.8', '2_90', '3.10/3.10.0/sources/vte-0.34.8.tar.xz', 'e4a7b691d0affcb05c463e0eeeab42591e13679f8b8cd042869b2b91aaa82c24222734f68767e3246f2554f8fca481b35383239ecfdb39e5865fc9b8b3b8479b'),
    ('0.34.9', '2_90', '3.10/3.10.2/sources/vte-0.34.9.tar.xz', '57fff7d5916bcd8a8a13e3cf050f85ed78e9154fdf2510a6d6f594f938c6d56f512089c6bc3e06c9123d35d17f2eb3b3814a5407635027ec0116c25f73034688'),
    ('0.36.0', '2_90', '3.12/3.12.1/sources/vte-0.36.0.tar.xz', '7666fdb2d3458390b154add7da781cb973498b019d859a3396797102dc4840d9bdbae44c83257a3c67609e658173dc0d5ff382b0343a5bf3c6db43e04392893c'),
    ('0.36.2', '2_90', '3.12/3.12.2/sources/vte-0.36.2.tar.xz', 'fafd368b95918024e6324c81f4fa6c35ad15138ad44af2f92164492d9773b127202d11824c9def4a26e17de44336f42e9c8906330dd300795c280ca068381632'),
    ('0.38.0', '-2.91', '3.14/3.14.0/sources/vte-0.38.0.tar.xz', '624d8c9e7d4429c21830d4bdbd325d3b9a75e35ecad0494fe6051ae339745c59ab656af4989d632e638402bc1fedf4c4f69387d39bf731bd6eabaccf682b1bc0'),
    ('0.38.1', '-2.91', '3.15/3.15.1/sources/vte-0.38.1.tar.xz', 'd6e616d2f327ac6c28ad9ac11f0e7a081a5659b9ad90dd3246fa4240a8642ed1ffe87502ab4307527e03789195103cc33d3f783f2d89e7c866c0cc8d5cd0e24c'),
    ('0.38.2', '-2.91', '3.14/3.14.2/sources/vte-0.38.2.tar.xz', '4c493e18cca4b50d66640d282d7d33a471d1ac4bd2dd929b059b829a42fed852d202669751b266adf7291502203e26c513b6852b3035458d41a433b900b0c6bb'),
    ('0.40.0', '-2.91', '3.16/3.16.1/sources/vte-0.40.0.tar.xz', 'f7ff28cdefc80e7fa5d876b8cba5d396fd98aa13c21a6cd320ac4042a8747e67ebf7a7c13ddab7bebb6b839231aebcc4fc25be9f0cc6c55859886c7948d4ac79'),
    ('0.40.2', '-2.91', '3.16/3.16.2/sources/vte-0.40.2.tar.xz', '06d1c9a34e8e82e1bd54810d245d908ebb837538ba19fbaabe683cdf3b96b7cb1630516ddeabf18b0294922b8d98d2b9a2f5028c171fac2ad913974d94555eb2'),
    ('0.42.0', '-2.91', '3.18/3.18.0/sources/vte-0.42.0.tar.xz', 'e2b2c00c81af05cdd5d99fd2de4fcb9019cffc5bd8b59878b7676cf7104c79a0c095b28d9a62586e3a531e00b80ba70062352ca1d4e96a902fef8d8f1121df49'),
    ('0.42.1', '-2.91', '3.18/3.18.1/sources/vte-0.42.1.tar.xz', '4cf917d3f343973dcb816a341276bfab7784a9f4dc6f8fb402193e9a9062503ac192ccc274fe92bb20a17ac182d21fd2268bf9c1ddea817f730db5612e3b21c0'),
    ('0.43.0', '-2.91', '3.18/3.18.2/sources/vte-0.43.0.tar.xz', 'fabe336996fd49ac08fc347f87e2b6169a875bff5570c3e0276271e0efcb215d206c6663d961ae604ee23ea668cbcacdc0664c06ec626e0a5ee7120cc57417fc'),
    ('0.44.0', '-2.91', '3.20/3.20.0/sources/vte-0.44.0.tar.xz', 'c190ba6cd4785fc16b1982517a0fcfe2935e50082acec095bdb5d56467b4952fdd48340776c2a4ecef4da847a668a56bca4599801b00f5090927a0e5f31d2c3a'),
    ('0.44.1', '-2.91', '3.20/3.20.1/sources/vte-0.44.1.tar.xz', '1fd352ea111cc13f8e7b2acae374e2fbd9d5025f6cb28b193164024594a5df12c9418bcdff11ff3247a9b785d6584c484a242c22df6a98afc3f0dfa1f716499c'),
    ('0.44.2', '-2.91', '3.20/3.20.2/sources/vte-0.44.2.tar.xz', '98db3c1528d5f458164e2d30056cd816e5943d9c569551878119e79d4fbca1865e52667393bf298f32fd54710d1b268a5aac125222ecb29ce854522be3776356'),
    ('0.46.0', '-2.91', '3.22/3.22.1/sources/vte-0.46.0.tar.xz', '543cdba5c51c5384e54fc372924c2667ded952cbc8ffafb7ff62f8643c6a7e2440439109eb12378ed70b0e0a256d3ef97d6da004dd8088d36bccdd7fa16593f9'),
    ('0.46.1', '-2.91', '3.22/3.22.2/sources/vte-0.46.1.tar.xz', '04b3f8ce922c4326d92bef605a0dbe195764946cd5f1acf28fd6d69c0cdb2ee661cc7e424436c72380da5d0250790ae658ac49d761b567dea88d92157285889d'),
    ('0.47.90', '-2.91', '3.24/3.24.0/sources/vte-0.47.90.tar.xz', 'c36310486b0575b26330879d2ca222ce4ca36af7659ec13113b209a897371da7ce0ff758f2c0fc5a9d42b7fd60caae8603aa564a2a5f58159979e4a9388a688b'),
    ('0.48.2', '-2.91', '3.24/3.24.1/sources/vte-0.48.2.tar.xz', 'cbb2835618c554d72a790e16f1ac5b3c06a8a810d8d517c475ed7ca46eeb56d7c9f9226918e13c5c84c04ce1ccb5467e62af7c4453f317a0aad197a4c179d76a'),
    ('0.48.3', '-2.91', '3.24/3.24.2/sources/vte-0.48.3.tar.xz', '3037b61a759cfcf56838bc7804df5a211da416bff9ddc5791f8a8d5157b90926985cfe57d7edbab42de64945d5e668470fe4129a218fb9c7af546648e1660c72'),
    ('0.50.0', '-2.91', '3.26/3.26.0/sources/vte-0.50.0.tar.xz', 'ac05622ecf92115cf6aef1ef7805b0ef19856d65d2dfc9792b149443aeee4c9bbfb871c600c9be8b0f4baac4a143e70412208d0a510cb53f13b2caf2caa33587'),
    ('0.50.1', '-2.91', '3.27/3.27.1/sources/vte-0.50.1.tar.xz', 'd5e9c7990ddb6ee789d4f4f8df05c23d794791e8381266551cf6574658ee8fd6adc4c7b9ac6aadcf957887b0ba13f7f89002fd820c8d35c789bba918414bd330'),
    ('0.50.2', '-2.91', '3.27/3.27.3/sources/vte-0.50.2.tar.xz', 'a1b12c74bedb167bf2a470294c566198c224c90be9b5c50366ef18d9542921f6cb2dc2329afd82f7342279c3eebd4ef5dfd753b4feb9d4e3e194cb878b48a7a2'),
    ('0.52.0', '-2.91', '3.28/3.28.0/sources/vte-0.52.0.tar.xz', '2f8b1efc7c73c4e74070d3bfcb33e61672d6ed70a352eed2c43198f8c3ffb513f6ed98dcf822dbd55d31d914c7f9dc157b29f8e4781705ee2c9ddb0e43c6e5fa'),
    ('0.52.1', '-2.91', '3.29/3.29.1/sources/vte-0.52.1.tar.xz', 'a1de54950cdcac9afccc1b13bd71b65ad1d6f93055d0b005b4a15b6f84f55029848cf8f2f9155cf3e6edc69fe973529fd4313f59af74fc1035aebd4c0b85655f'),
    ('0.54.0', '-2.91', '3.30/3.30.0/sources/vte-0.54.0.tar.xz', '69dd0caae4eacc179f84eccf98625a31140286beca4244a8f06420bd36ac62dcaddf9e9d8b114549ca97927e94b562df3e7daa9fad971484f05ebdd1c0f7b787'),
    ('0.54.1', '-2.91', '3.30/3.30.1/sources/vte-0.54.1.tar.xz', '5cb866e75c35e1b5728d17b0433641ceb4837495d59185a04fde9dd8c9849ab905a6b2718a50b27cc70323c7a6c5db31a808816576c30d7f18ece889a329fb61'),
    ('0.54.2', '-2.91', '3.30/3.30.2/sources/vte-0.54.2.tar.xz', '214ec69110d6ad6caa9bc41fb741874bfcf27f20f34d3ae745b13903c574f9c854f7e0dadbae3dbc8ce04c5a6eb818a433c50569c1ef802501a9a078385f23fc'),
    ('0.55.0', '-2.91', '3.31/3.31.2/sources/vte-0.55.0.tar.xz', '972bb4e616bc9436482dc938c31dcf62e8e00eba375554e4049485fbd1dc2f31f657fc6cd83777788781decb3b50559ee982684c8c50a139743e239dbfe078b1'),
    ('0.56.0', '-2.91', '3.32/3.32.0/sources/vte-0.56.0.tar.xz', 'f366ed4a28a896ba919184b50a55ee110eae43127847f34c049684bcb9b81327d1b72e9d871b2a5b7f7fa12f3f4aa721ac3d770770b600dca9c433cb2c674915'),
    ('0.56.3', '-2.91', '3.32/3.32.2/sources/vte-0.56.3.tar.xz', 'f78b3d532ca47e53c1bb51db6780697ce4692d493c0030d2dc4beb63a2595e44a43eb409ee31b94e4551eae259ac1baa8f06825a02fd66df8352e192f4ea1988'),
    ('0.57.0', '-2.91', '3.33/3.33.2/sources/vte-0.57.0.tar.xz', '87788ed44b39d57cf6d0ff99046ab575c8a410a0713e8f7404ada1239a1691f687b689a0b692f1bfe84ba7c38308382da409bab0780b1168d0ba99bbc0eb7b4f'),
    ('0.57.3', '-2.91', '3.33/3.33.4/sources/vte-0.57.3.tar.xz', 'f5496fd2b24af8d8eb895adaea59ee5ed4250c12a97745e025aacebca2d709901ae84befca58a3c5f1a54014a97af460ea53f844b1b1b9e32e192cc5883ecfed'),
    ('0.58.0', '-2.91', '3.34/3.34.0/sources/vte-0.58.0.tar.xz', '4d0fc725e0c71921b3d235d434600ad3c0807d5c0e7bd62fb782d857254db334bb851b75382c9613a5af753b5d6a1c05b174731427a8560b9b14101b3cc38c06'),
    ('0.58.1', '-2.91', '3.34/3.34.1/sources/vte-0.58.1.tar.xz', '1f795731fbb7ee76c4274562d5a55668c3b8ecad5a00ff83c762b0a2517ccffb85e796e937407d46e6bdb64327759eabc5878455d1d66cb1b8ff8b6060a4b1b7'),
    ('0.59.9', '-2.91', '3.35/3.35.1/sources/vte-0.59.0.tar.xz', '533d1e87a699137a33a6ddb82bf0f010925ba578974e1f6c87bae0b497309dd84c3cb2f5f6884f34f7fbcfad94fbaa07eb3a80387ee9f16b5f3f0ea2679e7376'),
)


for vte_version, vte_api, vte_file, vte_sha in vte_versions:
    vte_version_b = vte_version.replace('.', '_')
    vte_runtime = '3.30'
    if vte_api == '':
        vte_runtime = '3.28'
    with open('de.uchuujin.fp.termzoo.vte{}.json'.format(vte_version_b), "w") as f:
        f.write(VTE_TEMPLATE.substitute(vte_version=vte_version, vte_api=vte_api, vte_runtime=vte_runtime,
                  vte_version_b=vte_version_b, vte_file=vte_file, vte_sha=vte_sha))


