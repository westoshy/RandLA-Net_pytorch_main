from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

# https://github.com/QingyongHu/RandLA-Net/issues/73

ext_modules = [Extension(
       "nearest_neighbors",
       sources=["knn.pyx", "knn_.cpp",],  # source file(s)
       include_dirs=["./", numpy.get_include()],
       language="c++", 
       extra_compile_args=['-std=c++11',
                           '-D_GLIBCXX_USE_CXX11_ABI=0']     
  )]

setup(
    name = "KNN NanoFLANN",
    ext_modules = ext_modules,
    cmdclass = {'build_ext': build_ext},
)
