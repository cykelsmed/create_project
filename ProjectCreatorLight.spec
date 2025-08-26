# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['run_gui_light.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'project_creator',
        'project_creator.config.simple_settings',
        'project_creator.templates',
        'project_creator.generators',
        'project_creator.utils',
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'tkinter.filedialog'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib', 'numpy', 'pandas', 'scipy', 'PIL', 'PyQt5', 'PyQt6', 'PySide2', 'PySide6',
        'IPython', 'jupyter', 'notebook', 'qtpy', 'wx', 'pytest', 'unittest', 'doctest',
        'email', 'html', 'http', 'urllib3', 'requests', 'urllib', 'xml', 'xmlrpc',
        'multiprocessing', 'concurrent', 'asyncio', 'threading', 'queue',
        'sqlite3', 'dbm', 'pickle', 'shelve', 'marshal',
        'distutils', 'setuptools', 'pkg_resources', 'pkg_resources._vendor',
        'pydoc', 'doctest', 'test', 'tests', 'testing',
        'tkinter.test', 'tkinter.tix', 'tkinter.ttk.test',
        'yaml', 'click', 'pyyaml'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ProjectCreatorLight',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,
    upx=True,
    upx_exclude=[],
    name='ProjectCreatorLight',
)

app = BUNDLE(
    coll,
    name='ProjectCreatorLight.app',
    icon='icon.icns',
    bundle_identifier='com.cykelsmed.projectcreator.light',
    info_plist={
        'CFBundleName': 'Project Creator Light',
        'CFBundleDisplayName': 'Project Creator Light',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleIdentifier': 'com.cykelsmed.projectcreator.light',
        'CFBundleExecutable': 'ProjectCreatorLight',
        'CFBundlePackageType': 'APPL',
        'CFBundleSignature': '????',
        'LSMinimumSystemVersion': '10.13.0',
        'NSHighResolutionCapable': True,
        'NSRequiresAquaSystemAppearance': False,
    },
)
