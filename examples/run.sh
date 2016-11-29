#!/bin/bash

CONFIG=/da/sw/omegalib/configs/desktop.vrpnControllers.cfg
SCRIPT=/da/dev/luke/sources/daHandles/examples/manipulator.py

export PYTHONPATH=/da/dev/luke/sources/daHandles/python

/da/sw/omegalib/runOmegalib.v6.libav56.sh ${CONFIG} ${SCRIPT} 
