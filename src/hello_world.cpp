#include <hello_world.hpp>
#include <iostream>

std::string hello::hello_world::get_greeting(std::string name) {
  return "Hello, " + name + "!";
}

void hello::hello_world::print_greeting(std::string name) {
  std::cout << get_greeting(name) << '\n';
}
