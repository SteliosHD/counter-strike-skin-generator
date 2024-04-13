import pytest
from data_preparation.prepare_data import (
    load_image_file_based_on_name_pattern,
    price_string_to_float,
    quality_class_to_int,
)


def test_should_load_image_file_based_on_name_pattern():
    # Setup
    skin_name = "Syndicate"
    skin_id = "2"
    expected_file = "Syndicate_2_RestrictedPistol_CZ75-Auto.png"
    # Act
    actual_file = load_image_file_based_on_name_pattern([skin_name, skin_id])
    # Assert
    assert actual_file == expected_file


def test_should_raise_error_when_image_file_not_found():
    # Setup
    skin_name = "not a skin name"
    # Act
    # Assert
    with pytest.raises(FileNotFoundError) as exc_info:
        load_image_file_based_on_name_pattern([skin_name])
    assert "not found" in str(exc_info.value)


def test_string_with_euro_and_comma_should_work():
    # Setup
    string_with_euro = "1234,56€"
    expected_float = 1234.56
    # Act
    actual_float = price_string_to_float(string_with_euro)
    # Assert
    assert actual_float == expected_float


def test_string_with_euro_and_dot_should_work():
    # Setup
    string_with_euro = "1234.56€"
    expected_float = 1234.56
    # Act
    actual_float = price_string_to_float(string_with_euro)
    # Assert
    assert actual_float == expected_float


def test_string_with_euro_comma_and_space_should_work():
    # Setup
    string_with_euro = "1 234,56€"
    expected_float = 1234.56
    # Act
    actual_float = price_string_to_float(string_with_euro)
    # Assert
    assert actual_float == expected_float


def test_string_with_euro_comma_and_dash_should_work():
    # Setup
    string_with_euro = "1234,--€"
    expected_float = 1234.0
    # Act
    actual_float = price_string_to_float(string_with_euro)
    # Assert
    assert actual_float == expected_float


def test_string_with_dot_should_work():
    # Setup
    string_with_dot = "1234.56"
    expected_float = 1234.56
    # Act
    actual_float = price_string_to_float(string_with_dot)
    # Assert
    assert actual_float == expected_float


def test_string_with_text_should_return_none():
    # Setup
    string_with_euro = "not a price"
    # Act
    none_value = price_string_to_float(string_with_euro)
    # Assert
    assert none_value is None


def test_should_return_correct_quality_class_int():
    # Setup
    quality_class = "Mil-Spec Rifle"
    expected_int = 2
    # Act
    actual_int = quality_class_to_int(quality_class)
    # Assert
    assert actual_int == expected_int
