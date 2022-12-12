import re


type_map = {
    "long": int,
    "string": str,
    "float": float,
}


def parse_idl(idl_data: str):
    token_iter = (token for token in (t.strip() for t in re.split(r"(\W)", idl_data)) if token != "")
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
    return class_name, attributes
