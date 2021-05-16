import sys
import xml.etree.ElementTree as ET

from pprint import pprint


LIMITS = {
    "complexity": 2,
    "statements": 70,
    "others": 50
}

def read_xml(filename: str) -> list[dict]:
    tree = ET.parse(filename)
    root = tree.getroot()
    ans = []
    for child in root:
        print(child.tag)
        sub_childs = map(lambda item: (item.tag, item.text), child.iter())
        ans.append(tuple(sub_childs))
    # pprint(ans)
    tags = [item[1][1] for item in ans if len(item) > 1 and item[1][0] == 'Name']
    pprint(tags)
    print(len(tags))

def write_csv(filename: str):
    pass


def gen_stat(stat: list[dict]) -> bool:
    return True


if __name__ == "__main__":
    assert len(sys.argv) > 1
    filename = sys.argv[1]
    result = read_xml(filename)
    ret = gen_stat(result)
    if not ret:
        write_csv()
    exit(ret)