
def filter_inner(start, end):
    """
    过滤器：[start,to) 左侧为闭区间，右侧为开区间。
    :param start:
    :param to:
    :return:
    """
    if start > end:
        raise ValueError("start must be gt end!")
    return lambda x: x >= start and x < end


def fetch_inner(src, start, end):
    """
    从集合中挑选符合条件的元素
    :param src:
    :param start:
    :param end:
    :return:
    """
    if src is None:
        raise ValueError("src must be none!")
    if not isinstance(src, list):
        raise ValueError("src must be type list!")
    return list(filter(filter_inner(start, end), src))


class YearUtils(object):
    """
    年信息的工具类
    """

    @staticmethod
    def shorten(src_years):
        """
        将包含年的数组，转换为比较简洁的描述形式。
        示例：src = [1998,1999,2001,2002,2003,2004,2005,2008,2009,2010,2011,2012,2013,2015]
        =====》dest=["1998-1999","2001-2005","2008-2013,"2015"]
        :param src_years: 包含年信息的列表（或数组）
        :return:
        """
        cover = []
        end_year = max(src_years)
        start_year = min(src_years)
        ordered_year = sorted(src_years)

        lack_years = []
        for x in range(start_year, end_year):
            if x not in ordered_year:
                lack_years.append(x)

        latest_year = min(ordered_year)
        for lack_year in lack_years:
            last1_year = lack_year
            if latest_year == last1_year:
                inner = latest_year
            else:
                inner = fetch_inner(ordered_year, latest_year, last1_year)
            latest_year = lack_year
            added = YearUtils.reset_range(inner)
            if len(added) > 0:
                cover.append(added)
        inner = fetch_inner(ordered_year, latest_year, max(ordered_year) + 1)
        added = YearUtils.reset_range(inner)
        if len(added) > 0:
            cover.append(added)
        return cover

    @staticmethod
    def reset_range(range_list):
        """
        将连续的数字，采用xxx-yyy的表示方法进行描述
        举例：1994,1995,1996,1997
        :param range_list:
        :return:
        """
        if not isinstance(range_list, list):
            raise ValueError("range_list must be type of list!")
        if range_list is None or len(range_list) == 0:
           return ""
        if len(range_list) == 1:
            return "{}".format(range_list[0])
        else:
            return "{}-{}".format(min(range_list), max(range_list))

    pass





if __name__ == "__main__":
    ordered_year = [1992, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2004, 2007]
    lack_years = [1993, 2002, 2003, 2005, 2006]

    s_years = YearUtils.shorten(ordered_year)
    print(s_years)
