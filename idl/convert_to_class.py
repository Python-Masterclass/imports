import dataclasses
import re


type_map = {
    "long": int,
    "string": str,
    "float": float,
}


def convert_idl(idl_data: str):
    token_iter = (t.strip() for t in re.split(r"(\W)", idl_data) if t.strip() != "")
    attributes = []
    while token := next(token_iter):
        match token:
            case "interface":
                class_name = "".join(n.capitalize() for n in next(token_iter).split("_"))
                assert next(token_iter) == "{"
            case "long" | "string" | "float":
                attr_name = next(token_iter)
                attributes.append((attr_name, type_map[token]))
                assert next(token_iter) == ";"
            case "}":
                break
    idl_cls = dataclasses.make_dataclass(class_name, attributes)
    return idl_cls


if __name__ == "__main__":
    with open("result_data.idl") as f:
        data = f.read()
    IdlCls = convert_idl(data)
    x = IdlCls(1, "hallo", 3.14)
    print(x)
