from setuptools import setup, find_packages
from setuptools.extension import Extension
import numpy as np

USE_CYTHON = True
ext = '.pyx' if USE_CYTHON else '.c'

#sys.argv[1:] = ['build_ext', '--inplace']

ext_modules = [
    Extension("rlscore.learner._rls",["rlscore/learner/_rls"+ext]),
    Extension("rlscore.utilities._swapped",["rlscore/utilities/_swapped"+ext]),
    Extension("rlscore.learner._global_rankrls",["rlscore/learner/_global_rankrls"+ext]),
    Extension("rlscore.learner._two_step_rls",["rlscore/learner/_two_step_rls"+ext]),
    Extension("rlscore.learner._steepest_descent_mmc",["rlscore/learner/_steepest_descent_mmc"+ext]),
    Extension("rlscore.learner._interactive_rls_classifier",["rlscore/learner/_interactive_rls_classifier"+ext]),
    Extension("rlscore.learner._greedy_rls",["rlscore/learner/_greedy_rls"+ext]),
    Extension("rlscore.utilities._sampled_kronecker_products",["rlscore/utilities/_sampled_kronecker_products"+ext])
]

if USE_CYTHON:
    from Cython.Build import cythonize
    ext_modules = cythonize(ext_modules)

setup(
    name = 'konstan_testi',
    description = 'machine learning package',
    url = "https://github.com/konstanyman/RLScore",
    version = "0.8.14",
    license = "MIT",
    include_dirs = [np.get_include()],
    ext_modules = ext_modules,
    packages = find_packages()
    )


