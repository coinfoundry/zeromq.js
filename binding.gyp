{
  'variables': {
    'zmq_external%': 'true',
  },
  'targets': [
    {
      'target_name': 'zmq',
      'sources': ['binding.cc'],
      'include_dirs' : ["<!(node -e \"require('nan')\")"],
      'cflags!': ['-fno-exceptions'],
      'cflags_cc!': ['-fno-exceptions'],
      'conditions': [
        ["zmq_external == 'true'", {
          'link_settings': {
            'libraries': ['-lzmq'],
          },
        }, {
          'conditions': [
            ['OS=="win"', {
              'msbuild_toolset': 'v140',
              'defines': ['ZMQ_STATIC'],
              'include_dirs': ['windows/include'],
              'libraries': [
                '<(PRODUCT_DIR)/../../windows/lib/libzmq',
                'ws2_32.lib',
                'iphlpapi',
              ],
            }],
            ['OS=="mac" or OS=="solaris"', {
              'xcode_settings': {
                'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                'MACOSX_DEPLOYMENT_TARGET': '10.9',
              },
              'libraries': ['<(PRODUCT_DIR)/../../zmq/lib/libzmq.a'],
              'include_dirs': ['<(PRODUCT_DIR)/../../zmq/include'],
            }],
            ['OS=="openbsd" or OS=="freebsd"', {
             'include_dirs': [
               '<!@(pkg-config libzmq --cflags-only-I | sed s/-I//g)',
                '/usr/local/include'],
              'libraries': [
                '<!@(pkg-config libzmq --libs)',
                '-L/usr/local/lib']
            }],     
            ['OS=="linux"', {
              'libraries': ['<(PRODUCT_DIR)/../../zmq/lib/libzmq.a'],
              'include_dirs': ['<(PRODUCT_DIR)/../../zmq/include'],
            }],
          ],
        }],
      ],
    }
  ]
}
