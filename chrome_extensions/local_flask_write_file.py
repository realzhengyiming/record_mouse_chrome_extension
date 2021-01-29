import json
import traceback

from flask import Flask, make_response
from flask_cors import CORS
from flask_restful import Api
from loguru import logger

from resource import register_direct_ipproxy_resource


def app_creater(app_name: str = "ipproxy_service"):
    app = Flask(app_name)
    CORS(app, supports_credentials=True)
    api = Api(app)
    register_direct_ipproxy_resource(api)

    @app.errorhandler(Exception)
    def internal_error(error):
        error_tb = traceback.format_exc()
        logger.error(error_tb)
        return json.dumps(error_tb), 500

    @app.after_request
    def af_request(resp):
        """
        #请求钩子，在所有的请求发生后执行，加入headers。
        :param resp:
        :return:
        """
        resp = make_response(resp)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
        resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        return resp

    return app


if __name__ == '__main__':
    app = app_creater("ipproxy_service")
    app.run(debug=True, port=9999, host="0.0.0.0")
