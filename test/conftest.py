import sys
from dataclasses import dataclass

sys.path.append("src")


@dataclass
class Window:
    innerWidth: int = 0


browser = type(sys)("browser")
browser.ajax = lambda x: x
browser.window = Window()
sys.modules["browser"] = browser

javascript = type(sys)("javascript")
sys.modules["javascript"] = javascript
