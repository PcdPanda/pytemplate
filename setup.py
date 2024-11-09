from __future__ import annotations

from   setuptools               import find_packages, setup

setup(
    name='pytemplate',
    version='0.0.1',
    description='Python Template',
    author='Panda Pan',
    author_email='panchongdan@gmail.com',
    packages=find_packages(),
    install_requires=['pandas>=1.4.0'],  # some install requires example
    tests_require=['pytest>=3.3.1', 'pytest-cov>=2.5.1'],
    python_requires='>=3.8',
)
