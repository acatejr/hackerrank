def swap_case(s):
    """_summary_

    Args:
        s (_type_): _description_

    Returns:
        _type_: _description_


    Usage examples:
    >>> swap_case("Www.HackerRank.com")
    'wWW.hACKERrANK.COM'
    >>> swap_case("Pythonist 2")
    'pYTHONIST 2'
    """

    _s = s.swapcase()
    return _s


# if __name__ == '__main__':
#     s = "Www.HackerRank.com"
#     print(swap_case(s))

#     s = "Pythonist 2"
#     print(swap_case(s))