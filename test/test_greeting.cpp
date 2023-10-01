#include <hello_world.hpp>
#include <cassert> // such advanced testing framework, wow
#include <iostream>

int main() {
  hello::hello_world my_hello;

  auto greeting = my_hello.get_greeting("Gleb");
  assert(greeting == "Hello, Gleb!");

  std::cout << "100\% Success!" << std::endl;
  return 0;
}
