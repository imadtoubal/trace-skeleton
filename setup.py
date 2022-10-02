#!/usr/bin/env python
import os
import sys

from setuptools import Extension, setup

# set the compiler flags so it'll build on different platforms (feel free
# to file a  pull request with a fix if it doesn't work on yours)
if sys.platform == 'darwin':
    # default to clang++ as this is most likely to have c++11 support on OSX
    if "CC" not in os.environ or os.environ["CC"] == "":
        os.environ["CC"] = "clang++"
        # we need to set the min os x version for clang to be okay with
        # letting us use c++11; also, we don't use dynamic_cast<>, so
        # we can compile without RTTI to avoid its overhead
        extra_args = ["-O3", "-stdlib=libc++",
          "-mmacosx-version-min=10.7","-fno-rtti",
          "-std=c++0x"]  # c++11
else: # only tested on travis ci linux servers
    os.environ["CC"] = "g++" # force compiling c as c++
    extra_args = ["-O3", '-std=c++0x','-fno-rtti']

_trace_skeleton = Extension(
  '_trace_skeleton',
  ['trace_skeleton.i', 'trace_skeleton.c'],
  extra_compile_args=extra_args,
)

setup(name='trace_skeleton',
      version='0.1.2',
      author="SWIG Docs",
      description="""Simple swig example from docs""",
      ext_modules=[_trace_skeleton],
      py_modules=["trace_skeleton"])
