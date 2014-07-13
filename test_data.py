#!/usr/bin/env python    
# -*- coding: utf-8 -*-
import numpy
sizes=numpy.array([10,100,3000]) #6000太大了不用
numpy.save('/tmp/test_numpy_scipy_data_sizes',sizes)
fnames=dict.fromkeys(sizes)
for _i in sizes:

    x = numpy.random.random((_i,_i)) #float64 random sample
    _fname='/tmp/test_numpy_scipy_data%05d'%(_i)
    numpy.save(_fname,x)
    fnames[_i]=_fname
numpy.save('/tmp/test_numpy_scipy_data_fnames',fnames)