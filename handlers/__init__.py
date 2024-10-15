from .other_handlers import router as other_router
from .product_handlers import router as product_router
from .exchanges_handlers import router as exchanges_router
from .news_handlers import router as news_router

routers = [other_router, product_router, exchanges_router, news_router]





