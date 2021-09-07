from sanic import Sanic
from config import config, log_config
from models import init_db, init_cache, close_db, close_cache
from blueprints import api, handle_exception



app = Sanic(config['NAME'].capitalize(), log_config=log_config)
app.config.update(config)
app.error_handler.add(Exception, handle_exception)

app.blueprint(api)


@app.listener("before_server_start")
async def server_init(app, loop):
    app.db = await init_db(config)
    app.cache = await init_cache(config)


@app.listener("after_server_stop")
async def server_clean(app, loop):
    await close_cache(app.cache)
    await close_db(app.db)

if __name__ == '__main__':
    app.run(host=config['HOST'],
            port=config['PORT'],
            debug=config['DEBUG'],
            auto_reload=config['AUTO_RELOAD'],
            access_log=config['ACCESS_LOG'],
            workers=config['WORKERS'])
