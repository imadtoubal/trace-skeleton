#!/usr/bin/env python

from setuptools import Extension, setup

example_module = Extension(
  '_trace_skeleton', sources=['trace_skeleton_wrap.cxx', 'src/trace_skeleton.c'])

setup(name='trace_skeleton',
      version='0.1',
      author="SWIG Docs",
      description="""Simple swig example from docs""",
      ext_modules=[example_module],
      py_modules=["example"])
