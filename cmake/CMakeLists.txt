cmake_minimum_required(VERSION 3.7)

project (gird_world)

set (CMAKE_MAJOR_VERSION 0)
set (CMAKE_MINOR_VERSION 1)
set (CMAKE_PATCH_VERSION 0)

add_executable(grid_world main.cpp)

install (TARGETS grid_world DESTINATION ${CMAKE_INSTALL_PREFIX}/grid_world-${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION}.${CMAKE_PATCH_VERSION})
