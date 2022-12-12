from idl_parser import parse_idl


def create_python_module(mod_name, directory="."):
    with open(f"{directory}/{mod_name}.idl") as f:
        data = f.read()
    class_name, attributes = parse_idl(data)
    module_body = [
        "import dataclasses",
        "",
        "",
        "@dataclasses.dataclass",
        f"class {class_name}:",
    ]
    for attr_name, attr_type in attributes:
        module_body.append(f"    {attr_name}: {attr_type.__name__}")

    with open(f"{directory}/{mod_name}.py", "w") as f:
        f.write("\n".join(module_body))


if __name__ == "__main__":
    create_python_module("result_data")
