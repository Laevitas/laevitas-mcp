from mcp.server.fastmcp import FastMCP

from .client import ApiClient
from .controllers.analytics_controller import AnalyticsController


def run() -> None:
    mcp = FastMCP("laevitas")
    client = ApiClient()

    # Register controllers
    AnalyticsController(mcp, client)

    mcp.run(transport="stdio")


if __name__ == "__main__":
    run()
