obj = trace_skeleton_wrap.cxx _trace_skeleton.so

.PHONY: all
all : $(obj)

clean:
	rm -f *.o
	rm -f *.so
	rm -f *wrap*.c*
	rm -Rf build
	rm -f trace_skeleton.py

trace_skeleton_wrap.cxx : trace_skeleton.i
	swig -python -c++ trace_skeleton.i

_trace_skeleton.so: trace_skeleton.i
	python setup.py build_ext --inplace
