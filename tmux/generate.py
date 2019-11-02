#! /usr/bin/env python3

from string import Template

TMUX_TEMPLATE = Template(r"""
{
    "app-id": "de.uchuujin.fp.termzoo.tmux${tmux_version_b}",
    "runtime": "org.freedesktop.Platform",
    "runtime-version": "18.08",
    "sdk": "org.freedesktop.Sdk",
    "command": "tmux",
    "finish-args": ["--socket=x11", "--device=dri", "--talk-name=org.freedesktop.Flatpak"],
    "modules": [
        {
            "name": "libevent",
            "buildsystem": "autotools",
            "sources": [
                {
                    "type": "archive",
                    "url": "https://github.com/libevent/libevent/releases/download/release-2.1.8-stable/libevent-2.1.8-stable.tar.gz",
                    "sha512": "a2fd3dd111e73634e4aeb1b29d06e420b15c024d7b47778883b5f8a4ff320b5057a8164c6d50b53bd196c79d572ce2639fe6265e03a93304b09c22b41e4c2a17"
                }
            ]
        },
        {
            "name": "tmux",
            "buildsystem": "autotools",
            "build-options": {
                "ldflags": "-Wl,--copy-dt-needed-entries -L/app/lib"
            },
            "make-install-args": ["PREFIX=/app", "INSTALLBIN= install -m 755", "INSTALLMAN= install -m 444"],
            "sources": [
                {
                    "type": "archive",
                    "url": "https://github.com/tmux/tmux/releases/download/${tmux_version}/tmux-${tmux_version}.tar.gz",
                    "sha512": "${tmux_sha}"
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


tmux_versions = (
#    ('0.8', '52168ce7cafa9dae5b2eeb31a0978da18af7f52f5cef1001ca805d966c31632cb5d412ac2756fc5f87737d1c3624b1a4cb34c54a2416f0f4969b54cb841a05a6'),
#     ^^^^^ has no configure script
    ('0.9', 'bc83d64221ed4e37d1859eca33877a26a40e8561adb01cc453d4cee624248ab76931285893b51bb26495768cb76175902d6657e22d2f00e698a950627a5f94c6'),
    ('1.0', '4ec166da4670a75b7fab63d5d028008d44c69c42e99f14aa955cac990da19edf57a1d3ba077771aaafc92e2f38f461506ed74b59d344d9db88f009c7d20b7e04'),
    ('1.1', 'b4139bb22a71c5df9fe6d0352b1067c85e78ca0478cdc4095fb07ee1d954fc955f626f8bd2eceb09f9427eefbbbeafa09078242d8e1fc9d4102cdf4dc231a068'),
    ('1.2', '29c4e2828f4c99490d0ba502486768e4b110fc5a215f40288c253d7d75539b47d7a1f9f870fe1607a4b25ed2d45a68ad8cead93017b99ef131b087265c463001'),
    ('1.3', '306fae6239b32a9b0e18329608b18d1170aa81802aee383d1bf88007fbb3a53fc8764e344b8cf5f7e02042db2b37c98a299ded02fef7ba9fcdc7e2ec8b63393d'),
    ('1.4', '75c71da11711a0fed76ff3ebdc109ec6c1474ec79d200cba51a38f1eb85ed903cb27f28a02e1366d83c96eb6e88391989bce835cf56720e9caffe0f2fda0b579'),
    ('1.5', 'a2004923d645f32e30d3e6ecee92a5cea71f831718bc09dec14c11a420848d175eff919f00b344ac65be1e2af00362c4b0ffc4e03851d5e3df2fa4c005069bd6'),
    ('1.6', '5c7b311d011f2f2027926a615d4300e97fd22f3ae32b0c364fdf935ff02124c59d1d0c48e7e9d572229c7600b6583fd679f4b960a5af872305f005d27350ad9c'),
    ('1.7', 'd2002858ab6c974e6a6c7dc31db20cd6271170cba9e7314216dfcea6670ae09c5112a4313b77bd21d14a906c89723fc9f6c20cea528e7320e2857ec4d71c725b'),
    ('1.8', '555c7cdc51bfbaa1c90fa0dc820e7ad89d8a4eb818e62d8ccf4637cc96e985ffd9c242b9ba092820c3fb96d09d65c46064ce361062e59ef2586b122e624bbbbb'),
    ('1.9', '47ccfefe8e8b1d6b1732e49888f0010b804990d5a79744cb5461afcb7d83157767d38208e45e0e8b3848d8b4ddea20c83a558214dc7c9dafccc090946a15b13e'),
    ('1.9a', '842984638dc1f7364c03393187379598f35679d535d911d5df4016944d6032e61a1bf840d7d339c6e99b30c55581d470acca85ab6ee5799b8927d18c0e9a91df'),
    ('2.0', '8a4be40ceb9b371a91107173de08348c4379b103454fa397ee326506f78a5fda1034dc7148c090c687221eddb8a2fc0c3aeb85da57841df6bcd74fb5f4f5f53d'),
    ('2.1', '0faa0a60a84b777ca3cf572cf741d0e4f82a9f32d27dfeddfda41bad57830823a6d5f2323f27ba794b86e194d9f7db7028c94dc6a15bb4ac5a18508f890bdaa4'),
    ('2.2', '4d4fc316c78aab0d13f7f15098d952f01d7da7d74d46251ae2dd90440522f07c785afe984d82de2b4518fb67ea441f5a5a46c357c87ddc6ddbfba4b7f08be7bf'),
    ('2.3', '521e3734104be43837cba95d8b3d050d033708fa7469f7e7db66ae6993b002c4d9f6bafec41f3c9446eda91a4499e571019534dfa2e5a0563085b2d16e1b94af'),
    ('2.4', 'e9d93f6b8b68dddf05046ef1e1bc8c55a1f2c4bb96f4e12c25c202358b3280b3e14df8818ed449aadc783306b0869e5e7418192f60bb16afebc6b396cb50999c'),
    ('2.5', 'c0e8365a553d034e347f2f7a0d64f04e2be4307a75a9f72c8218fc56b72e531f3f37fe4a8f0e8d70801f5f62ee250ab7e9978abd6d101d273f76b4a1a92b08e0'),
    ('2.6', '20a1ae8b8494c5b42757902322f3877731c2cc330c9c00f097a317785d25252b7ebaa8bbab9fc17843299e80cb2914aaac0a664715a85c50f7ea489d23753832'),
    ('2.7', '7839ef748ea55df8c02c727047f65bd235b5e3b8ab23157246071e1b9954fa269594da9fbd0fabf6a850e3b5dfda962a0a067c1507411c92a84d1db2666ecf37'),
    ('2.8', 'e382aec122a10624953432b3c869b21d69390bc2e7d459440a46950802e39503eafb398178f8085191261925e4f0872bb99b19e0403e7beb56d3ceecc4c86b09'),
    ('2.9', 'a712da19ebea240bafb3e8b0bf313baec6f2e6c6e32babac1221a0fbaaf4da82cd8cad4e6cf3da1e277ddc830b5405d104ca69b278627d3db5d0e4439d4896b3'),
    ('2.9a', 'aca6882688727c10c5647443fdd18bbd6c0f80b7a3bf9667903d1b89d523e604cd715f176f33f2e5673258f00e626a6dc273f80fe97ae4f91621814d89985713'),
)


for tmux_version, tmux_sha in tmux_versions:
    tmux_version_b = tmux_version.replace('.', '_')
    with open('de.uchuujin.fp.termzoo.tmux{}.json'.format(tmux_version_b), "w") as f:
        f.write(TMUX_TEMPLATE.substitute(tmux_version=tmux_version, tmux_version_b=tmux_version_b, tmux_sha=tmux_sha))


