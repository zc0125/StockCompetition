#coding=utf-8

from handlers import user_info
from handlers import verify_code
from handlers import favorite_stocks
from handlers import user_hold_stocks
from handlers import trade
from handlers import contest
from handlers import contest_trade

urls = [
    (r'/api/login', user_info.LoginHandler),
    (r'/api/logout', user_info.LogoutHandler),
    (r'/api/register', user_info.RegisterHanler),
    (r'/api/getuserinfo', user_info.GetUserInfo),

    (r'/piccode', verify_code.PicCodeHandler),
    (r'/api/checkpic', verify_code.SMSCodeHandler),

    # 用戶自選股
    (r'/api/favoritestock/add', favorite_stocks.AddStock2FavoriteHandler),
    (r'/api/favoritestock/del', favorite_stocks.DelStockHandler),
    (r'/api/favoritestock/checkin', favorite_stocks.CheckStockHandler),
    (r'/api/favoritestock/list', favorite_stocks.GetStockListHandler),

    # 持倉股票
    (r'/api/holdstocks/list', user_hold_stocks.GetStockList),

    # 股票交易記錄相關
    (r'/api/stocks/buy', trade.BuyStockHander),
    (r'/api/stocks/sale', trade.SaleStockHandler),
    (r'/api/stocks/history/tradelist', trade.GetTradeHistoryHandler),
    (r'/api/stocks/invoke', trade.InvokeStockHandler),

    # 比賽相關
    (r'/api/contest/create', contest.ContestCreate),
    (r'/api/contest/join', contest.ContestJoin),
    (r'/api/contest/list', contest.Contest_get_list),
    (r'/api/contest/list/user', contest.Contest_get_user_contest),
    (r'/api/contest/quit', contest.ContestQuit),
    (r'/api/contest/detail/ranklist', contest.Contest_get_contest_rank),
    (r'/api/contest/checkin', contest.Contest_check_in_contest),
    (r'/api/contest/userinfo', contest.ContestUserInfo),

    (r'/api/contest/stocks/list', contest_trade.ListContestStocks),
    (r'/api/contest/stocks/buy', contest_trade.BuyStockHander),
    (r'/api/contest/stocks/sale', contest_trade.SaleStockHandler),
    (r'/api/contest/stocks/invoke', contest_trade.InvokeStockHandler),
    (r'/api/contest/stocks/history/tradelist', contest_trade.GetTradeHistoryHandler),
]

def main():
    pass


if __name__ == '__main__':
    main()