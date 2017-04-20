{
  "variables": {
      # may be redefined in command line on configuration stage
      "BUILD_LIBRDKAFKA%": "<!(echo ${BUILD_LIBRDKAFKA:-1})",
      "WITH_SASL%": "<!(echo ${WITH_SASL:-1})",
      "WITH_LZ4%": "<!(echo ${WITH_LZ4:-0})"
  },
  "targets": [
    {
      "target_name": "node-librdkafka",
      "sources": [ "<!@(ls -1 src/*.cc)", ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "<(module_root_dir)/"
      ],
      'conditions': [
        [ "<(BUILD_LIBRDKAFKA)==1",
            {
                "dependencies": [
                    "<(module_root_dir)/deps/librdkafka.gyp:librdkafka_cpp"
                ],
                "include_dirs": [ "deps/librdkafka/src-cpp" ],
            },
            # Else link against globally installed rdkafka and use
            # globally installed headers.  On Debian, you should
            # install the librdkafka1, librdkafka++1, and librdkafka-dev
            # .deb packages.
            {
                "libraries": ["-lrdkafka", "-lrdkafka++"],
                "include_dirs": [
                    "/usr/include/librdkafka",
                    "/usr/local/include/librdkafka"
                ],
            },
        ],
        [
          'OS=="linux"',
          {
            'cflags_cc' : [
              '-std=c++11'
            ],
            'cflags_cc!': [
              '-fno-rtti'
            ]
          }
        ],
        [
          'OS=="win"',
          {
            'cflags_cc' : [
              '-std=c++11'
            ]
          }
        ],
        [
          'OS=="mac"',
          {
            'xcode_settings': {
              'MACOSX_DEPLOYMENT_TARGET': '10.11',
              'GCC_ENABLE_CPP_RTTI': 'YES',
              'OTHER_CPLUSPLUSFLAGS': [
                '-std=c++11'
              ],
            },
          }
<<<<<<< HEAD
=======
        ],
        [ "<(WITH_SASL)==1",
          {
            'libraries' : ['-lsasl2'],
            'conditions': [
              [ 'OS=="mac"',
                {
                  'xcode_settings': {
                    'libraries' : ['-lsasl2']
                  }
                }
              ],
            ]
          }
        ],
        [ "<(WITH_LZ4)==1",
          {
            'libraries' : ['-llz4'],
            'conditions': [
              [ 'OS=="mac"',
                {
                  'xcode_settings': {
                    'libraries' : ['-llz4']
                  }
                }
              ],
            ]
          }
>>>>>>> 41e613cf5c659f960a7359f18b61982b4c13aa92
        ]
      ]
    }
  ]
}
