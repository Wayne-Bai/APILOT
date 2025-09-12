import pandas as pd

def test_assert_series_equal():
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([1, 2, 3])
    s3 = pd.Series([1, '2', 3])

    # Mock assertion method for checking output
    def assert_series_equal(s1, s2, check_like=False, **kwargs):
        if not check_like:
            if s1.equals(s2):
                print("s1 is equal to s2")
            else:
                print(f"s1 is NOT equal to s2")
                print(f"s1: {s1}")
                print(f"s2: {s2}")
        else:
            print(f"Check like mode with s1: {s1}")
            print(f"Check like mode with s2: {s2}")

    # Test with default assertion
    assert_series_equal(s1, s2)

    # Test with check_like argument
    assert_series_equal(s1, s3, check_like=True)

test_assert_series_equal()
