#! /usr/bin/env python3

from string import Template

SCREEN_TEMPLATE = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.screen${screen_version_b}",
    "runtime": "org.freedesktop.Platform",
    "runtime-version": "18.08",
    "sdk": "org.freedesktop.Sdk",
    "command": "screen",
    "finish-args": ["--socket=x11", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "screen",
            "buildsystem": "autotools",
            "build-options": {
                "ldflags": "-Wl,--copy-dt-needed-entries -L/app/lib"
            },
            "sources": [
                {
                    "type": "archive",
                    "url": "https://mirrors.kernel.org/gnu/screen/screen-${screen_version}.tar.gz",
                    "sha512": "${screen_sha}"
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


screen_versions = (
    ('3.9.15', '5b5654213bd7d63be9309801b63f7b7d90501c83fd9ac1c49bce9ec4203cc408170060c1f00839e3faeee994a2a8aa88911aee85230d0064ab8e05fc3cd192e4'),
    ('4.0.2', 'a003f2703659644a08436f8c3c8ca4000f35309f1615a2e7a1a1c774f88e9a6129c93a933debf9aa6b3265a177b67a1f4dc94dd10680ed34279c4c1d6255521e'),
    ('4.0.3', '24c1f598972f3dc9ed49cd2c05852190a0190d22fa01401eee8484627c8dd2815f0a422d9b2697faa8aaa0b3efc6730a94e2d5aa787dbe5e9ec719143176c338'),
    ('4.2.0', 'be9b04de668864c1e9ebabe76dc35be60ece15bda16d983d8fee0331ddbf6d732ca354a136cd602dda76baf155d8f324e1ef16cc10b4b13ee07c74d37af49350'),
    ('4.2.1', '30826b2a2fc436483276b90cc4c6679470f7ccb7098c9bb8457d0e534998cd12da02882cf80678465f6540cade170c3fdc6bdfa31b07359ff0d3ffe2d6063710'),
    ('4.3.0', '35997a2763be739bd74eaafbb22ede0ac909de7111281b2350b281c846fc04c777a75dd4eab2a63e00653285aaa7b0950f901bf2a03af7cf3c38e17c52964269'),
    ('4.3.1', '8e8a25b23330a7d8e00fc9e6cc430f0eb3937ccf4183efbd6fd24e4dc04cc09b3acae45bfc24892faee433b18fa79b1cfe0211fd75c0d74ecf908f916bf774aa'),
    ('4.4.0', '6e43f85c419f778822ec85e4340c95769e981a3d51abdeb5f26c6ebb840da9ab11b351ecc7f380ceea39bcfaa87f1124cfebd6af4ecb62b886eb189e7b79981b'),
    ('4.5.0', 'b2705ed9604355d4153d7902f820af6131a1f2387650f5c6efeda7acf543aad48e8603c26d7c6e74213c8eece994d5d9bb0d114bc19c8d8f3d8e99c00ea4a484'),
    ('4.5.1', 'ca53477ad38264be38efb1d10a1337b647dd061127162c77533b17a30d046cd0caabe38e4a9e5389aac30d5dc62eb53e7877411e69adae36d0ca869bd0a82804'),
    ('4.6.0', '2ee7cc51c62a478e72eda0647f3f347e63f40384e19bc11b074158bd94cdb628c6425b1dd7a472496d56bff11a30a9dc58859c2e7e539fae2a8718ed9b0f96d7'),
    ('4.6.1', 'e5d029400ed5b509ebddc1f55812c33536d6f5ce91119537c7d06e1fa7dee84939c43337df4638f61c818ce0412f4d08fe212202162a4483a9e84bbc4b3e4336'),
    ('4.6.2', '224bd16ad5ae501d1b8bb7d2ba9cc19e6a0743de5a5b320109c2f6bf3b1ca564cc7094ed9211be13733d9d769cde77d13fe236341d448cad0518038ab1e85c99'),
    ('4.7.0', '44c7a33e2ed772ce91998cdc07556ef7b972e5b100335e14702b273a234e437fe6415de459e7b6d34c6086282a432778629047424ef9159ac6fcf26d22b45745'),
    ('4.8.0', '770ebaf6ee9be711bcb8a6104b3294f2bf4523dae6683fdc5eac4b3aff7e511be2d922b6b2ad28ec241113c2e4fe0d80f9a482ae1658adc19c8c3a3680caa25c'),
)


for screen_version, screen_sha in screen_versions:
    screen_version_b = screen_version.replace('.', '_')
    with open('de.uchuujin.fp.termzoo.screen{}.json'.format(screen_version_b), "w") as f:
        f.write(SCREEN_TEMPLATE.substitute(screen_version=screen_version, screen_version_b=screen_version_b, screen_sha=screen_sha))


