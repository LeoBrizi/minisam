from distutils.core import setup
from setuptools import setup, find_packages

setup(name='minisam',
      version='0.0.0',
      packages=['minisam', 'minisam.sophus'],
      package_dir={'minisam': 'minisam',
                   'minisam.sophus': 'minisam/sophus'},
      package_data={'minisam': ['_minisam_py_wrapper*.so', 'libminisam*', 'minisam*'],
                    'minisam.sophus': ['*.so']},
      include_package_data=True,
      zip_safe=False,
)
