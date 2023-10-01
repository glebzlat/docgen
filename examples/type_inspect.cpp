#include <hello_world.hpp>
#include <type_traits>

// <<type-pack-impl>>
template <typename T> struct just_type {
  using type = T;
};

template <typename... Ts> struct type_pack {
  static constexpr std::size_t size() { return sizeof...(Ts); }

  static constexpr bool empty() { return size() == 0; }
};

using empty_pack = type_pack<>;

template <typename> struct Error_Type_Pack_Out_Of_Range;

template <std::size_t Idx, std::size_t Count, class TP, typename>
struct at_helper {
  using type = typename Error_Type_Pack_Out_Of_Range<TP>::type;
};

template <std::size_t Idx, std::size_t Count, typename T, typename... Ts>
struct at_helper<Idx, Count, type_pack<T, Ts...>,
                 typename std::enable_if<Idx == Count, void>::type> {
  using type = T;
};

template <std::size_t Idx, std::size_t Count, typename T, typename... Ts>
struct at_helper<Idx, Count, type_pack<T, Ts...>,
                 typename std::enable_if<Idx != Count, void>::type> {
  using type = typename at_helper<Idx, Count + 1, type_pack<Ts...>, void>::type;
};

template <std::size_t Idx, class TP> struct at : at_helper<Idx, 0, TP, void> {};

template <std::size_t Idx, class TP> using at_t = typename at<Idx, TP>::type;

// <</type-pack-impl>>

int main() {
  // <<simple-example>>
  hello::inspect_type<int>();
  // <</simple-example>>

  // <<complicated-example>>
  auto a = 10;
  hello::inspect_type<decltype(a)>();
  hello::inspect_type<std::add_rvalue_reference_t<decltype(a)>>();
  // <</complicated-example>>

  // <<sample-1>>
  // <<type-pack-sample>>
  using tp = type_pack<int, double, float>;
  using type = at_t<1, tp>;
  // <</type-pack-sample>>
  hello::inspect_type<type>();
  // <</sample-1>>
}
