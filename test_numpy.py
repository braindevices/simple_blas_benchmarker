#!/usr/bin/env python     
# -*- coding: utf-8 -*-
import numpy
import sys
import timeit

try:
    import numpy.core._dotblas
    print 'FAST BLAS'
except ImportError:
    print 'slow blas'

print "version:", numpy.__version__
print "maxint:", sys.maxint
print
fnames=numpy.load('/tmp/test_numpy_scipy_data_fnames.npy')[None][0]
N=5
ts=[]
sizes=fnames.keys()
sizes.sort()
for _i in sizes:
    _fname=fnames[_i]
    setup = "import numpy; x = numpy.load('%s.npy')"%(_fname)
    count = N
    
    t = timeit.Timer("numpy.dot(x, x.T)", setup=setup)
    print "size=",_i,"dot:", t.timeit(count)/count, "sec"
    ts.append(t.timeit(count)/count)
print "ts=", ts
numpy.savetxt('/tmp/test_numpy_scipy_result_dot.txt',ts)

