import sys
from functionCode.funApi import FunApi

if __name__ == "__main__":
    funapi = FunApi()

    if len(sys.argv):
        sheet = sys.argv[0]
        res = funapi.run_test(sheet)
    else:
        print("输入Sheet名称不能为空")
