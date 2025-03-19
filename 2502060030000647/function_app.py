# import logging
# import azure.functions as func

# app = func.FunctionApp()

# @app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=False,
#               use_monitor=False) 
# def mytimer(myTimer: func.TimerRequest) -> None:
#     if myTimer.past_due:
#         logging.info('The timer is past due!')

#     logging.info('Python timer trigger function executed.')

import requests


import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="mytimer")
@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    url = "https://learn.microsoft.com/en-us/"
    try:
        response = requests.get(url)
        logging.info(response.status_code)
        response.raise_for_status()
    except requests.Timeout as e:
        logging.error(f"HTTPリクエストタイムアウト: {e}")
    except requests.ConnectionError as e:
        logging.error(f"HTTPリクエスト接続エラー: {e}")
    except requests.RequestException as e:
        logging.error(f"HTTPリクエスト失敗: {e.__class__.__name__}: {e}")
    logging.info('Python timer trigger function executed.')