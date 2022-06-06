# flame
import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from FlameSpam.utils import load_plugins
import logging
from telethon import events
from . import Flame, Flame2, Flame3, Flame4, Flame5, Flame6, Flame7, Flame8, Flame9, Flame10

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
    Flame.run_until_disconnected()
    
if __name__ == "__main__":
    Flame2.run_until_disconnected()

if __name__ == "__main__":
    Flame3.run_until_disconnected()
    
if __name__ == "__main__":
    Flame4.run_until_disconnected()

if __name__ == "__main__":
    Flame5.run_until_disconnected()
    
if __name__ == "__main__":
    Flame6.run_until_disconnected()
    
if __name__ == "__main__":
    Flame7.run_until_disconnected()

if __name__ == "__main__":
    Flame8.run_until_disconnected()
    
if __name__ == "__main__":
    Flame9.run_until_disconnected()

if __name__ == "__main__":
    Flame10.run_until_disconnected()    
