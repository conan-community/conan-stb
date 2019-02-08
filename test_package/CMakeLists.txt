PROJECT(MyHello)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
CONAN_BASIC_SETUP(TARGETS)

add_executable(example example.c)
IF(UNIX)
    target_link_libraries(example CONAN_PKG::stb m)
ELSE()
    target_link_libraries(example CONAN_PKG::stb)
ENDIF()