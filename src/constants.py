import os
import pathlib

ROOT_DIR = pathlib.Path(os.path.dirname(os.path.abspath(__file__))).parent
SRC_DIR = ROOT_DIR / 'src'
TEMPLATE_DIR = ROOT_DIR / 'templates'
STATIC_DIR = ROOT_DIR / 'static'