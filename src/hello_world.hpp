/**
 * @file hello_world.hpp
 *
 * This is a small useful library, that allows user to pretty print greetings.
 *
 */
#ifndef HELLO_WORLD_HPP
#define HELLO_WORLD_HPP

#include <string>

/**
 * @brief Main namespace of a library
 *
 * This namespace contains main library class - `hello_world`
 *
 * Sad, but MyST Markdown capabilities does not work inside code documentation
 * Because MyST handles standalone `.md` files. Documentation is handled by
 * Breathe.
 *
 * So admonitions do not work and cause a warning `WARNING: Pygments lexer name
 * 'tip' is not known`
 *
 * ```cpp
 * int main() {
 *   hello::hello_world my_hello;
 *   my_hello.print_greeting();
 *   return 0;
 * }
 * ```
 */
namespace hello {

/**
 * @brief Greeting generator
 *
 * This small yet super useful class allows you to print your (but not only
 * your) name in a super cool greeting.
 *
 * @sa [hello world
 * program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
 */
class hello_world {
public:
  /**
   * @brief Function that creates greetings
   *
   * Supply you name to this function, and it will return you the string
   * "Hello, {your-name}!". Of course, if your PC has enough RAM to store this
   * string, otherwise it may not work. And it also _may_ throw an exception,
   * and in this case you will not get your pretty greeting. Yes, life is cruel.
   *
   * You even can not supply your (or any) name. In this case function will
   * return classical "Hello, World!". Not bad, right?
   *
   * @warning This method really can throw an exception!
   *
   * @param name Your name you want to appear in a greeting
   * @return Instance of `std::string`, that contain the greeting
   */
  std::string get_greeting(std::string name = "World");

  /**
   * @brief Creates greeting string and prints it to stdout
   *
   * If you toooooo lazy to include <iostream>, type `std::cout` and `std::endl`
   * and just want to get your greeting in a console, use this function. It is
   * so kind, that it prints the greeting to stdout itself, freeing you from
   * this boring routine. Except this feature, this function is the same as
   * the `hello_world::get_greeting` function.
   *
   * @note
   * Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce iaculis urna
   * sit amet semper porta. Sed eget convallis nulla. Quisque at ornare eros, ac
   * cursus erat. Fusce sed ante sit amet risus bibendum volutpat. Sed leo est,
   * molestie ut tincidunt mattis, viverra eu est. Nullam euismod cursus tortor,
   * sit amet tincidunt orci pellentesque at. Suspendisse potenti. Ut imperdiet,
   * dolor sed blandit commodo, felis augue placerat tellus, vitae feugiat
   * mauris quam nec massa. In rutrum tincidunt lectus, eu congue massa
   * facilisis eu. Nullam ultrices velit eu imperdiet auctor. Donec in elit et
   * nisl laoreet feugiat ut sit amet dolor. Integer scelerisque ullamcorper
   * ante, in lacinia massa egestas eu. Aliquam diam dolor, ultrices sit amet
   * justo eu, condimentum luctus tellus.
   */
  void print_greeting(std::string name);
};

/**
 * @brief Inspect type function
 *
 * This simple function is a great help, when you're writing highly templatized
 * code. You can supply the type to it and see its representation.
 *
 * You can do either this:
 *
 * ```cpp
 * inspect_type<MyType>();
 * ```
 *
 * to inspect a type, or this:
 *
 * ```cpp
 * inspect_type<decltype(my_var)>();
 * ```
 *
 * to inspect the type of a variable.
 */
template <typename T>
void inspect_type() {
  printf("Inspect type: %s\n", __PRETTY_FUNCTION__);
}

} // namespace hello

#endif
