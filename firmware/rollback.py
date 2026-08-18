from .version import parse_version


def allow_firmware_update(current_version, new_version):
    current = parse_version(current_version)
    new = parse_version(new_version)

    if new <= current:
        return False

    return True
