#! /usr/bin/env python3

from string import Template

ALACRITTY_TEMPLATE = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.alacritty${alacritty_version_b}",
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
                    "url": "https://github.com/jwilm/alacritty/releases/download/v${alacritty_version}/Alacritty-v${alacritty_version}${alacritty_filename}.tar.gz",
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

ALACRITTY_TEMPLATE2 = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.alacritty${alacritty_version_b}",
    "runtime": "org.freedesktop.Platform",
    "runtime-version": "24.08",
    "sdk": "org.freedesktop.Sdk",
    "sdk-extensions": [
        "org.freedesktop.Sdk.Extension.rust-stable"
    ],
    "command": "alacritty",
    "finish-args": [
        "--share=ipc",
        "--socket=fallback-x11",
        "--socket=wayland",
        "--device=dri",
        "--talk-name=org.freedesktop.Flatpak"
    ],
    "build-options": {
        "append-path": "/usr/lib/sdk/rust-stable/bin"
    },
    "modules": [
        {
            "name": "alacritty",
            "buildsystem": "simple",
            "build-options": {
                "env": {
                    "CARGO_HOME": "/run/build/alacritty/cargo"
                }
            },
            "build-commands": [
                "cargo --offline fetch --manifest-path Cargo.toml --verbose",
                "cargo --offline build --release --verbose",
                "install -Dm755 ./target/release/alacritty -t /app/bin/"
            ],
            "sources": [
                {
                    "type": "archive",
                    "url": "https://github.com/alacritty/alacritty/archive/refs/tags/v${alacritty_version}.tar.gz",
                    "sha256": "${alacritty_sha}"
                },
                "generated-sources-${alacritty_version}.json"
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
    ('0.2.9', '-x86_64', '5c646eb3577f10449c33d91b31eae59f3c773fad4eac6dc62c2fe6af4d7f3cdbc1572fba3e0799331ec1e51e31fd585c0dfce4b69872cde24140581c1da005b1'),
    ('0.3.0', '-ubuntu_18_04-x86_64', 'bd30db68453e319ee723c91bd4cba19297f77ca8c8affd8b7f17a5b34f2ad3ea650787b67cb5df2c84d4e642220772ba04e0f43f5f9eafa020a5d6aac89e4fa2'),
    ('0.3.1', '-ubuntu_18_04-x86_64', '6ee7aadce1296d7994a2982e17f880343c552a73333d734b9953e1e3bbf85e1d70b41dce61f9ef5dadeeb29ab9f1d0bb8ca084ac3a7463f7f69b328095b572ee'),
    ('0.3.2', '-ubuntu_18_04-x86_64', '256b174a418da25eee006f25e1405938abf142ef733abe09d748fbc1c4e8ea9405be16a016b16f6ef2b8a8b86fd7fb5196bd4aa81acc67154449b3a296ce8c27'),
    ('0.3.3', '-ubuntu_18_04_amd64', 'f1e2438e19110383c25533aed6a957c818745edf56307fc3dc00e3d0f71f0f04d025f73ef7606da34a0f39a4072a7cd084a16d3aab5b12f488561c03937b073b'),
    ('0.4.0', '-ubuntu_18_04_amd64', 'ddf5e5cbf483edba276319ad7fbe66f77db0f961792d65884be5bbf2adffcde39ea67988c34fb29502021333edc4814398c9525557dc310942200aa8b62312a0'),
    ('0.4.1', '-ubuntu_18_04_amd64', '547ffe6e25cb53ef4fba20e52aab805c799df831598e621ccbfcb9c813d12ae461784989220baecf722fed24d10011d10a78533e596408a84621c5a863d61cbf'),
    ('0.4.2', '-ubuntu_18_04_amd64', '9039901c3c17a59f38da23393364e9b660583150efb0d647c903b6a1659950e02b2caa3beff6f4801513180ef8d2385c49999d9f82aec32c968db478b47dd0dd'),
    ('0.4.3', '-ubuntu_18_04_amd64', '79b19e3ec0fc0fe8540f40d5c169c65c4e9827aa335865c4ddc88fb88321d9da94f677c82782d6d095fe8f58ec893ed781de6f42a78b6ca518ef0c3c6f245edd'),
)

alacritty_versions2 = (
    ('0.5.0', '9bc0e6ff9a0772ea522d7e34ab8371faa96e6cc4e588459966585f0dbb848dcb'),
    ('0.6.0', 'c794125a900a6477f1b40168dc9d22674a5326f32e4b083d6f1a45486d2505bf'),
    ('0.7.0', 'b9b7e96ebc1725962de628dac7d7bc0766ff9aea5f4c09f399e95823369d5882'),
    ('0.7.2', '750c294d384d23f1dfc30e9105380e4194507b0828ac91d8ffd94c9bbc18d6c3'),
    ('0.8.0', 'e450ff4ceafdf4894d82f2f22ca93b422ffd1283f876d44cf744e4ed3bc0eaf6'),
    ('0.9.0', '6d3aaac9e0477f903563b6fb26e089118407cdbfe952a1e2ffbf4e971b7062b3'),
    ('0.10.0', '5dee9c94f944b742b0189dd87c43c87175ffadde8049abb4668ca5a3e68fd65a'),
    ('0.10.1', 'e48d4b10762c2707bb17fd8f89bd98f0dcccc450d223cade706fdd9cfaefb308'),
    ('0.11.0', '0fb3370c662f5b87d1b9a487aef999195212b192e08f6f68a572fed8fd637e07'),
    ('0.12.0', '4cbf282da46c7e0f53ad552204f508904051baa324c771a0953c38484ab2359f'),
    ('0.12.3', '7825639d971e561b2ea3cc41e30b57cde8e185a400fee001843bb634df6b28ab'),
    ('0.13.0', '1c1cebf20e10bb26dc8bc735bb2d02eb88df89180d6c59f5d946a0a1d3d585b2'),
    ('0.13.1', '38a42e23e1e6faaa9e300347df3f7b58b6182908a701517aac6e296fbdf37451'),
    ('0.13.2', 'e9a54aabc92bbdc25ab1659c2e5a1e9b76f27d101342c8219cc98a730fd46d90'),
    ('0.14.0', '2919767177c010339502085b4ac5d3f9f15ca27e6befc39aa9d20fefb93ebcdf'),
    ('0.15.0', 'aa4479c99547c0b6860760b5b704865f629ffe1f1ec374153c2cd84e53ce5412'),
)


for alacritty_version, alacritty_filename, alacritty_sha in alacritty_versions:
    alacritty_version_b = alacritty_version.replace('.', '_')
    with open('de.uchuujin.fp.termzoo.alacritty{}.json'.format(alacritty_version_b), "w") as f:
        f.write(ALACRITTY_TEMPLATE.substitute(alacritty_version=alacritty_version, alacritty_filename=alacritty_filename, alacritty_version_b=alacritty_version_b,
                    alacritty_sha=alacritty_sha))


for alacritty_version, alacritty_sha in alacritty_versions2:
    alacritty_version_b = alacritty_version.replace('.', '_')
    with open('de.uchuujin.fp.termzoo.alacritty{}.json'.format(alacritty_version_b), "w") as f:
        f.write(ALACRITTY_TEMPLATE2.substitute(alacritty_version=alacritty_version, alacritty_version_b=alacritty_version_b,
                    alacritty_sha=alacritty_sha))

