# flame
import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from FlameSpam.utils import load_plugins
import logging
from telethon import events
from . import FlameSpam, FlameSpam2, FlameSpam3, FlameSpam4, FlameSpam5, FlameSpam6, FlameSpam7, FlameSpam8, FlameSpam9, FlameSpam10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "FlameSpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Flame Bot Spam Successfully deployed -!")
print("Enjoy! Do visit @FlameSpam")

if __name__ == "__main__":
    FlameSpam.run_until_disconnected()
    
if __name__ == "__main__":
    FlameSpam2.run_until_disconnected()

if __name__ == "__main__":
    FlameSpam3.run_until_disconnected()
    
if __name__ == "__main__":
    FlameSpam4.run_until_disconnected()

if __name__ == "__main__":
    FlameSpam5.run_until_disconnected()
    
if __name__ == "__main__":
    FlameSpam6.run_until_disconnected()
    
if __name__ == "__main__":
    FlameSpam7.run_until_disconnected()

if __name__ == "__main__":
    FlameSpam8.run_until_disconnected()
    
if __name__ == "__main__":
    FlameSpam9.run_until_disconnected()

if __name__ == "__main__":
    FlameSpam10.run_until_disconnected()    
