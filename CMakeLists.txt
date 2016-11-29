cmake_minimum_required(VERSION 2.8)

include(RezBuild)

file(GLOB_RECURSE py_files "python/*.py")

rez_install_python(
    py
    FILES ${py_files}
    DESTINATION .
)

file(GLOB resource_files "resources/*")

rez_install_files(
    ${resource_files}
    DESTINATION .
)
