project(HelloWorldExamples)

add_executable(PrintGreeting print_greeting.cpp)
target_link_libraries(PrintGreeting PRIVATE HelloWorld)
