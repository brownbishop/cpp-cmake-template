cmake_minimum_required(VERSION 3.10)

project(test)

# for clangd
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_executable(test src/main.cpp)

