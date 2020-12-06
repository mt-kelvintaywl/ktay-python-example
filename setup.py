import setuptools

VERSION = "0.1.0"

PACKAGES = setuptools.find_packages(where="src")

setuptools.setup(
    name="ktay_python_example",
    version=VERSION,
    url="https://github.com/mt-kelvintaywl/ktay-python-example",
    author="Kelvin Tay",
    author_email="ktay@moneytree.jp",
    description="Example python package installable from GitHub",
    packages=PACKAGES,
    package_dir={"": "src"},
    python_requires=">=3.7",
)
