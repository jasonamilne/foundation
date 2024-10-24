from solutions import Solution
import pytest
import random
import string

@pytest.fixture
def solution():
    return Solution()

# Test normal cases functionality
def test_lengthOfLongestSubstring_normal_cases(solution):
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3  # "abc"
    assert solution.lengthOfLongestSubstring("bbbbb") == 1     # "b"
    assert solution.lengthOfLongestSubstring("pwwkew") == 3    # "wke"
    assert solution.lengthOfLongestSubstring("") == 0          # ""
    assert solution.lengthOfLongestSubstring(" ") == 1         # " "
    assert solution.lengthOfLongestSubstring("au") == 2        # "au"
    assert solution.lengthOfLongestSubstring("dvdf") == 3      # "vdf"

# Test edge cases functionality
def test_lengthOfLongestSubstring_edge_cases(solution):
    assert solution.lengthOfLongestSubstring("") == 0          # ""
    assert solution.lengthOfLongestSubstring(" ") == 1         # " "

# Test special cases functionality
def test_lengthOfLongestSubstring_special_cases(solution):
    assert solution.lengthOfLongestSubstring("a") == 1         # "a"
    assert solution.lengthOfLongestSubstring("abcdefg") == 7   # "abcdefg"

# Test performance cases functionality
def test_lengthOfLongestSubstring_performance_cases(solution):
    long_string = "a" * 10000 + "b"
    assert solution.lengthOfLongestSubstring(long_string) == 2  # "ab"

# Test alternative paths functionality
def test_lengthOfLongestSubstring_alternative_paths(solution):
    assert solution.lengthOfLongestSubstring("abba") == 2      # "ab" or "ba"

# Test compatibility cases functionality
def test_lengthOfLongestSubstring_compatibility_cases(solution):
    assert solution.lengthOfLongestSubstring("abcABC") == 6    # "abcABC"

# Test usability cases functionality
def test_lengthOfLongestSubstring_usability_cases(solution):
    assert solution.lengthOfLongestSubstring("a b c") == 3     # "a b c"

# Test localization cases functionality
def test_lengthOfLongestSubstring_localization_cases(solution):
    assert solution.lengthOfLongestSubstring("你好世界你好世界") == 4  # "你好世界"

# Test regression testing functionality
def test_lengthOfLongestSubstring_regression_testing(solution):
    # Assuming a previous bug with specific input
    assert solution.lengthOfLongestSubstring("dvdf") == 3      # "vdf"

# Test all identical characters functionality
def test_lengthOfLongestSubstring_all_identical_characters(solution):
    assert solution.lengthOfLongestSubstring("aaaaa") == 1     # "a"

# Test long unique string functionality
def test_lengthOfLongestSubstring_long_unique_string(solution):
    assert solution.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyz") == 26  # "abcdefghijklmnopqrstuvwxyz"

# Test special characters functionality
def test_lengthOfLongestSubstring_special_characters(solution):
    assert solution.lengthOfLongestSubstring("a!@#b!@#c") == 5  # "a!@#b"

# Test robustness by utilizing random strings
def test_lengthOfLongestSubstring_randomized(solution):
    for _ in range(10):  # Run 10 random tests
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
        # Since the string is random, we can't predict the exact result, but we can ensure it runs without error
        result = solution.lengthOfLongestSubstring(random_string)
        assert isinstance(result, int)  # Ensure the result is an integer

# Test edge case with maximum length
def test_lengthOfLongestSubstring_max_length(solution):
    max_length_string = ''.join(random.choices(string.ascii_letters + string.digits, k=1000000))
    # This test is primarily to ensure performance and should complete in a reasonable time
    result = solution.lengthOfLongestSubstring(max_length_string)
    assert isinstance(result, int)  # Ensure the result is an integer
