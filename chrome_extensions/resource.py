import json
import re

from flask import request, make_response, app
from flask_restful import Resource
from flask_cors import CORS
COMMA_BEFORR_BRACE = ",(?=\})"




def before_convert_to_json(string: str) -> str:
    string = string.replace(" ", "")
    string = string.replace("'", '"')
    string = string.replace("\n", "")
    string = re.sub(pattern=COMMA_BEFORR_BRACE, string=string, repl="")
    return string


# def write_to_csv()


class DirectIpProxy(Resource):
    def get(self):
        return json.dumps({"data": "None", "status": 200})

    def post(self):
        receive_data_tmp = request.get_data(as_text=True)
        receive_json = json.loads(before_convert_to_json(receive_data_tmp))
        print(receive_json)  # 接收到后打印出来

        return json.dumps({"status": 200, "method": "post"})


def register_direct_ipproxy_resource(api):
    api.add_resource(DirectIpProxy, "/direct_proxy/")

