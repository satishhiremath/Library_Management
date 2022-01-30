load("@rules_python//python:defs.bzl", "py_library", "py_test", "py_binary")

py_binary(
    name = "library_management_binary",
    srcs = [
        "custom_exceptions.py",
        "library.py",
        "user.py",
        "library_management.py"
    ],
    main = "library_management.py",
    visibility = ["//visibility:public"],
)
