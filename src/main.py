"""
Start App
"""

from app import App
from config import Config
from logger import init_logger


if __name__ == "__main__":
    cfg = Config()

    init_logger(cfg.log_level)

    web_app = App(cfg)
    web_app.run()
