project(TestTesting)

add_executable(HelloTest test_greeting.cpp)
target_link_libraries(HelloTest PRIVATE HelloWorld)


add_custom_target(RunHelloTest ALL
    COMMAND HelloTest
    DEPENDS HelloTest
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)
