# =================
# @time  : 2021/9/1 0:57
# @author: HerbLee
# @file  : fund_data.py
# =============================
import time

import requests
import json
import random
import pandas as pd

from collections import namedtuple

# =========================================
"""
基金公司信息
信息依次为 基金代码，基金名称，开放基金数量，封闭基金数量，总基金数量，开放基金份额，封闭基金份额，总基金份额
"""
FundCompany = namedtuple('FundCompany', ['id', 'name', 'OF', 'CF', 'total', 'share_open', "share_close", "share_total"])
# ==========================================
"""
简单的基金信息
"""
SimpleFundData = namedtuple("SimpleFundData", ['symbol', 'name', 'CompanyName', 'SubjectName'])


# ==========================================

def get_random_str(length=16):
    """
    get length random str
    :param length: 0 < length < 1000
    :return: str length
    """
    if length is None or not isinstance(length, int) or length > 1000 or length <= 0:
        length = 16

    alph = list("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    res_str = ""
    for idx in range(length):
        res_str += random.choice(alph)
    return res_str


def save_data_to_pandas(file_name, data):
    columns = []
    dd_data = []
    for dt in data:
        dt_dict = dt._asdict()
        print(dt_dict)
        if len(columns) == 0:
            columns = dt_dict.keys()
        dd_data.append(dt_dict.values())
    df = pd.DataFrame(columns=columns, data=dd_data)
    df.to_csv(file_name, encoding='GBK')


class FundDataTool:

    def __init__(self):
        pass

    def __format_sina_result(self, data_str, random_str):
        """
        格式化新浪拿到的数据
        :param data_str: 数据结果
        :param random_str: 申请时的随机值
        :return:
        """
        try:
            data_str = data_str.replace("/*<script>location.href='//sina.com';</script>*/", "")
            # data_str = data_str.decode("unicode-escape")
            data_str = data_str.replace("IO.XSRV2.CallbackList[{}]".format(random_str), "")
            data_str = data_str.replace("makeFilterData", "")
            data_str = data_str[2:-2]
            # print(data_str)
            # print(data_str)
            data_dict = eval(data_str)

        except:
            try:
                data_dict = json.loads(data_str)
            except:
                return None
        return data_dict

    def __format_company_data(self, data_str, random_str):
        """
        格式化基金公司数据
        :param data_str:
        :param random_str:
        :return: [FundCompany,FundCompany,...]
        """
        res_data = []
        data_dict = self.__format_sina_result(data_str, random_str)
        if data_dict is None:
            return res_data
        for fund_detail in data_dict.get("data", []):
            fund_company = FundCompany(fund_detail.get("FundCompanyId"),
                                       fund_detail.get("FundCompanyName"),
                                       fund_detail.get("FundNum_OF"),
                                       fund_detail.get("FundNum_CF"),
                                       fund_detail.get("FundNum_Total"),
                                       fund_detail.get("FundShare_Open"),
                                       fund_detail.get("FundShare_Close"),
                                       fund_detail.get("FundShare_Total"))
            res_data.append(fund_company)

        return res_data

    def get_all_fund_company_info(self):
        """
        获取所有基金公司信息
        :return: [FundCompany,FundCompany,...]
        """

        url = "http://vip.stock.finance.sina.com.cn/fund_center/data/jsonp.php/IO.XSRV2.CallbackList[" \
              "{}]/FundRank_Service.getFundCompanyList?page={}&num=40&sort=&type=jjglr&asc=1&ccode= "

        current_page = 1
        random_str = get_random_str()
        temp_url = url.format(random_str, current_page)
        current_page += 1
        net_res = requests.get(temp_url)
        res_data = self.__format_company_data(net_res.text, random_str)

        return res_data

    def get_all_fund_code(self):
        """
        获取所有基金code
        :return:
        """
        url = "http://stock.finance.sina.com.cn/fundfilter/api/openapi.php/MoneyFinanceFundFilterService" \
              ".getFundFilterAll?callback=makeFilterData&page={}&num=50&dpc=1"

        current_page = 1
        while True:
            random_str = get_random_str()
            temp_url = url.format(current_page)
            current_page += 1
            net_res = requests.get(temp_url)
            data_dict = self.__format_sina_result(net_res.text, random_str)

            if data_dict is None:
                break
            data_list = data_dict.get("result", {}).get("data", {}).get("data", {})
            if data_list is None or len(data_list) == 0:
                break

            res_list = [
                SimpleFundData(item
                               .get("symbol"), item.get("name"), item.get("CompanyName"), item.get("SubjectName"))
                for item in data_list]
            # 获取的基金数据，然后处理一下，可以整理一份基金ID出来然后存档
            # 再根据基金ID去查找基金的信息
            # print(len(data_dict.get("data")))

            time.sleep(1)
            break

    def get_fund_detail_info(self, code):
        """
        根据基金代码获取基金详细信息
        :param code: 基金代码
        :return:
        """

        # 当天信息
        # https://hq.sinajs.cn/list=fu_660001,......就可以查每天的数据

        url = "https://stock.finance.sina.com.cn/fundInfo/api/openapi.php/" \
              "FundPageInfoService.tabjjgk?symbol={}&format=json".format(code)

        net_res = requests.get(url)
        res = json.loads(net_res.text)

        print(res)


if __name__ == '__main__':
    fd = FundDataTool()
    res = fd.get_fund_detail_info("660001")
    # print(res)
