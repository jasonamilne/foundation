from solutions import Solution
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_lengthOfLongestSubstring(solution):
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3  # "abc"
    assert solution.lengthOfLongestSubstring("bbbbb") == 1     # "b"
    assert solution.lengthOfLongestSubstring("pwwkew") == 3    # "wke"
    assert solution.lengthOfLongestSubstring("") == 0          # ""
    assert solution.lengthOfLongestSubstring(" ") == 1         # " "
    assert solution.lengthOfLongestSubstring("au") == 2        # "au"
    assert solution.lengthOfLongestSubstring("dvdf") == 3      # "vdf"

def test_lengthOfLongestSubstring_normal_cases(solution):
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3  # "abc"
    assert solution.lengthOfLongestSubstring("pwwkew") == 3    # "wke"

def test_lengthOfLongestSubstring_edge_cases(solution):
    assert solution.lengthOfLongestSubstring("") == 0          # ""
    assert solution.lengthOfLongestSubstring(" ") == 1         # " "

def test_lengthOfLongestSubstring_special_cases(solution):
    assert solution.lengthOfLongestSubstring("a") == 1         # "a"
    assert solution.lengthOfLongestSubstring("abcdefg") == 7   # "abcdefg"

def test_lengthOfLongestSubstring_performance_cases(solution):
    long_string = "a" * 10000 + "b"
    assert solution.lengthOfLongestSubstring(long_string) == 2  # "ab"

def test_lengthOfLongestSubstring_alternative_paths(solution):
    assert solution.lengthOfLongestSubstring("abba") == 2      # "ab" or "ba"

def test_lengthOfLongestSubstring_compatibility_cases(solution):
    assert solution.lengthOfLongestSubstring("abcABC") == 6    # "abcABC"

def test_lengthOfLongestSubstring_usability_cases(solution):
    assert solution.lengthOfLongestSubstring("a b c") == 3     # "a b c"

def test_lengthOfLongestSubstring_localization_cases(solution):
    assert solution.lengthOfLongestSubstring("你好世界你好世界") == 4  # "你好世界"

def test_lengthOfLongestSubstring_regression_testing(solution):
    # Assuming a previous bug with specific input
    assert solution.lengthOfLongestSubstring("dvdf") == 3      # "vdf"
