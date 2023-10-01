cmake_minimum_required(VERSION 3.20)

option(TEST_DOC "Generate documentation" OFF)
option(TEST_TEST "Build and run tests" ON) # enabled by default just because TDD
option(TEST_EXAMPLES "Build examples" OFF)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

project(HelloWorld)

set(DOC_DIR ${PROJECT_SOURCE_DIR}/doc)
set(SRC_DIR ${PROJECT_SOURCE_DIR}/src)
set(TEST_DIR ${PROJECT_SOURCE_DIR}/test)
set(EXAMPLES_DIR ${PROJECT_SOURCE_DIR}/examples)

add_library(HelloWorld ${SRC_DIR}/hello_world.cpp)
target_include_directories(HelloWorld PUBLIC src)

if(TEST_TEST)
    add_subdirectory(${TEST_DIR})
endif()

if(TEST_DOC)
    add_subdirectory(${DOC_DIR})
endif()

if(TEST_EXAMPLES)
    add_subdirectory(${EXAMPLES_DIR})
endif()
