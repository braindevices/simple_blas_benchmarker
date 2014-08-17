#!/usr/bin/env python    
# -*- coding: utf-8 -*-
import numpy
sizes=numpy.array([10,100,500,1000]) #6000太大了不用
numpy.save('/tmp/pinv_test_numpy_scipy_data_sizes',sizes)
fnames=dict.fromkeys(sizes)
for _i in sizes:

    x = numpy.random.random((_i*10,_i)) #float64 random sample
    y = numpy.linalg.pinv(x)
    _fname='/tmp/pinv_test_numpy_scipy_data%05d'%(_i)
    #print _fname
    numpy.savez_compressed(_fname,A=y,AT=x)
    fnames[_i]=_fname
numpy.save('/tmp/pinv_test_numpy_scipy_data_fnames',fnames)