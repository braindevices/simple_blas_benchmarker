#!/usr/bin/env python    
# -*- coding: utf-8 -*-
import timeit, numpy
fnames=numpy.load('/tmp/test_numpy_scipy_data_fnames.npy')[None][0]
N=5
ts=[]
ts2=[]
sizes=fnames.keys()
sizes.sort()
for _i in sizes:
    _fname=fnames[_i]
    setup = "import numpy;\
            import scipy.linalg as linalg;\
            x = numpy.load('%s.npy');\
            z = numpy.dot(x, x.T)"%(_fname)
    count = N

    t = timeit.Timer("linalg.cholesky(z, lower=True)", setup=setup)
    print "size=",_i, "cholesky:", t.timeit(count)/count, "sec"
    ts.append(t.timeit(count)/count)
    #if _i>1000:
        #continue
    t = timeit.Timer("linalg.svd(z)", setup=setup)
    print "size=",_i,"svd:", t.timeit(count)/count, "sec"
    ts2.append(t.timeit(count)/count)
numpy.savetxt('/tmp/test_numpy_scipy_result_cholesky.txt',ts)
numpy.savetxt('/tmp/test_numpy_scipy_result_svd.txt',ts2)