#!/bin/bash -e
bkdate=$(date +"%Y%m%d-%H%M%S")
logFile="tests-log-${bkdate}.txt"

TMPDIR="${HOME}/mytmp/tmp"
export TMPDIR

python -c "import sys; print sys.executable" | tee -a ${logFile}
echo "OMP_NUM_THREADS = ${OMP_NUM_THREADS}" | tee -a ${logFile}
echo "###sys BLAS config###>>>" | tee -a ${logFile}
#find /usr/lib -maxdepth 1 -type l -iname "*libblas*"|xargs -I{} sh -c 'echo "{} =>" $(realpath {})' | tee -a ${logFile}
#find /usr/lib -maxdepth 1 -type l -iname "*liblapack*"|xargs -I{} sh -c 'echo "{} =>" $(realpath {})' | tee -a ${logFile}
find /usr/lib -maxdepth 1 -type l \( -iname "*libblas*" -or -iname "*liblapack*" \) -exec echo -n "{} =>" \; -exec realpath {} \; | tee -a ${logFile}
echo "###sys BLAS config###<<<" | tee -a ${logFile}
echo "###site.cfg###>>>" | tee -a ${logFile}
python -c "import numpy; print numpy.__config__.show();" | tee -a ${logFile}
echo "###site.cfg###<<<" | tee -a ${logFile}
set -v
#python test_data.py 2>&1 | tee -a ${logFile} all BLAS should be test with the same set of data, so generate the data then run all test on it
cp test_data/* /tmp/
python test_numpy.py 2>&1 | tee -a ${logFile}
python test_scipy.py 2>&1 | tee -a ${logFile}
mkdir "tests-log-${bkdate}"
cp /tmp/test_numpy_scipy_result_* "tests-log-${bkdate}/"
set +v