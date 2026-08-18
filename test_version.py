from version import is_newer_version
from rollback import allow_firmware_update


def test_new_version():
    assert is_newer_version("1.1.0", "1.0.0") is True


def test_old_version():
    assert is_newer_version("1.0.0", "1.1.0") is False


def test_same_version():
    assert allow_firmware_update("1.0.0", "1.0.0") is False


def test_rollback():
    assert allow_firmware_update("2.0.0", "1.0.0") is False


def test_valid_update():
    assert allow_firmware_update("1.0.0", "1.1.0") is True
