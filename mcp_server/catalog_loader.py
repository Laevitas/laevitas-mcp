import json
import inspect
from typing import Any, Dict, List

from mcp.server.fastmcp import FastMCP

from .client import ApiClient


async def _call_endpoint(client: ApiClient, method: str, path_template: str, path_params: Dict[str, Any], query_params: Dict[str, Any]) -> Any:
    endpoint = path_template.format(**path_params)
    query_params = {k: v for k, v in query_params.items() if v is not None}
    if method.upper() == "GET":
        return await client.get(endpoint, query_params)
    return await client.post(endpoint, query_params)


def _create_function(name: str, description: str, method: str, path_template: str, path_param_names: List[str], query_param_names: List[str], mcp: FastMCP, client: ApiClient):
    async def func(**kwargs):
        path_params = {k: kwargs[k] for k in path_param_names}
        query_params = {k: kwargs.get(k) for k in query_param_names}
        return await _call_endpoint(client, method, path_template, path_params, query_params)

    func.__name__ = name
    func.__doc__ = description

    parameters = []
    for p in path_param_names:
        parameters.append(inspect.Parameter(p, inspect.Parameter.POSITIONAL_OR_KEYWORD))
    for p in query_param_names:
        parameters.append(inspect.Parameter(p, inspect.Parameter.POSITIONAL_OR_KEYWORD, default=None))
    func.__signature__ = inspect.Signature(parameters)

    decorated = mcp.tool()(func)
    return decorated


def register_catalog_endpoints(mcp: FastMCP, client: ApiClient, catalog_path: str = "laevitas_catalog.json") -> None:
    """Register all endpoints from the catalog as MCP tools."""
    with open(catalog_path, "r") as fh:
        catalog = json.load(fh)

    for entry in catalog.get("api_list", []):
        name = entry.get("methodName")
        description = entry.get("description", "")
        path_template = entry.get("path")
        method = entry.get("method", "GET")
        path_params = list(entry.get("path_params", {}).keys())
        query_params = list(entry.get("query_params", {}).keys())

        _create_function(name, description, method, path_template, path_params, query_params, mcp, client)
