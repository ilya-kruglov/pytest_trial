import pytest

old_version = True


@pytest.mark.skipif(
    "sys.version_info > (2, 7)",
    reason='Только для старых версий Python'
)
def test_for_old_versions():
    assert old_version == True
