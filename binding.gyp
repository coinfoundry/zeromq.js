{
  'targets': [
    {
      'target_name': 'zmq',
      'sources': ['binding.cc'],
      'include_dirs' : ["<!(node -e \"require('nan')\")"],
      'cflags!': ['-fno-exceptions'],
      'cflags_cc!': ['-fno-exceptions'],
      'link_settings': {
        'libraries': ['-lzmq'],
      },
      'conditions': [
        ['OS=="win"', {
          'msbuild_toolset': 'v140',
          'defines': ['ZMQ_STATIC'],
          'include_dirs': ['windows/include'],
          'libraries': [
            'ws2_32.lib',
            'iphlpapi',
          ],
        }],
        ['OS=="mac" or OS=="solaris"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'MACOSX_DEPLOYMENT_TARGET': '10.9',
          }
        }],
        ['OS=="openbsd" or OS=="freebsd"', {
          'include_dirs': [
            '<!@(pkg-config libzmq --cflags-only-I | sed s/-I//g)',
            '/usr/local/include'],
          'libraries': [
            '<!@(pkg-config libzmq --libs)',
            '-L/usr/local/lib']
        }],
      ],
    }
  ]
}
