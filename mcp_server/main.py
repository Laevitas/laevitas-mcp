from mcp.server.fastmcp import FastMCP

from .client import ApiClient
from .controllers.analytics_controller import AnalyticsController
from .catalog_loader import register_catalog_endpoints


def run() -> None:
    mcp = FastMCP("laevitas")
    client = ApiClient()

    # Register controllers
    AnalyticsController(mcp, client)
    # Register legacy endpoints from catalog
    register_catalog_endpoints(mcp, client)

    mcp.run(transport="stdio")


if __name__ == "__main__":
    run()
