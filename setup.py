from __future__ import annotations

from   Cython.Build             import cythonize
import glob
from   setuptools               import Extension, find_packages, setup

package_name = "pytemplate"
package_dir = f"./src/python"
pyx_files = glob.glob("**/*.pyx", recursive=True)

# 合并 .pyx 和 .pxd 文件
ext_modules = [
    Extension(name=file.replace("/", ".").replace("\\", ".").replace(".pyx", ""), sources=[file], language="c++")
    for file in pyx_files
]

setup(
    name=package_name,
    version="0.0.1",
    description="Python Template",
    author="Panda Pan",
    author_email="panchongdan@gmail.com",
    packages=find_packages(where=package_dir),
    py_modules=[package_name],
    package_dir={package_name: f"{package_dir}/{package_name}"},
    package_data={package_name: ["lib/*.so"]},
    install_requires=["pandas>=1.4.0", "Cython"],  # some install requires example
    tests_require=[
        "pytest>=3.3.1",
        "pytest-cov>=2.5.1",
        "pytest-sugar>=1.0.0",
    ],
    extras_require=dict(dev=["pytest>=8.0", "pytest-cov>=2.5.1", "pytest-sugar>=1.0.0"]),
    python_requires=">=3.11",
    ext_modules=cythonize(ext_modules, compiler_directives={"language_level": "3"}),
)
