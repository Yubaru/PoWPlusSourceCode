
# 0imports.rpy
# This file imports certain python modules at runtime for DDLC and template
# features.

python early:
    # For DSR/DSP, Effects
    import math 

    # For Credits
    import datetime

    # For Glitchtext
    import random

    # For Splash
    import re
    import os

    # For BSOD
    import subprocess
    import platform

init -1 python:
    # Achievements/Gallery
    # Note: Achievements are accessed via the achievements namespace (achievements.Achievement, etc.)
    # No import needed as the namespace is accessible directly from the store.
    
    try:
        from store.gallery import GalleryImage, galleryList
    except ModuleNotFoundError:
        pass
