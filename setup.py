from distutils.core import setup
import os


# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk("strict_timeout"):
    # Ignore dirnames that start with "."
    for i, dirname in enumerate(dirnames):
        if dirname.startswith("."): del dirnames[i]

    if "__init__.py" in filenames:
        pkg = dirpath.replace(os.path.sep, ".")
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, ".")
        packages.append(pkg)

    if filenames:
        prefix = dirpath[15:] # Strip "strict_timeout/"
        for f in filenames:
            if f != "__init__.py":
                data_files.append(os.path.join(prefix, f))


setup(
    name="strict_timeout",
    version="1.0.0",
    package_dir={"strict_timeout": "strict_timeout"},
    packages=packages,
    package_data={"strict_timeout": data_files},
)
