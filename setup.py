from __future__ import annotations

from   setuptools               import find_packages, setup

package_name = "pcdpy"
package_dir = f"./src/python"

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
    install_requires=["pandas>=1.4.0"],  # some install requires example
    tests_require=[
        "pytest>=3.3.1",
        "pytest-cov>=2.5.1",
        "pytest-sugar>=1.0.0",
    ],
    python_requires=">=3.8",
)
