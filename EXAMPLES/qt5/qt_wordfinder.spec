# -*- mode: python -*-

block_cipher = None


a = Analysis(['qt_wordfinder.py'],
             pathex=['/Users/jstrick/Documents/curr/courses/python/examples3/qt5'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='qt_wordfinder',
          debug=False,
          strip=False,
          upx=True,
          console=True )
