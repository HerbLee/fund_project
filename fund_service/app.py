from sanic import Sanic
from config import log_config, CONFIG
from models import init_db, init_cache, close_db, close_cache
from blueprints import api, handle_exception

from sanic_cors import CORS
from sanic_openapi import openapi3_blueprint

app = Sanic(CONFIG.NAME.capitalize(), log_config=log_config)

app.config.update_config(CONFIG)

app.error_handler.add(Exception, handle_exception)

app.blueprint(api)

# swagger api
app.blueprint(openapi3_blueprint)

CORS(app, resources={r"*": {"origins": "*"}})


@app.listener("before_server_start")
async def server_init(app, loop):
    app.db = await init_db(app.config)
    app.cache = await init_cache(app.config)


@app.listener("after_server_stop")
async def server_clean(app, loop):
    await close_cache(app.cache)
    await close_db(app.db)


if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'],
            auto_reload=app.config['AUTO_RELOAD'],
            access_log=app.config['ACCESS_LOG'],
            workers=app.config['WORKERS'])
