#!/usr/bin/env python     
# -*- coding: utf-8 -*-
import numpy
import scipy.linalg as linalg
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
fnames=numpy.load('/tmp/pinv_test_numpy_scipy_data_fnames.npy')[None][0]
N=5
ts0=[]
ts1=[]
ts2=[]
accuracy=[]
sizes=fnames.keys()
sizes.sort()
for _i in sizes:
    _fname=fnames[_i]
    _data = numpy.load('%s.npz'%(_fname))
    _A=_data['A']
    _AT=_data['AT']
    _result = [numpy.linalg.pinv(_A),linalg.pinv(_A),linalg.pinv2(_A)]
    _accuracy = [numpy.linalg.norm(_x-_AT) for _x in _result]
    print "pinv errors [numpy_pinv, scipy_pinv, scipy_pinv2] = ",_accuracy
    accuracy.append(_accuracy)
    
    setup = "import numpy; data = numpy.load('%s.npz');A=data['A']"%(_fname)
    count = N
    
    t = timeit.Timer("numpy.linalg.pinv(A)", setup=setup)
    print "size=",_i,"pinv:", t.timeit(count)/count, "sec"
    #code执行了N次
    ts0.append(t.timeit(count)/count)
    
    setup = "import numpy; data = numpy.load('%s.npz');A=data['A'];import scipy.linalg as linalg"%(_fname)
    t = timeit.Timer("linalg.pinv(A)", setup=setup)
    print "size=",_i,"scipy_pinv:", t.timeit(count)/count, "sec"
    ts1.append(t.timeit(count)/count)
    t = timeit.Timer("linalg.pinv2(A)", setup=setup)
    print "size=",_i,"scipy_pinv2:", t.timeit(count)/count, "sec"
    ts2.append(t.timeit(count)/count)
    
numpy.savetxt('/tmp/test_numpy_scipy_pinv_errors.txt',accuracy)
numpy.savetxt('/tmp/test_numpy_result_pinv.txt',ts0)
numpy.savetxt('/tmp/test_scipy_result_pinv.txt',ts1)
numpy.savetxt('/tmp/test_scipy_result_pinv2.txt',ts2)