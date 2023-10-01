/**
 * @file print_greeting.cpp
 *
 * This is an example of how to use `hello_world` class.
 */

#include <hello_world.hpp>
#include <iostream>

int main() {
  hello::hello_world my_hello;

  std::cout << "Enter your name: ";

  std::string name;
  std::cin >> name;

  std::cout << '\n';

  my_hello.print_greeting(name);
}
