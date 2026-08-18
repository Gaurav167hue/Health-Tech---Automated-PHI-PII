CURRENT_VERSION = "1.0.0"


def parse_version(version):
    return tuple(map(int, version.split(".")))


def is_newer_version(new_version, current_version):
    return parse_version(new_version) > parse_version(current_version)
