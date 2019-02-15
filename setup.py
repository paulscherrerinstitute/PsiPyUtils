import setuptools
import shutil
import os
from setuptools.command.sdist import sdist


#Cleanup before sdist
class CustomSdist(sdist):
    def run(self):
        #Cleanup before building
        shutil.rmtree("dist", ignore_errors=True)
        shutil.rmtree("PsiPyUtils.egg-info", ignore_errors=True)

        #Build from directory above
        sdist.run(self)

#Package
setuptools.setup(
    name="PsiPyUtils",
    version="3.0.0",
    author="Oliver Bründler",
    author_email="oliver.bruendler@psi.ch",
    description="Python Utility Library",
    license="PSI HDL Library License, Version 1.0",
    url="https://github.com/paulscherrerinstitute/PsiPyUtils",
    package_dir = {"PsiPyUtils" : "."},
    packages = ["PsiPyUtils"],
    install_requires = [
        "lxml"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    cmdclass = {
        "sdist" : CustomSdist
    }
)