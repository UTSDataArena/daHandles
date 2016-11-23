# -*- coding: utf-8 -*-

name = 'pyhandles'

version = '0.1.0'

description = 'On-screen handles library for the Data Arena'

requires = ['python']

variants = [['platform-linux', 'arch-x86_64', 'os-Gentoo-2.2']]


def commands():
    env.PYTHONPATH.append('{root}/python')
