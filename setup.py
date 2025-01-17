# DexYCB Toolkit
# Copyright (C) 2021 NVIDIA Corporation
# Licensed under the GNU General Public License v3.0 [see LICENSE for details]

from setuptools import setup

setup(
    name='dex-ycb-toolkit',
    version='1.0',
    install_requires=[
        'chumpy',
        'numpy',
        'matplotlib',
        'open3d',
        'opencv-python',
        'pycocotools',
        'pyglet',
        'pyrender',
        'python-fcl',
        'pyyaml',
        'scikit-image',
        'tabulate',
        'torch',
    ],
)
