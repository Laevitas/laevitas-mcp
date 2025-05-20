"""
Laevitas MCP Server
"""

import os
import json
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import httpx

# Load environment variables
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("laevitas")

# Load API key
LAEVITAS_API_KEY = os.getenv("LAEVITAS_API_KEY")
if not LAEVITAS_API_KEY:
    raise ValueError("LAEVITAS_API_KEY not found in environment variables")

# Base URL for Laevitas API
BASE_URL = "https://api.laevitas.ch"

# HTTP client
client = httpx.AsyncClient(
    base_url=BASE_URL,
    headers={"apiKey": LAEVITAS_API_KEY},
    timeout=30.0
)

async def make_request(method: str, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
    """Make a request to the Laevitas API."""
    try:
        response = await client.request(method, endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
async def getatmimpliedvolatilitytimelapse(market: str, currency: str) -> str:
    """ ATM Implied Volatility Time Lapse for a Specific Market and Currency
    
    Required parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    """
    # Build the endpoint path
    endpoint_path = "/analytics/options/atm_iv_ts/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {}
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getgexdataforalloptions(market: str, currency: str) -> str:
    """ GEX (Gamma Exposure) Data for All Options on a Specific Market and Currency
    
    Required parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    """
    # Build the endpoint path
    endpoint_path = "/analytics/options/gex_date_all/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {}
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionmaturities(market: str, currency: str) -> str:
    """ Option Maturities
    
    Required parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    """
    # Build the endpoint path
    endpoint_path = "/analytics/options/maturities/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {}
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsopeninterestbyexpiry(market: str, currency: str) -> str:
    """ Options Open Interest by Expiry
    
    Required parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    """
    # Build the endpoint path
    endpoint_path = "/analytics/options/oi_expiry/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {}
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsopeninterestbystrike(market: str, currency: str) -> str:
    """ Options Open Interest by Strike
    
    Required parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    """
    # Build the endpoint path
    endpoint_path = "/analytics/options/oi_strike_all/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {}
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsopeninterestbytype(market: str, currency: str) -> str:
    """ Options Open Interest by Type
    
    Required parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    """
    # Build the endpoint path
    endpoint_path = "/analytics/options/oi_type/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {}
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gettoptradedoptions(market: str, currency: str) -> str:
    """ Top Traded Options
    
    Required parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    """
    # Build the endpoint path
    endpoint_path = "/analytics/options/top_traded_option/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {}
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsvolumebyexpiry(market: str, currency: str) -> str:
    """
    Options Volume by Expiry
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - maturity: Expiry date
        - c: Volume of call options
        - p: Volume of put options
        - notional_c: Notional value of call options
        - notional_p: Notional value of put options
        - premium_c: Premium value of call options
        - premium_p: Premium value of put options
    """
    endpoint_path = f"/analytics/options/v_expiry/{market}/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsvolumebystrike(market: str, currency: str) -> str:
    """
    Options Volume by Strike
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - strike: Strike price
        - c: Volume of call options
        - p: Volume of put options
        - notional_c: Notional value of call options
        - notional_p: Notional value of put options
    """
    endpoint_path = f"/analytics/options/v_strike_all/{market}/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsvolumebysell(market: str, currency: str) -> str:
    """
    Options Volume by Buy/Sell
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - strike: Strike price
        - c_buy: Volume of call options bought
        - c_sell: Volume of call options sold
        - p_buy: Volume of put options bought
        - p_sell: Volume of put options sold
        - c_buy_premium: Premium paid for call options bought
        - c_sell_premium: Premium received from call options sold
        - p_buy_premium: Premium paid for put options bought
        - p_sell_premium: Premium received from put options sold
        - c_buy_notional: Notional value of call options bought
        - c_sell_notional: Notional value of call options sold
        - p_buy_notional: Notional value of put options bought
        - p_sell_notional: Notional value of put options sold
    """
    endpoint_path = f"/analytics/options/volume_buy_sell_all/{market}/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsgexbydate(market: str, currency: str, maturity: str) -> str:
    """
    Options GEX by Date
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    - maturity: Maturity date (e.g., '24DEC26')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - strike: Strike price
        - optionType: Option type ('call' or 'put')
        - gex: GEX value
    """
    endpoint_path = f"/analytics/options/gex_date/{market}/{currency}/{maturity}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsimpliedvolatilitybystrike(market: str, currency: str, strike: str) -> str:
    """
    Options Implied Volatility (IV) by Strike
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    - strike: Strike price (e.g., '10000')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - date: Date of IV data
        - iv: Implied volatility value
    """
    endpoint_path = f"/analytics/options/iv_strike/{market}/{currency}/{strike}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsopeninterestbystrike(market: str, currency: str, maturity: str) -> str:
    """
    Options Open Interest (OI) by Strike
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    - maturity: Maturity date (e.g., '24DEC26')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - strike: Strike price
        - c: Open interest for call options
        - p: Open interest for put options
        - notional_c: Notional value of call options
        - notional_p: Notional value of put options
        - premium_c: Premium value of call options
        - premium_p: Premium value of put options
        - intrinsic: Intrinsic value of options
    """
    endpoint_path = f"/analytics/options/oi_strike/{market}/{currency}/{maturity}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsopeninterestnetchangeforallstrikes(market: str, currency: str, hours: str) -> str:
    """
    Options Open Interest Net Change for All Strikes
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    - hours: Time period in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - strike: Strike price
        - C: Net change in open interest for call options
        - C_premium: Net change in premium value for call options
        - C_notional: Net change in notional value for call options
        - P: Net change in open interest for put options
        - P_premium: Net change in premium value for put options
        - P_notional: Net change in notional value for put options
    """
    endpoint_path = f"/analytics/options/oi_net_change_all/{market}/{currency}/{hours}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def gettopinstrumentswithoptionsopeninterestchange(market: str, currency: str, hours: str) -> str:
    """
    Top Instruments with Options Open Interest Change
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    - hours: Time period in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - open_interest: Current open interest
        - oi_change_notional: Net change in notional value
        - oi_change_premium: Net change in premium value
        - instrument: Instrument identifier
    """
    endpoint_path = f"/analytics/options/top_instrument_oi_change/{market}/{currency}/{hours}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsvolumebysellactivity(market: str, currency: str, maturity: str) -> str:
    """
    Options Volume by Buy/Sell Activity
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    - maturity: Maturity date (e.g., '24DEC26')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - strike: Strike price
        - c_buy: Volume of call options bought
        - c_sell: Volume of call options sold
        - p_buy: Volume of put options bought
        - p_sell: Volume of put options sold
        - c_buy_premium: Premium paid for call options bought
        - c_sell_premium: Premium received from call options sold
        - p_buy_premium: Premium paid for put options bought
        - p_sell_premium: Premium received from put options sold
        - c_buy_notional: Notional value of call options bought
        - c_sell_notional: Notional value of call options sold
        - p_buy_notional: Notional value of put options bought
        - p_sell_notional: Notional value of put options sold
    """
    endpoint_path = f"/analytics/options/volume_buy_sell/{market}/{currency}/{maturity}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptions24hvolumebystrike(market: str, currency: str, maturity: str) -> str:
    """
    Options 24h Volume By Strike
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    - maturity: Maturity date (e.g., '24DEC26')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - c: Volume of call options
        - p: Volume of put options
        - notional_c: Notional value of call options
        - notional_p: Notional value of put options
        - premium_c: Premium value of call options
        - premium_p: Premium value of put options
    """
    endpoint_path = f"/analytics/options/v_strike/{market}/{currency}/{maturity}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionstradesummary(market: str, currency: str, hours: str) -> str:
    """
    Options Trade Summary
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    - hours: Time period in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing trade summary details for different strategies
    """
    endpoint_path = f"/analytics/options/summary_trades/{market}/{currency}/{hours}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsgreeks(market: str, currency: str, maturity: str, type: str) -> str:
    """
    Options Greeks data
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    - maturity: Maturity date (e.g., '24DEC26')
    - type: Option type (e.g., 'C' for call)
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - strike: Strike price
        - underlying_price: Price of underlying asset
        - delta: Delta value
        - gamma: Gamma value
        - theta: Theta value
        - vega: Vega value
    """
    endpoint_path = f"/analytics/options/greeks/{market}/{currency}/{maturity}/{type}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsivall(market: str, currency: str, maturity: str, type: str) -> str:
    """
    Options IV data
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    - maturity: Maturity date (e.g., '24DEC26')
    - type: Option type (e.g., 'C' for call)
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - strike: Strike price
        - mark_iv: Mark implied volatility
        - bid_iv: Bid implied volatility
        - ask_iv: Ask implied volatility
        - delta: Delta value
    """
    endpoint_path = f"/analytics/options/iv_all/{market}/{currency}/{maturity}/{type}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getivtable(market: str, currency: str) -> str:
    """
    Implied Volatility Table
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing implied volatility data for different maturities
    """
    endpoint_path = f"/analytics/options/iv_table/{market}/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoinetchange(market: str, currency: str, maturity: str, hours: str) -> str:
    """
    Open Interest Net Change
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    - maturity: Maturity date (e.g., '24DEC26')
    - hours: Time period in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - strike: Strike price
        - C: Net change in open interest for call options
        - C_premium: Premium value of call options
        - C_notional: Notional value of call options
        - P: Net change in open interest for put options
        - P_premium: Premium value of put options
        - P_notional: Notional value of put options
    """
    endpoint_path = f"/analytics/options/oi_net_change/{market}/{currency}/{maturity}/{hours}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionssnapshot(market: str, currency: str) -> str:
    """
    Options Snapshot
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing detailed information about individual options contracts
    """
    endpoint_path = f"/analytics/options/snapshot/{market}/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsinstruments(option_type: Optional[str] = None, strike: Optional[str] = None, maturity: Optional[str] = None, currency: Optional[str] = None, market: Optional[str] = None) -> str:
    """
    Options Instruments List
    
    Optional query parameters:
    - option_type: Option type (e.g., 'C')
    - strike: Strike price
    - maturity: Maturity date (e.g., '24DEC26')
    - currency: Currency identifier (e.g., 'BTC')
    - market: Market identifier (e.g., 'DERIBIT')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - currency: Currency identifier
        - maturity: Maturity date
        - strike: Strike price
        - option_type: Option type
        - instrument: Instrument identifier
    """
    endpoint_path = "/analytics/options/Instruments"
    query_params = {}
    if option_type:
        query_params["option_type"] = option_type
    if strike:
        query_params["strike"] = strike
    if maturity:
        query_params["maturity"] = maturity
    if currency:
        query_params["currency"] = currency
    if market:
        query_params["market"] = market
    return await make_request("GET", endpoint_path, query_params)


@mcp.tool()
async def getoptionsoibreakdown() -> str:
    """
    Options Open Interest Breakdown
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing:
        - notional: Notional value breakdown by exchange
        - open_value: Open value breakdown by exchange
    """
    endpoint_path = "/analytics/options/oi_breakdown"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsvolumebreakdown() -> str:
    """
    Options Volume Breakdown
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing:
        - notional: Notional value breakdown by exchange
        - open_value: Open value breakdown by exchange
    """
    endpoint_path = "/analytics/options/volume_breakdown"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsoibreakdownbycurrency() -> str:
    """
    Options Open Interest Breakdown by Currency
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing:
        - notional: Notional value breakdown by currency
        - open_value: Open value breakdown by currency
    """
    endpoint_path = "/analytics/options/oi_breakdown_by_currency"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsvolumebreakdownbycurrency() -> str:
    """
    Options Volume Breakdown by Currency
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing:
        - notional: Notional value breakdown by currency
        - open_value: Open value breakdown by currency
    """
    endpoint_path = "/analytics/options/volume_breakdown_by_currency"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getexpiredoptionexpiries(market: str, currency: str, maturity: Optional[str] = None) -> str:
    """
    Expired Option Expiries
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    
    Optional query parameters:
    - maturity: Expired maturity date in DDMMYY format (e.g., '31DEC21')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - Date: Maturity date
        - Strike: Strike price
        - OptionType: Option type
        - mark_price: Mark price
        - mark_price_usd: Mark price in USD
        - position: Position value
        - index_price: Index price at expiry
    """
    endpoint_path = f"/analytics/options/expired_expiries/{market}/{currency}"
    query_params = {}
    if maturity:
        query_params["maturity"] = maturity
    return await make_request("GET", endpoint_path, query_params)


@mcp.tool()
async def get_customchange(name: str, market: str, currency: str, end: Optional[str] = None, start: Optional[str] = None) -> str:
    """
    Custom Change Data
    
    Required path parameters:
    - name: Data type identifier (e.g., 'atmivts_historical', 'heatmap_change')
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BTC')
    
    Optional query parameters:
    - end: End date in YYYY-MM-DD format (e.g., '2025-05-19')
    - start: Start date in YYYY-MM-DD format (e.g., '2025-05-12')
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing historical data with applied changes between start and end dates
    """
    endpoint_path = f"/analytics/options/custom_change/{name}/{market}/{currency}"
    query_params = {}
    if end:
        query_params["end"] = end
    if start:
        query_params["start"] = start
    return await make_request("GET", endpoint_path, query_params)


@mcp.tool()
async def getmodelskewcharts(currency: str, maturity: str, type: str) -> str:
    """
    Model Skew Charts
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - maturity: Maturity date in DDMMYY format (e.g., '24DEC26')
    - type: Chart type ('delta' or 'strike')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - delta/strike: Delta value or strike price
        - iv: Implied volatility value
    """
    endpoint_path = f"/analytics/options/model_charts/skew/{currency}/{maturity}/{type}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getmodelvolatilityruncharts(currency: str, maturity: str) -> str:
    """
    Model Volatility Run Charts
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - maturity: Maturity date in DDMMYY format (e.g., '24DEC26')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - expiry: Expiration date
        - forward: Forward price
        - atm_spot_iv: ATM spot implied volatility
        - skew_10d/15d/25d/35d: Skew values at different deltas
        - rr_10d/15d/25d/35d: Risk reversal values at different deltas
        - fly_10d/15d/25d/35d: Butterfly values at different deltas
    """
    endpoint_path = f"/analytics/options/model_charts/vol_run/{currency}/{maturity}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getmodelskewcharttimelapse(currency: str, maturity: str, type: str) -> str:
    """
    Model Skew Chart Time Lapse
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - maturity: Maturity date in DDMMYY format (e.g., '24DEC26')
    - type: Chart type ('delta' or 'strike')
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing time-lapse data for different periods:
        - Today/Yesterday/2 Days Ago/1 Week Ago/2 Weeks Ago/3 Weeks Ago/1 Month Ago
        Each period contains array of objects with:
        - delta/strike: Delta value or strike price
        - iv: Implied volatility value
    """
    endpoint_path = f"/analytics/options/model_charts/skew/{currency}/{maturity}/{type}/time_lapse"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getmodelforwardcurvechart(currency: str) -> str:
    """
    Model Forward Curve Chart
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - forward: Forward price
        - ttm: Time to maturity
    """
    endpoint_path = f"/analytics/options/model_charts/forward_curve/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getmodeltermstructureatmchart(currency: str) -> str:
    """
    Model Term Structure ATM Chart
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing:
        - tenor: Array of objects with ttm and iv values
        - expiry: Array of objects with expiry date and iv values
    """
    endpoint_path = f"/analytics/options/model_charts/term_structure_atm/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getmodeltermstructureatmcharttimelapse(currency: str) -> str:
    """
    Model Term Structure ATM Chart Time Lapse
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing time-lapse data for different periods:
        - Today/Yesterday/2 Days Ago/1 Week Ago/2 Weeks Ago/3 Weeks Ago/1 Month Ago
        Each period contains:
        - tenor: Array of objects with ttm and iv values
        - expiry: Array of objects with expiry date and iv values
    """
    endpoint_path = f"/analytics/options/model_charts/term_structure_atm/{currency}/time_lapse"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getmodeltermstructurechart(currency: str, type: str) -> str:
    """
    Model Term Structure Chart
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - type: Chart type ('delta' or 'strike')
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing:
        - delta/strike: Array of objects with expiry date and iv values
    """
    endpoint_path = f"/analytics/options/model_charts/term_structure/{currency}/{type}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsskewbycurrencyandmaturity(currency: str, maturity: str) -> str:
    """
    Options Skew by Currency and Maturity
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - maturity: Maturity date in DDMMYY format (e.g., '24DEC26')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - currency: Currency identifier
        - strike: Strike price
        - delta: Delta value
        - iv: Implied volatility value
    """
    endpoint_path = f"/analytics/options/skew_currency/{currency}/{maturity}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsskewbymarketandmaturity(market: str, maturity: str) -> str:
    """
    Options Skew by Market and Maturity
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - maturity: Maturity date in DDMMYY format (e.g., '24DEC26')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - currency: Currency identifier
        - strike: Strike price
        - delta: Delta value
        - iv: Implied volatility value
    """
    endpoint_path = f"/analytics/options/skew_market/{market}/{maturity}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsivbycurrency(currency: str) -> str:
    """
    Options IV by Currency
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - currency: Currency identifier
        - maturity: Maturity date
        - iv: Implied volatility value
    """
    endpoint_path = f"/analytics/options/iv_currency/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsivbymarket(market: str) -> str:
    """
    Options IV by Market
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - currency: Currency identifier
        - maturity: Maturity date
        - iv: Implied volatility value
    """
    endpoint_path = f"/analytics/options/iv_market/{market}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getethbtcatmivtermstructure() -> str:
    """
    ETH-BTC ATM IV Term Structure
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing time-lapse data for different periods:
        - Today/Yesterday/2 Days Ago/1 Week Ago/2 Weeks Ago/3 Weeks Ago/1 Month Ago
        Each period contains:
        - maturity: Maturity date of the option contract
        - iv: At-the-money implied volatility value
    """
    endpoint_path = "/analytics/options/eth-btc_atm_iv_term_structure"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoptionsskewbymarketandcurrency(market: str, currency: str) -> str:
    """
    Options Skew by Market and Currency
    
    Required path parameters:
    - market: Market identifier (e.g., 'deribit')
    - currency: Currency identifier (e.g., 'BNB')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - currency: Currency identifier
        - strike: Strike price
        - delta: Delta value
        - iv: Implied volatility value
    """
    endpoint_path = f"/analytics/options/skew/{market}/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getoichangebystrike(currency: str, market: str, date_range: Optional[str] = None, maturity: Optional[str] = None, min_strike: Optional[str] = None, max_strike: Optional[str] = None) -> str:
    """
    Open Interest Change by Strike
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - market: Market identifier (e.g., 'Deribit')
    
    Optional query parameters:
    - date_range: Date range in hours (e.g., '24')
    - maturity: Maturity period (e.g., 'all')
    - min_strike: Minimum strike price (e.g., '40000')
    - max_strike: Maximum strike price (e.g., '50000')
    
    Returns:
    - Array of objects containing:
        - date: Timestamp in milliseconds
        - strike: Strike price
        - open_interest: Open interest value
        - total_notional_change: Total notional change
        - open_interest_change: Change in open interest
        - open_interest_change_percent: Percentage change in open interest
        - strike_index: Strike price index
        - date_index: Date index
        - intensity: Intensity of open interest change
    """
    endpoint_path = f"/analytics/options/options_strategy/oi_change_by_strike/{currency}/{market}"
    query_params = {}
    if date_range:
        query_params["date_range"] = date_range
    if maturity:
        query_params["maturity"] = maturity
    if min_strike:
        query_params["min_strike"] = min_strike
    if max_strike:
        query_params["max_strike"] = max_strike
    return await make_request("GET", endpoint_path, query_params)


@mcp.tool()
async def gettopoptionsstrategies(currency: str, hours_interval: str, single_trade: str) -> str:
    """
    Top Options Strategies
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - hours_interval: Interval in hours (e.g., '24')
    - single_trade: Single trade indicator (true/false or 1/0)
    
    Returns:
    - Array of objects containing:
        - date: Timestamp in milliseconds
        - oi_change: Change in open interest
        - iv: Implied volatility
        - amount: Strategy amount
        - index_price: Current index price
        - instrument_name: Options instrument name
        - maturity: Maturity date
        - strike: Strike price
        - direction: Trade direction (buy/sell)
        - total_notional: Total notional value
        - total_premium: Total premium
        - total_premium_usd: Total premium in USD
        - strategy_name: Strategy name
        - block_trade_id: Block trade identifier
        - level: Trade level relative to bid
        - mark_price: Mark price
        - ask_price: Ask price
        - bid_price: Bid price
        - ask_size: Ask size
        - bid_size: Bid size
        - delta: Delta value
        - gamma: Gamma value
        - vega: Vega value
        - theta: Theta value
    """
    endpoint_path = f"/analytics/options/options_strategy/top_options_strategies/{currency}/{hours_interval}/{single_trade}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getstrategylegbubblechart(currency: str, strategy: Optional[str] = None, maturity: Optional[str] = None, hours_interval: Optional[str] = None, size_filter: Optional[str] = None, single_trade: Optional[str] = None) -> str:
    """
    Strategy Leg Bubble Chart
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Optional query parameters:
    - strategy: Trading strategy (e.g., 'all')
    - maturity: Maturity period (e.g., 'all')
    - hours_interval: Interval in hours (e.g., '24')
    - size_filter: Size filter value (e.g., '0')
    - single_trade: Single trade indicator (true/false or 1/0)
    
    Returns:
    - Array of objects containing:
        - date: Timestamp in milliseconds
        - oi_change: Change in open interest
        - iv: Implied volatility
        - amount: Strategy amount
        - index_price: Current index price
        - instrument_name: Options instrument name
        - maturity: Maturity date
        - strike: Strike price
        - direction: Trade direction (buy/sell)
        - total_notional: Total notional value
        - total_premium: Total premium
        - total_premium_usd: Total premium in USD
        - strategy_name: Strategy name
        - block_trade_id: Block trade identifier
        - level: Trade level relative to bid
        - mark_price: Mark price
        - ask_price: Ask price
        - bid_price: Bid price
        - ask_size: Ask size
        - bid_size: Bid size
        - delta: Delta value
        - gamma: Gamma value
        - vega: Vega value
        - theta: Theta value
    """
    endpoint_path = f"/analytics/options/options_strategy/strategy_leg_bubble_chart/{currency}"
    query_params = {}
    if strategy:
        query_params["strategy"] = strategy
    if maturity:
        query_params["maturity"] = maturity
    if hours_interval:
        query_params["hours_interval"] = hours_interval
    if size_filter:
        query_params["size_filter"] = size_filter
    if single_trade:
        query_params["single_trade"] = single_trade
    return await make_request("GET", endpoint_path, query_params)


@mcp.tool()
async def getopeninterestchangesummary(currency: str, period: str) -> str:
    """
    Open Interest Change Summary
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - period: Change period in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - markets: Array of market names
        - ticker: Ticker symbol
        - open_interest: Total open interest value
        - open_interest_notional: Notional value of open interest
        - open_interest_change_usd: Change in open interest in USD
        - open_interest_notional_change: Change in notional value
    """
    endpoint_path = f"/analytics/options/open_interest_change_summary/{currency}/{period}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getopeninterestchange(market: str, currency: str, period: str) -> str:
    """
    Open Interest Change
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - currency: Currency identifier (e.g., 'BTC')
    - period: Change period in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - symbol: Ticker symbol
        - open_interest: Total open interest value
        - open_interest_notional: Notional value of open interest
        - open_interest_change_usd: Change in open interest in USD
        - open_interest_notional_change: Change in notional value
    """
    endpoint_path = f"/analytics/options/open_interest_change/{market}/{currency}/{period}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getanalyticoptionsorbitaltvol(currency: str) -> str:
    """
    Options Orbit Alternative Volatility
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'AAVE')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - 10D FLY: 10-day volatility fly
        - 10D RR: 10-day risk reversal
        - 25D FLY: 25-day volatility fly
        - 25D RR: 25-day risk reversal
        - ATM: At-the-money volatility
        - tenor: Tenor value
    """
    endpoint_path = f"/analytics/options/orbit_alt_vol/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getfuturesinstrumentdata() -> str:
    """
    Futures Instrument Data
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - type: Instrument type
        - currency: Currency identifier
        - instrument: Instrument name/identifier
        - expiry: Expiry date
    """
    endpoint_path = "/analytics/futures/instruments"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getalternativecurrencydata() -> str:
    """
    Alternative Currency Data
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of alternative currency identifiers
    """
    endpoint_path = "/analytics/futures/alt_currency"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getperpetualfundingdata(currency: str) -> str:
    """
    Perpetual Funding Data
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - symbol: Contract symbol
        - funding: Funding rate
        - yield: Yield value
        - next_fr: Next funding rate
    """
    endpoint_path = f"/analytics/futures/perpetual_funding/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getfuturesyielddata(currency: str) -> str:
    """
    Futures Yield Data
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - maturity: Maturity date
        - value: Yield value
    """
    endpoint_path = f"/analytics/futures/futures_yield/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getfuturesbasisdata(currency: str) -> str:
    """
    Futures Basis Data
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - maturity: Maturity date
        - value: Basis value
    """
    endpoint_path = f"/analytics/futures/futures_basis/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getfuturescurvedata(currency: str, market: str) -> str:
    """
    Futures Curve Data for Currency and Market
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - market: Market identifier (e.g., 'DERIBIT')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - maturity: Maturity date
        - value: Curve value
    """
    endpoint_path = f"/analytics/futures/futures_curve/{currency}/{market}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getfuturescurvedataforcurrency(currency: str) -> str:
    """
    Futures Curve Data for Currency
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - maturity: Maturity date
        - value: Curve value
    """
    endpoint_path = f"/analytics/futures/futures_curve/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getopeninterestgainersandlosersforfuturesmarkets(currency: str, option: str, param: str) -> str:
    """
    Open Interest Gainers and Losers for Futures Markets
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - option: Option type (e.g., 'all')
    - param: Change interval in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - open_interest_change: Change in open interest
        - open_interest_change_perc: Percentage change in open interest
        - open_interest_notional_change: Change in notional open interest
        - open_interest_notional_change_perc: Percentage change in notional open interest
    """
    endpoint_path = f"/analytics/futures/markets_oi_gainers_and_losers/{currency}/{option}/{param}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getfuturesmarketsnapshot(market: str) -> str:
    """
    Futures Market Snapshot
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing market data with keys as market symbols and values as objects with:
        - expiration_date: Contract expiration date
        - bid: Bid price
        - bid_amount: Bid amount
        - ask: Ask price
        - ask_amount: Ask amount
        - volume: Trading volume
        - volume_usd: Trading volume in USD
        - open_interest: Open interest
        - datetime: Data collection timestamp
        - underlyer: Underlying asset
        - basis: Basis value
        - underlyer_spot: Spot price of underlying
    """
    endpoint_path = f"/analytics/futures/snapshot/{market}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getperpetualfundingdatawithtype(currency: str, type: str) -> str:
    """
    Perpetual Funding Data with Type
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - type: Market type (e.g., 'c' for Centralized)
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - symbol: Contract symbol
        - funding: Funding rate
        - yield: Yield value
        - next_fr: Next funding rate
    """
    endpoint_path = f"/analytics/futures/perpetual_funding/{currency}/{type}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getopeninterestbreakdowndata(currency: str, type: str) -> str:
    """
    Open Interest Breakdown Data
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - type: Market type (e.g., 'c' for Centralized)
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing:
        - all: Open interest for all types
            - usd: USD values by market
            - notional: Notional values by market
        - future: Open interest for futures
            - usd: USD values by market
            - notional: Notional values by market
        - perpetual: Open interest for perpetuals
            - usd: USD values by market
            - notional: Notional values by market
    """
    endpoint_path = f"/analytics/futures/oi_breakdown/{currency}/{type}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getvolumebreakdowndata(currency: str, type: str) -> str:
    """
    Volume Breakdown Data
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - type: Market type (e.g., 'c' for Centralized)
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing:
        - all: Volume for all types
            - usd: USD values by market
            - notional: Notional values by market
        - future: Volume for futures
            - usd: USD values by market
            - notional: Notional values by market
        - perpetual: Volume for perpetuals
            - usd: USD values by market
            - notional: Notional values by market
    """
    endpoint_path = f"/analytics/futures/volume_breakdown/{currency}/{type}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getopeninterestgainersandlosersdata(currency: str, option: str, param: str, type: str) -> str:
    """
    Open Interest Gainers and Losers Data
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - option: Option type (e.g., 'all')
    - param: Change interval in hours (e.g., '1')
    - type: Market type (e.g., 'c' for Centralized)
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - open_interest_change: Change in open interest
        - open_interest_change_perc: Percentage change in open interest
        - open_interest_notional_change: Change in notional open interest
        - open_interest_notional_change_perc: Percentage change in notional open interest
    """
    endpoint_path = f"/analytics/futures/markets_oi_gainers_and_losers/{currency}/{option}/{param}/{type}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getaggregatedfuturesummarydata(currency: str) -> str:
    """
    Aggregated Future Summary Data
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - symbol: Future symbol
        - currency: Currency identifier
        - expiry: Expiry date
        - price: Price value
        - open_interest: Open interest value
        - open_interest_notional: Notional open interest
        - volume: Volume value
        - volume_notional: Notional volume
        - yield: Yield value
        - basis: Basis value
        - open_interest_volume: Open interest volume
        - markets: Array of market identifiers
    """
    endpoint_path = f"/analytics/futures/aggregated_future_summary/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getaggregatedoptionsummarydata(currency: str) -> str:
    """
    Aggregated Option Summary Data
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - symbol: Option symbol
        - currency: Currency identifier
        - expiry: Expiry date
        - price: Price value
        - open_interest: Open interest value
        - open_interest_notional: Notional open interest
        - volume: Volume value
        - volume_notional: Notional volume
        - yield: Yield value
        - basis: Basis value
        - open_interest_volume: Open interest volume
        - markets: Array of market identifiers
    """
    endpoint_path = f"/analytics/futures/aggregated_option_summary/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getfutureopeninterestchangesummary(currency: str, period: str) -> str:
    """
    Future Open Interest Change Summary
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - period: Change period in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - markets: Array of market identifiers
        - ticker: Ticker symbol
        - open_interest: Total open interest
        - open_interest_notional: Notional open interest
        - open_interest_change_usd: Change in USD
        - open_interest_notional_change: Change in notional value
    """
    endpoint_path = f"/analytics/futures/open_interest_change_summary/{currency}/{period}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getfutureopeninterestchange(market: str, currency: str, period: str) -> str:
    """
    Future Open Interest Change
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - currency: Currency identifier (e.g., 'BTC')
    - period: Change period in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - symbol: Ticker symbol
        - open_interest: Total open interest
        - open_interest_notional: Notional open interest
        - open_interest_change_usd: Change in USD
        - open_interest_notional_change: Change in notional value
    """
    endpoint_path = f"/analytics/futures/open_interest_change/{market}/{currency}/{period}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def get_futures(market: str, currency: str, maturity: str) -> str:
    """
    Futures Live Data
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - currency: Currency identifier (e.g., 'BTC')
    - maturity: Maturity date (e.g., '29DEC23')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - symbol: Contract symbol
        - base_currency: Base currency
        - margin: Margin type
        - index_price: Index price
        - price: Current price
        - basis: Basis value
        - apy: Annual percentage yield
        - open_interest: Open interest
        - open_interest_coin: Open interest in coin
        - oi_volume24h: 24h open interest volume
        - volume24h: 24h trading volume
        - volume24h_coin: 24h trading volume in coin
        - bid: Bid price
        - ask: Ask price
        - bid_amount: Bid amount
        - ask_amount: Ask amount
        - liquidations: Object containing:
            - short: Short liquidations
            - long: Long liquidations
    """
    endpoint_path = f"/analytics/derivs/futures/{market}/{currency}/{maturity}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def get_perpetuals(market: str, currency: str) -> str:
    """
    Perpetual Swaps Live Data
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - symbol: Contract symbol
        - base_currency: Base currency
        - margin: Margin type
        - market_cap: Market capitalization
        - index_price: Index price
        - price: Current price
        - basis: Basis value
        - funding: Current funding rate
        - next_funding: Next funding rate
        - apy: Annual percentage yield
        - open_interest: Open interest
        - open_interest_coin: Open interest in coin
        - oi_volume24h: 24h open interest volume
        - volume24h: 24h trading volume
        - volume24h_coin: 24h trading volume in coin
        - bid: Bid price
        - ask: Ask price
        - bid_amount: Bid amount
        - ask_amount: Ask amount
        - liquidations: Object containing:
            - short: Short liquidations
            - long: Long liquidations
        - long_short_ratio: Long/short ratio
        - realized_vol: Object containing realized volatility for different periods
        - avg_apr: Object containing average APR for different periods
    """
    endpoint_path = f"/analytics/derivs/perpetuals/{market}/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def get_summary_c(currency: str) -> str:
    """
    Aggregated Perps Summary for Currency
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - currency: Currency identifier
        - price: Current price
        - change: Price change
        - market_cap: Market capitalization
        - realized_vol: Realized volatility
        - open_interest: Open interest
        - open_interest_notional: Notional open interest
        - volume: Trading volume
        - oi_volume_24h: 24h open interest volume
        - markets: Array of market identifiers
        - funding: Funding rate
        - yield: Yield value
    """
    endpoint_path = f"/analytics/derivs/summary/{currency}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def get_summary() -> str:
    """
    Aggregated Perps Summary for All Currencies
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - currency: Currency identifier
        - price: Current price
        - change: Price change
        - market_cap: Market capitalization
        - realized_vol: Realized volatility
        - open_interest: Open interest
        - open_interest_notional: Notional open interest
        - volume: Trading volume
        - oi_volume_24h: 24h open interest volume
        - markets: Array of market identifiers
        - funding: Funding rate
        - yield: Yield value
    """
    endpoint_path = "/analytics/derivs/summary"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def get_oi_gainers(market: str, type: str, period: str) -> str:
    """
    Open Interest Gainers
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - type: Type of instrument (e.g., 'future')
    - period: Change interval in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - symbol: Contract symbol
        - open_interest_change: Change in open interest
        - open_interest_change_notional: Change in notional open interest
        - open_interest_change_percentage: Percentage change in open interest
    """
    endpoint_path = f"/analytics/derivs/oi_gainers/{market}/{type}/{period}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def get_price_gainers(market: str, type: str, period: str) -> str:
    """
    Price Gainers
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - type: Type of instrument (e.g., 'future')
    - period: Change interval in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - symbol: Contract symbol
        - priceChange: Price change value
    """
    endpoint_path = f"/analytics/derivs/price_gainers/{market}/{type}/{period}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getperpetualssnapshotdatabymarket(market: str) -> str:
    """
    Perpetuals Snapshot Data by Market
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    
    Returns:
    - date: Timestamp of data collection
    - data: Object containing perpetual contract data with keys as contract symbols and values as objects with:
        - bid: Bid price
        - bid_amount: Bid amount
        - ask: Ask price
        - ask_amount: Ask amount
        - volume: Trading volume
        - volume_usd: Trading volume in USD
        - open_interest: Open interest
        - datetime: Data collection timestamp
        - underlyer: Underlying asset
        - underlyer_spot: Spot price of underlying
        - basis: Basis value
        - fr: Current funding rate
        - next_fr: Next funding rate
    """
    endpoint_path = f"/analytics/derivs/perpetuals_snapshot/{market}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getperpetualsdatabymarket(market: str) -> str:
    """
    Perpetuals Data by Market
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - symbol: Contract symbol
        - base_currency: Base currency
        - margin: Margin type
        - market_cap: Market capitalization
        - index_price: Index price
        - price: Current price
        - basis: Basis value
        - funding: Current funding rate
        - next_funding: Next funding rate
        - apy: Annual percentage yield
        - open_interest: Open interest
        - open_interest_coin: Open interest in coin
        - oi_volume24h: 24h open interest volume
        - volume24h: 24h trading volume
        - volume24h_coin: 24h trading volume in coin
        - bid: Bid price
        - ask: Ask price
        - bid_amount: Bid amount
        - ask_amount: Ask amount
        - liquidations: Object containing:
            - short: Short liquidations
            - long: Long liquidations
        - long_short_ratio: Long/short ratio
        - realized_vol: Object containing realized volatility for different periods
        - avg_apr: Object containing average APR for different periods
    """
    endpoint_path = f"/analytics/derivs/perpetuals/{market}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getfuturesdatabymarket(market: str) -> str:
    """
    Futures Data by Market
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - symbol: Contract symbol
        - base_currency: Base currency
        - margin: Margin type
        - index_price: Index price
        - price: Current price
        - basis: Basis value
        - apy: Annual percentage yield
        - open_interest: Open interest
        - open_interest_coin: Open interest in coin
        - oi_volume24h: 24h open interest volume
        - volume24h: 24h trading volume
        - volume24h_coin: 24h trading volume in coin
        - bid: Bid price
        - ask: Ask price
        - bid_amount: Bid amount
        - ask_amount: Ask amount
        - liquidations: Object containing:
            - short: Short liquidations
            - long: Long liquidations
    """
    endpoint_path = f"/analytics/derivs/futures/{market}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getaltoptiondatabymarket(market: str) -> str:
    """
    Alternative Options Data by Market
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - market: Market identifier
        - symbol: Contract symbol
        - margin: Margin type
        - index_price: Index price
        - underlying_price: Underlying asset price
        - atm_vol: At-the-money volatility
        - _25_delta_risk_reversal: 25-delta risk reversal
        - _25_delta_butterfly: 25-delta butterfly
        - open_interest: Open interest
        - open_interest_notional: Notional open interest
        - volume24h_call: 24h call volume
        - volume24h_call_notional: 24h call volume notional
        - volume24h_put: 24h put volume
        - volume24h_put_notional: 24h put volume notional
        - volume24h: 24h total volume
        - volume24h_notional: 24h total volume notional
        - basis: Basis value
        - expiry: Expiry date
    """
    endpoint_path = f"/analytics/derivs/alt_option/{market}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def gettopfundingdata(market: str) -> str:
    """
    Top Funding Data by Market
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - symbol: Contract symbol
        - funding: Funding rate
        - yield: Yield value
    """
    endpoint_path = f"/analytics/derivs/top_funding/{market}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getderivsopeninterestchangesummary(currency: str, period: str) -> str:
    """
    Perpetual Open Interest Change Summary
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    - period: Change period in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - markets: Array of market identifiers
        - open_interest: Total open interest
        - open_interest_notional: Notional open interest
        - open_interest_change_usd_percentage: Percentage change in USD
        - open_interest_change_usd: Change in USD
        - open_interest_notional_change_usd_percentage: Percentage change in notional USD
        - open_interest_notional_change_usd: Change in notional USD
    """
    endpoint_path = f"/analytics/derivs/perpetual/open_interest_change_summary/{currency}/{period}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def getderivsopeninterestchange(market: str, currency: str, period: str) -> str:
    """
    Perpetual Open Interest Change
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - currency: Currency identifier (e.g., 'BTC')
    - period: Change period in hours (e.g., '1')
    
    Returns:
    - date: Timestamp of data collection
    - data: Array of objects containing:
        - symbol: Contract symbol
        - open_interest: Total open interest
        - open_interest_notional: Notional open interest
        - open_interest_change_usd: Change in USD
        - open_interest_notional_change: Change in notional value
    """
    endpoint_path = f"/analytics/derivs/perpetual/open_interest_change/{market}/{currency}/{period}"
    return await make_request("GET", endpoint_path)


@mcp.tool()
async def gethistoricalderivssnapshot(market: str, currency: str, start: str, end: str, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """
    Historical Derivatives Snapshot Data
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - currency: Currency identifier (e.g., 'BTC')
    
    Required query parameters:
    - start: Start date of search range (e.g., '2025-05-12', '2025-05-12T10:15', '1747011600000')
    - end: End date of search range (e.g., '2025-05-19', '2025-05-19T10:15', '1747618500000')
    
    Optional query parameters:
    - limit: Maximum number of results per page (max 144)
    - page: Page number to return (each page = 1 minute of data)
    - granularity: Interval between dates ('5m', '15m', '30m', '1h', '2h', '4h', '6h', '12h', '1d')
    
    Returns:
    - meta: Object containing pagination info:
        - total: Total number of minutes in time range
        - page: Current page number
        - items: Number of items on current page
        - total_pages: Total number of pages
    - items: Array of objects containing:
        - date: Data recording timestamp
        - volume: Trading volume
        - volume_usd: Trading volume in USD
        - underlyer: Underlying asset
        - bid: Bid price
        - bid_amount: Amount at bid price
        - ask: Ask price
        - ask_amount: Amount at ask price
        - underlyer_spot: Spot price of underlying
        - next_fr: Next funding rate
        - basis: Basis point
        - datetime: Precise recording time
        - fr: Current funding rate
        - open_interest: Total open interest
        - instrument_name: Derivative instrument name
    """
    endpoint_path = f"/historical/derivs/snapshot/{market}/{currency}"
    query_params = {
        "start": start,
        "end": end,
        "limit": limit,
        "page": page,
        "granularity": granularity
    }
    return await make_request("GET", endpoint_path, query_params)

@mcp.tool()
async def getderivativesliquidationdata(market: str, symbol: str, start: str, end: str, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """
    Historical Contract Liquidations
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - symbol: Symbol identifier (e.g., 'BTC_USDC-PERPETUAL')
    
    Required query parameters:
    - start: Start date of search range (e.g., '2025-05-12', '2025-05-12T10:15', '1747011600000')
    - end: End date of search range (e.g., '2025-05-19', '2025-05-19T10:15', '1747618500000')
    
    Optional query parameters:
    - limit: Maximum number of results per page (max 144)
    - page: Page number to return
    - granularity: Interval between dates ('5m', '15m', '30m', '1h', '2h', '4h', '6h', '12h', '1d')
    
    Returns:
    - meta: Object containing pagination info:
        - total: Total number of items
        - page: Current page number
        - items: Number of items on current page
        - total_pages: Total number of pages
    - items: Array of objects containing:
        - date: Data recording timestamp
        - side: Trade side (long/short)
        - usd_amount: Trading volume in USD
    """
    endpoint_path = f"/historical/derivs/liquidation/{market}/{symbol}"
    query_params = {
        "start": start,
        "end": end,
        "limit": limit,
        "page": page,
        "granularity": granularity
    }
    return await make_request("GET", endpoint_path, query_params)

@mcp.tool()
async def getderivativesliquidationbycurrencydata(market: str, currency: str, start: str, end: str, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """
    Historical Contract Liquidations by Currency
    
    Required path parameters:
    - market: Market identifier (e.g., 'AGGREGATED')
    - currency: Currency identifier (e.g., 'BTC')
    
    Required query parameters:
    - start: Start date of search range (e.g., '2025-05-12', '2025-05-12T10:15', '1747011600000')
    - end: End date of search range (e.g., '2025-05-19', '2025-05-19T10:15', '1747618500000')
    
    Optional query parameters:
    - limit: Maximum number of results per page (max 144)
    - page: Page number to return
    - granularity: Interval between dates ('5m', '15m', '30m', '1h', '2h', '4h', '6h', '12h', '1d')
    
    Returns:
    - meta: Object containing pagination info:
        - total: Total number of items
        - page: Current page number
        - items: Number of items on current page
        - total_pages: Total number of pages
    - items: Array of objects containing:
        - date: Data recording timestamp
        - side: Trade side (long/short)
        - usd_amount: Trading volume in USD
    """
    endpoint_path = f"/historical/derivs/liquidation_by_currency/{market}/{currency}"
    query_params = {
        "start": start,
        "end": end,
        "limit": limit,
        "page": page,
        "granularity": granularity
    }
    return await make_request("GET", endpoint_path, query_params)

@mcp.tool()
async def gethistoricalderivssummary(currency: str, start: str, end: str, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """
    Historical Derivatives Summary
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Required query parameters:
    - start: Start date of search range (e.g., '2025-05-12', '2025-05-12T10:15', '1747011600000')
    - end: End date of search range (e.g., '2025-05-19', '2025-05-19T10:15', '1747618500000')
    
    Optional query parameters:
    - limit: Maximum number of results per page (max 144)
    - page: Page number to return
    - granularity: Interval between dates ('5m', '15m', '30m', '1h', '2h', '4h', '6h', '12h', '1d')
    
    Returns:
    - meta: Object containing pagination info:
        - total: Total number of items
        - page: Current page number
        - items: Number of items on current page
        - total_pages: Total number of pages
    - items: Array of objects containing:
        - date: Data recording timestamp
        - price: Contract price
        - open_interest: Total open interest
        - volume: Trading volume
        - funding: Funding rate
        - next_fr: Next funding rate
        - yield: Contract yield
        - liquidations_long: Long position liquidations
        - liquidations_short: Short position liquidations
        - market_cap: Market capitalization
        - oi_volume24h: 24h open interest volume
    """
    endpoint_path = f"/historical/derivs/summary/{currency}"
    query_params = {
        "start": start,
        "end": end,
        "limit": limit,
        "page": page,
        "granularity": granularity
    }
    return await make_request("GET", endpoint_path, query_params)

@mcp.tool()
async def gettotalvolumeforperpetuals(start: str, end: str, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """
    Total Trading Volume for Perpetuals
    
    Required query parameters:
    - start: Start date of search range (e.g., '2025-05-12', '2025-05-12T10:15', '1747011600000')
    - end: End date of search range (e.g., '2025-05-19', '2025-05-19T10:15', '1747618500000')
    
    Optional query parameters:
    - limit: Maximum number of results per page (max 144)
    - page: Page number to return
    - granularity: Interval between dates ('5m', '15m', '30m', '1h', '2h', '4h', '6h', '12h', '1d')
    - legacy: Use old endpoint logic ('true'/'false')
    
    Returns:
    - meta: Object containing pagination info:
        - total: Total number of items
        - page: Current page number
        - items: Number of items on current page
        - total_pages: Total number of pages
    - items: Array of objects containing:
        - date: Data recording timestamp
        - BTC: Total Bitcoin perpetual volume
        - ETH: Total Ethereum perpetual volume
        - Other: Total other perpetual volume
    """
    endpoint_path = "/historical/derivs/perpetual/total_volume_by_currency"
    query_params = {
        "start": start,
        "end": end,
        "limit": limit,
        "page": page,
        "granularity": granularity,
        "legacy": legacy
    }
    return await make_request("GET", endpoint_path, query_params)

@mcp.tool()
async def gettotaloiforperpetuals(start: str, end: str, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """
    Total Open Interest for Perpetuals
    
    Required query parameters:
    - start: Start date of search range (e.g., '2025-05-12', '2025-05-12T10:15', '1747011600000')
    - end: End date of search range (e.g., '2025-05-19', '2025-05-19T10:15', '1747618500000')
    
    Optional query parameters:
    - limit: Maximum number of results per page (max 144)
    - page: Page number to return
    - granularity: Interval between dates ('5m', '15m', '30m', '1h', '2h', '4h', '6h', '12h', '1d')
    - legacy: Use old endpoint logic ('true'/'false')
    
    Returns:
    - meta: Object containing pagination info:
        - total: Total number of items
        - page: Current page number
        - items: Number of items on current page
        - total_pages: Total number of pages
    - items: Array of objects containing:
        - date: Data recording timestamp
        - BTC: Total Bitcoin perpetual open interest
        - ETH: Total Ethereum perpetual open interest
        - Other: Total other perpetual open interest
    """
    endpoint_path = "/historical/derivs/perpetual/total_open_interest_by_currency"
    query_params = {
        "start": start,
        "end": end,
        "limit": limit,
        "page": page,
        "granularity": granularity,
        "legacy": legacy
    }
    return await make_request("GET", endpoint_path, query_params)

@mcp.tool()
async def gethistoricalfuturesdata(market: str, symbol: str, start: str, end: str, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """
    Historical Futures Data
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - symbol: Symbol identifier (e.g., 'BTC-26SEP25')
    
    Required query parameters:
    - start: Start date of search range (e.g., '2025-05-12', '2025-05-12T10:15', '1747011600000')
    - end: End date of search range (e.g., '2025-05-19', '2025-05-19T10:15', '1747618500000')
    
    Optional query parameters:
    - limit: Maximum number of results per page (max 144)
    - page: Page number to return
    - granularity: Interval between dates ('5m', '15m', '30m', '1h', '2h', '4h', '6h', '12h', '1d')
    
    Returns:
    - meta: Object containing pagination info:
        - total: Total number of items
        - page: Current page number
        - items: Number of items on current page
        - total_pages: Total number of pages
    - items: Array of objects containing:
        - date: Data recording timestamp
        - expiry: Contract expiry date
        - price: Contract price
        - index: Index value
        - basis: Basis point
        - yield: Contract yield
        - volume: Trading volume
        - open_interest: Total open interest
        - oi_volume24h: 24h open interest volume
    """
    endpoint_path = f"/historical/derivs/futures/{market}/{symbol}"
    query_params = {
        "start": start,
        "end": end,
        "limit": limit,
        "page": page,
        "granularity": granularity
    }
    return await make_request("GET", endpoint_path, query_params)

@mcp.tool()
async def gethistoricalperpetualderivativesdata(market: str, symbol: str, start: str, end: str, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """
    Historical Perpetual Derivatives Data
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - symbol: Symbol identifier (e.g., 'BTC-PERPETUAL')
    
    Required query parameters:
    - start: Start date of search range (e.g., '2025-05-12', '2025-05-12T10:15', '1747011600000')
    - end: End date of search range (e.g., '2025-05-19', '2025-05-19T10:15', '1747618500000')
    
    Optional query parameters:
    - limit: Maximum number of results per page (max 144)
    - page: Page number to return
    - granularity: Interval between dates ('5m', '15m', '30m', '1h', '2h', '4h', '6h', '12h', '1d')
    
    Returns:
    - meta: Object containing pagination info:
        - total: Total number of items
        - page: Current page number
        - items: Number of items on current page
        - total_pages: Total number of pages
    - items: Array of objects containing:
        - date: Data recording timestamp
        - price: Contract price
        - index: Index value
        - basis: Basis point
        - funding: Funding rate
        - yield: Contract yield
        - volume: Trading volume
        - open_interest: Total open interest
        - oi_volume24h: 24h open interest volume
        - long_short_ratio: Long/short ratio
        - next_funding: Next funding rate
    """
    endpoint_path = f"/historical/derivs/perpetuals/{market}/{symbol}"
    query_params = {
        "start": start,
        "end": end,
        "limit": limit,
        "page": page,
        "granularity": granularity
    }
    return await make_request("GET", endpoint_path, query_params)


@mcp.tool()
async def get_calculateriskslide(market: str, currency: str, instrument: Optional[str] = None) -> str:
    """Calculates the risk slide for a given instrument in the specified market and currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    instrument: ['BTC-26SEP25-110000-C', 'XRP-31JAN25-2.5-C', 'SOL-31JAN25-245-C', 'BNB-31JAN25-760-C', 'ETH-26SEP25-4000-C', 'PAXG-27JUN25-2720-C', 'DOGE-27DEC24-0.304-C', 'XRP-27DEC24-2.12-C', 'SOL-27DEC24-240-C', 'BNB-3JAN25-630-C', 'ETH-26SEP25-3200-C', 'BTC-26SEP25-80000-C', 'XRP-3JAN25-2.3-C', 'NEAR-31JAN25-6-C', 'FIL-31JAN25-6.5-C', 'TON-31JAN25-6.4-C', 'SOL-3JAN25-200-C', 'BCH-31JAN25-500-C', 'ETH-28MAR25-4200-C', 'BTC-28MAR25-102000-C', 'ETH-26SEP25-4600-C', 'BTC-26SEP25-120000-C', 'DOGE-31JAN25-0.365-C', 'KAS-31JAN25-0.145-C', 'XRP-31JAN25-2.38-C', 'TON-31JAN25-5.9-C', 'FIL-31JAN25-6.4-C', 'NEAR-31JAN25-6.6-C', 'ICP-31JAN25-12.25-C', 'LINK-31JAN25-27.6-C', 'ORDI-31JAN25-30-C', 'SOL-31JAN25-190-C', 'BCH-31JAN25-535-C', 'BNB-31JAN25-710-C', 'ETH-26SEP25-4000-C', 'BTC-26SEP25-110000-C', 'ETH-26SEP25-6000-C', 'BTC-26SEP25-95000-C']
    """
    # Build the endpoint path
    endpoint_path = "/pricer/risk_slide/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['instrument'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getriskslideinstruments(market: str) -> str:
    """list of instruments available for risk slide calculations in the specified market
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    
    Query parameters:

    """
    # Build the endpoint path
    endpoint_path = "/pricer/risk_slide_instruments/{market}"
    endpoint_path = endpoint_path.replace("{market}", market)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in [] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def get_calculateriskslidev2(market: str, currency: str, instrument: Optional[str] = None) -> str:
    """Calculates the risk slide for a given instrument in the specified market and currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    instrument: ['BTC-26SEP25-110000-C', 'XRP-31JAN25-2.5-C', 'SOL-31JAN25-245-C', 'BNB-31JAN25-760-C', 'ETH-26SEP25-4000-C', 'PAXG-27JUN25-2720-C', 'DOGE-27DEC24-0.304-C', 'XRP-27DEC24-2.12-C', 'SOL-27DEC24-240-C', 'BNB-3JAN25-630-C', 'ETH-26SEP25-3200-C', 'BTC-26SEP25-80000-C', 'XRP-3JAN25-2.3-C', 'NEAR-31JAN25-6-C', 'FIL-31JAN25-6.5-C', 'TON-31JAN25-6.4-C', 'SOL-3JAN25-200-C', 'BCH-31JAN25-500-C', 'ETH-28MAR25-4200-C', 'BTC-28MAR25-102000-C', 'ETH-26SEP25-4600-C', 'BTC-26SEP25-120000-C', 'DOGE-31JAN25-0.365-C', 'KAS-31JAN25-0.145-C', 'XRP-31JAN25-2.38-C', 'TON-31JAN25-5.9-C', 'FIL-31JAN25-6.4-C', 'NEAR-31JAN25-6.6-C', 'ICP-31JAN25-12.25-C', 'LINK-31JAN25-27.6-C', 'ORDI-31JAN25-30-C', 'SOL-31JAN25-190-C', 'BCH-31JAN25-535-C', 'BNB-31JAN25-710-C', 'ETH-26SEP25-4000-C', 'BTC-26SEP25-110000-C', 'ETH-26SEP25-6000-C', 'BTC-26SEP25-95000-C']
    """
    # Build the endpoint path
    endpoint_path = "/pricer/v2/risk_slide/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['instrument'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getriskslideinstrumentsv2(market: str) -> str:
    """list of instruments available for risk slide calculations in the specified market
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    
    Query parameters:

    """
    # Build the endpoint path
    endpoint_path = "/pricer/v2/risk_slide_instruments/{market}"
    endpoint_path = endpoint_path.replace("{market}", market)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in [] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def get_calculateoptionprice() -> str:
    """Calculates the price and various Greek values for a given option strategy based on the provided input parameters
    
    Path parameters:

    
    Query parameters:

    """
    # Build the endpoint path
    endpoint_path = "/pricer/price"

    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in [] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def get_analyticspotpairs(market: str) -> str:
    """Provides analytics on available spot pairs per market.
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    
    Query parameters:

    """
    # Build the endpoint path
    endpoint_path = "/analytics/spot/spot_pairs/{market}"
    endpoint_path = endpoint_path.replace("{market}", market)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in [] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)



@mcp.tool()
async def gethistoricaltotalnotionalpremiumopeninterestbymarket(market: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """Retrieves historical total notional value and open value by market for a specific market
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/total/oi_by_market/{market}"
    endpoint_path = endpoint_path.replace("{market}", market)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricaltotalnotionalpremiumvolumebymarket(market: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """Retrieves historical total notional volume and premium volume data for a specific market
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/total/volume_by_market/{market}"
    endpoint_path = endpoint_path.replace("{market}", market)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsdvol(market: str, currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Delta Volatility (Dvol) Data by Market and Currency in Options Market
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/dvol/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsvix(market: str, currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Volatility Index (VIX) Data by Market and Currency in Options Market
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/vix/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsoitotal(market: str, currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Total Open Interest (OI) by Market and Currency in Options Market
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/oi_total/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsoipcratio(market: str, currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Put-Call (PC) Ratio in Options Market by Market and Currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/oi_pc_ratio/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsvolumetotal(market: str, currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Total Historical Volume in Options Market by Market and Currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/volume_total/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsatmiv(market: str, currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical ATM Implied Volatility by Market and Currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/atm_iv/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsmaxpain(market: str, currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Max Pain Data by Market and Currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/max_pain/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsgexindex(market: str, currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical GEX Index Data by Market and Currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/gex_index/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsvolumepcratio(market: str, currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Put/Call Ratio Data by Market and Currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/volume_pc_ratio/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionstypegammabands(market: str, currency: str, type: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Gamma Bands by Market, Currency and Type
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    type: ['C', 'P']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/type/gamma_bands/{market}/{currency}/{type}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{type}", type)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gettotaloibycurrency(currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ total Open Interest by Currency
    
    Path parameters:
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/total/oi_by_currency/{currency}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionstotalvolumebycurrency(currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Volume Data by Currency in Options Market
    
    Path parameters:
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/total/volume_by_currency/{currency}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionstypeivbidask(market: str, currency: str, type: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Implied Volatility Bid and Ask by Market, Currency and Type
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    type: ['C', 'P']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/type/iv_bid_ask/{market}/{currency}/{type}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{type}", type)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionstyperiskreversalmodel(market: str, currency: str, type: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Risk Reversal Model Data by Market, Currency and Type
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    type: ['C', 'P']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/type/risk_reversal_model/{market}/{currency}/{type}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{type}", type)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionstyperiskreversal(market: str, currency: str, type: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Risk Reversal Data by Market, Currency and Type
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    type: ['C', 'P']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/type/risk_reversal/{market}/{currency}/{type}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{type}", type)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionstypeskewmodel(market: str, currency: str, type: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Skew Model Data by Market, Currency and Type
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    type: ['C', 'P']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/type/skew_model/{market}/{currency}/{type}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{type}", type)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionstypeskew(market: str, currency: str, type: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Skew Data by Market, Currency and Type
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    type: ['C', 'P']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/type/skew/{market}/{currency}/{type}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{type}", type)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionstypebutterflymodel(market: str, currency: str, type: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Butterfly Model Data by Market, Currency, and Type
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    type: ['C', 'P']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/type/butterfly_model/{market}/{currency}/{type}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{type}", type)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionstypebutterfly(market: str, currency: str, type: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Butterfly Data by Market, Currency, and Type
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    type: ['C', 'P']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/type/butterfly/{market}/{currency}/{type}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{type}", type)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionstypeatmivmodel(market: str, currency: str, type: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical ATM IV Model Data by Market, Currency, and Type
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    type: ['C', 'P']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/type/atm_iv_model/{market}/{currency}/{type}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{type}", type)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsmaturityatmiv(market: str, currency: str, maturity: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical At-The-Money Implied Volatility (ATM IV) for a Specific Maturity by Market and Currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    maturity: ['10MAY25', '11MAY25', '16MAY25', '23MAY25', '25JUL25', '26DEC25', '26SEP25', '27JUN25', '27MAR26', '30MAY25', '8MAY25', '9MAY25']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/maturity/atm_iv_h/{market}/{currency}/{maturity}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{maturity}", maturity)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsmaturityoivolume(market: str, currency: str, maturity: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Open Interest (OI) and Volume for a Specific Maturity by Market and Currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    maturity: ['10MAY25', '11MAY25', '16MAY25', '23MAY25', '25JUL25', '26DEC25', '26SEP25', '27JUN25', '27MAR26', '30MAY25', '8MAY25', '9MAY25']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/maturity/oi_volume/{market}/{currency}/{maturity}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{maturity}", maturity)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsorbitaltvol(currency: str, maturity_name: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """Historical Options Orbit Alternative Volatility Data for a Specific Maturity by Currency
    
    Path parameters:
    currency: Any valid token symbol
    maturity_name: ['atmivts_historical', 'heatmap_change', 'historical_buy_sell_volume', 'iv_table_change', 'oi_gainers_and_losers', 'oi_net_change', 'time_skew']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/orbit_alt_vol/{currency}/{maturity_name}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{maturity_name}", maturity_name)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsivrv(market: str, currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Implied Volatility (IV) and Realized Volatility (RV) Data by Market and Currency in Options Market
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/iv_rv/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsspreadtypeskew(market: str, type: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Skew Data for a Specific Spread (ETH - BTC) by Market and Type
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    type: ['C', 'P']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/spread/type/skew/{market}/{type}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{type}", type)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsmaturitytotaloi(market: str, currency: str, maturity: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Total Open Interest (OI) for a Specific Maturity by Market and Currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    maturity: ['10MAY25', '11MAY25', '16MAY25', '23MAY25', '25JUL25', '26DEC25', '26SEP25', '27JUN25', '27MAR26', '30MAY25', '8MAY25', '9MAY25']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/maturity/total_oi/{market}/{currency}/{maturity}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{maturity}", maturity)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsmaturitytotalvolume(market: str, currency: str, maturity: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Total Volume for a Specific Maturity by Market and Currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    maturity: ['10MAY25', '11MAY25', '16MAY25', '23MAY25', '25JUL25', '26DEC25', '26SEP25', '27JUN25', '27MAR26', '30MAY25', '8MAY25', '9MAY25']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/maturity/total_volume/{market}/{currency}/{maturity}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{maturity}", maturity)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsactualvolbutterflymodel(market: str, currency: str, type: str, days: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Options Actual Volatility with Butterfly Model for a Specific Type and Number of Days
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    type: ['C', 'P']
    days: ['180', '30', '365', '60', '7', '90']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/actual_vol/butterfly_model/{market}/{currency}/{type}/{days}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{type}", type)
    endpoint_path = endpoint_path.replace("{days}", days)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsactualvolskewmodel(market: str, currency: str, type: str, days: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Options Actual Volatility with Skew Model for a Specific Type and Number of Days
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    type: ['C', 'P']
    days: ['180', '30', '365', '60', '7', '90']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/actual_vol/skew_model/{market}/{currency}/{type}/{days}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{type}", type)
    endpoint_path = endpoint_path.replace("{days}", days)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getoptionsactualvolriskreversalmodel(market: str, currency: str, type: str, days: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Options Actual Volatility with Risk Reversal Model for a Specific Type and Number of Days
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    type: ['C', 'P']
    days: ['180', '30', '365', '60', '7', '90']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/actual_vol/risk_reversal_model/{market}/{currency}/{type}/{days}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{type}", type)
    endpoint_path = endpoint_path.replace("{days}", days)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getv2historicaltrades(market: str, currency: str, date: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, blockTradeId: Optional[str] = None, sortBy: Optional[str] = None) -> str:
    """Get historical trades for a specific market and currency
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    date: YYYY-MM-DD format
    limit: Integer (records per page)
    page: Integer (page number)
    blockTradeId: Block trade identifier
    sortBy: Field to sort by
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/v2/trades/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['date', 'limit', 'page', 'blockTradeId', 'sortBy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gettotalvolumeforoptions(start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """Get total trading volume for options
    
    Path parameters:

    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/total_volume_by_currency"

    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gettotaloiforoptions(start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """Get total open interest (OI) for options
    
    Path parameters:

    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/options/total_open_interest_by_currency"

    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getfuturesrealizedvolatility(currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Futures Realized Volatility for a Specific Currency
    
    Path parameters:
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/realized_volatility/{currency}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getfuturesoiweightedfunding(currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Futures Open Interest Weighted Funding for a Specific Currency
    
    Path parameters:
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/oi_weighted_funding/{currency}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getfuturesoiweightedvolumefunding(currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Futures Open Interest Weighted Volume Funding for a Specific Currency
    
    Path parameters:
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/oi_weighted_volume_funding/{currency}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getfuturesoiweightedbasisfunding(currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Futures Open Interest Weighted Basis for a Specific Currency
    
    Path parameters:
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/oi_weighted_basis/{currency}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getfuturestotaloi(currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Futures Total Open Interest for a Specific Currency
    
    Path parameters:
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/total_oi/{currency}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getfuturestotaloibymargin(currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Futures Total Open Interest by Margin for a Specific Currency
    
    Path parameters:
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/total_oi_by_margin/{currency}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getfuturestotalvolume(currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Futures Total Volume for a Specific Currency
    
    Path parameters:
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/total_volume/{currency}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getfuturestotalvolumebymargin(currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Futures Total Volume by Margin for a Specific Currency
    
    Path parameters:
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/total_volume_by_margin/{currency}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getfuturesaltcoinsummary(currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Futures Altcoin Summary for a Specific Currency
    
    Path parameters:
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/alt_summary/{currency}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getfuturesmarketindexdata(index: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Futures Market Index Data for a Specific Index
    
    Path parameters:
    index: ['defi', 'digital_asset', 'exchange', 'layer1', 'layer2', 'memecoin', 'nft_gaming', 'oracle_data', 'privacy']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/market_index/{index}"
    endpoint_path = endpoint_path.replace("{index}", index)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricalindicespricedata(index: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Indices Price Data
    
    Path parameters:
    index: ['defi', 'digital_asset', 'exchange', 'layer1', 'layer2', 'memecoin', 'nft_gaming', 'oracle_data', 'privacy']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/indices_price/{index}"
    endpoint_path = endpoint_path.replace("{index}", index)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricalfuturesannualizedbasisdata(currency: str, days: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Futures Annualized Basis Data
    
    Path parameters:
    currency: Any valid token symbol
    days: ['180', '30', '365', '60', '7', '90']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/futures_annualized_basis/{currency}/{days}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{days}", days)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricalperpetualfundingexchangedata(currency: str, option: str, market: Optional[str] = None, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """ Historical Perpetual Funding Exchange Data
    
    Path parameters:
    currency: Any valid token symbol
    option: ['all', 'future', 'perpetual']
    
    Query parameters:
    market: []
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/perpetual_funding_exchange/{currency}/{option}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{option}", option)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['market', 'start', 'end', 'limit', 'page', 'granularity'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricaltotalopeninterestbyexchangedata(currency: str, option: str, market: Optional[str] = None, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """ Historical Total Open Interest by Exchange Data
    
    Path parameters:
    currency: Any valid token symbol
    option: ['all', 'future', 'perpetual']
    
    Query parameters:
    market: []
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/total_oi_by_exchange/{currency}/{option}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{option}", option)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['market', 'start', 'end', 'limit', 'page', 'granularity'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricaltotalvolumebyexchangedata(currency: str, option: str, market: Optional[str] = None, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """ Historical Total Volume by Exchange Data
    
    Path parameters:
    currency: Any valid token symbol
    option: ['all', 'future', 'perpetual']
    
    Query parameters:
    market: []
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/total_volume_by_exchange/{currency}/{option}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{option}", option)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['market', 'start', 'end', 'limit', 'page', 'granularity'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricalperpetualyielddata(currency: str, market: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Perpetual Yield Data
    
    Path parameters:
    currency: Any valid token symbol
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/perpetual_yield/{currency}/{market}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{market}", market)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricalperpetualfundingdata(currency: str, market: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Perpetual Funding Data
    
    Path parameters:
    currency: Any valid token symbol
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/perpetual_funding/{currency}/{market}"
    endpoint_path = endpoint_path.replace("{currency}", currency)
    endpoint_path = endpoint_path.replace("{market}", market)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricaltotalglobalopeninterestactivitydata(start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Total Global Open Interest Activity Data
    
    Path parameters:

    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/oi_total_global_activity"

    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricaltotalglobalvolumeactivitydata(start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Total Global Volume Activity Data
    
    Path parameters:

    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/volume_total_global_activity"

    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricalexchangedata(market: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Exchange Data
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/aggregate_exchange_data/{market}"
    endpoint_path = endpoint_path.replace("{market}", market)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricalglobalfuturesactivitydata(market: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """ Historical Global Future Activity Data
    
    Path parameters:
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/global_activity_futures/{market}"
    endpoint_path = endpoint_path.replace("{market}", market)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gettotalvolumeforfutures(start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """Get total trading volume for futures
    
    Path parameters:

    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/total_volume_by_currency"

    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gettotaloiforfutures(start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None, legacy: Optional[str] = None) -> str:
    """Get total open interest (OI) for futures
    
    Path parameters:

    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    legacy: Boolean (true/false)
    """
    # Build the endpoint path
    endpoint_path = "/historical/futures/total_open_interest_by_currency"

    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity', 'legacy'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricalderivssummary(currency: str, start: str, end: str, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """
    Historical Derivatives Summary
    
    Required path parameters:
    - currency: Currency identifier (e.g., 'BTC')
    
    Required query parameters:
    - start: Start date of search range (e.g., '2025-05-12', '2025-05-12T10:15', '1747011600000')
    - end: End date of search range (e.g., '2025-05-19', '2025-05-19T10:15', '1747618500000')
    
    Optional query parameters:
    - limit: Maximum number of results per page (max 144)
    - page: Page number to return
    - granularity: Interval between dates ('5m', '15m', '30m', '1h', '2h', '4h', '6h', '12h', '1d')
    
    Returns:
    - meta: Object containing pagination info:
        - total: Total number of items
        - page: Current page number
        - items: Number of items on current page
        - total_pages: Total number of pages
    - items: Array of objects containing:
        - date: Data recording timestamp
        - price: Contract price
        - open_interest: Total open interest
        - volume: Trading volume
        - funding: Funding rate
        - next_fr: Next funding rate
        - yield: Contract yield
        - liquidations_long: Long position liquidations
        - liquidations_short: Short position liquidations
        - market_cap: Market capitalization
        - oi_volume24h: 24h open interest volume
    """
    endpoint_path = f"/historical/derivs/summary/{currency}"
    query_params = {
        "start": start,
        "end": end,
        "limit": limit,
        "page": page,
        "granularity": granularity
    }
    return await make_request("GET", endpoint_path, query_params)


@mcp.tool()
async def gethistoricalfuturesdata(market: str, symbol: str, start: str, end: str, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """
    Historical Futures Data
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - symbol: Symbol identifier (e.g., 'BTC-26SEP25')
    
    Required query parameters:
    - start: Start date of search range (e.g., '2025-05-12', '2025-05-12T10:15', '1747011600000')
    - end: End date of search range (e.g., '2025-05-19', '2025-05-19T10:15', '1747618500000')
    
    Optional query parameters:
    - limit: Maximum number of results per page (max 144)
    - page: Page number to return
    - granularity: Interval between dates ('5m', '15m', '30m', '1h', '2h', '4h', '6h', '12h', '1d')
    
    Returns:
    - meta: Object containing pagination info:
        - total: Total number of items
        - page: Current page number
        - items: Number of items on current page
        - total_pages: Total number of pages
    - items: Array of objects containing:
        - date: Data recording timestamp
        - expiry: Contract expiry date
        - price: Contract price
        - index: Index value
        - basis: Basis point
        - yield: Contract yield
        - volume: Trading volume
        - open_interest: Total open interest
        - oi_volume24h: 24h open interest volume
    """
    endpoint_path = f"/historical/derivs/futures/{market}/{symbol}"
    query_params = {
        "start": start,
        "end": end,
        "limit": limit,
        "page": page,
        "granularity": granularity
    }
    return await make_request("GET", endpoint_path, query_params)


@mcp.tool()
async def gethistoricalperpetualderivativesdata(market: str, symbol: str, start: str, end: str, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """
    Historical Perpetual Derivatives Data
    
    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - symbol: Symbol identifier (e.g., 'BTC-PERPETUAL')
    
    Required query parameters:
    - start: Start date of search range (e.g., '2025-05-12', '2025-05-12T10:15', '1747011600000')
    - end: End date of search range (e.g., '2025-05-19', '2025-05-19T10:15', '1747618500000')
    
    Optional query parameters:
    - limit: Maximum number of results per page (max 144)
    - page: Page number to return
    - granularity: Interval between dates ('5m', '15m', '30m', '1h', '2h', '4h', '6h', '12h', '1d')
    
    Returns:
    - meta: Object containing pagination info:
        - total: Total number of items
        - page: Current page number
        - items: Number of items on current page
        - total_pages: Total number of pages
    - items: Array of objects containing:
        - date: Data recording timestamp
        - price: Contract price
        - index: Index value
        - basis: Basis point
        - funding: Funding rate
        - yield: Contract yield
        - volume: Trading volume
        - open_interest: Total open interest
        - oi_volume24h: 24h open interest volume
        - long_short_ratio: Long/short ratio
        - next_funding: Next funding rate
    """
    endpoint_path = f"/historical/derivs/perpetuals/{market}/{symbol}"
    query_params = {
        "start": start,
        "end": end,
        "limit": limit,
        "page": page,
        "granularity": granularity
    }
    return await make_request("GET", endpoint_path, query_params)


@mcp.tool()
async def getorderbookbymarkettypesymbol(marketType: str, currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """Fetch historical simple order books for specific market type 
    
    Path parameters:
    marketType: ['future', 'perpetual', 'spot']
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    """
    # Build the endpoint path
    endpoint_path = "/historical/orderbooks/{marketType}/{currency}"
    endpoint_path = endpoint_path.replace("{marketType}", marketType)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getorderbookbymarkettypemarketcurrency(marketType: str, market: str, currency: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """Fetch historical simple order books for specific market and currency 
    
    Path parameters:
    marketType: ['future', 'perpetual', 'spot']
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    currency: Any valid token symbol
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    """
    # Build the endpoint path
    endpoint_path = "/historical/orderbooks/{marketType}/{market}/{currency}"
    endpoint_path = endpoint_path.replace("{marketType}", marketType)
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{currency}", currency)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def getorderbookbymarkettypemarketsymbol(marketType: str, market: str, symbol: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None, granularity: Optional[str] = None) -> str:
    """Fetch historical simple order books for specific market and symbol 
    
    Path parameters:
    marketType: ['future', 'perpetual', 'spot']
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    symbol: ['BTC_USDCETUAL', 'BTC-27JUN25', 'BTCETUAL', 'ETHETUAL', 'BTCDOMUSDT', 'BTCUSD_250627', 'BTCUSD_250926', 'BTCUSD_PERP', 'BTCUSDC', 'TBTCF0:USTF0', 'ETHUSD', 'ETHUSDT', 'BTCPERP', 'BTCUSD', 'BTCUSDM25', 'BTCUSDT', 'BTCUSDT-26DEC25', 'BTC-USD', 'BTC-USDT', 'ETH-USD', 'ETH-USDT', 'ETHFI-USDT', 'BTC-USD', 'BTC-USDC', 'BTC-USDT', 'ETH-USD', 'ETHFI-USDT']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    granularity: ['1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d']
    """
    # Build the endpoint path
    endpoint_path = "/historical/orderbooks/by_symbol/{marketType}/{market}/{symbol}"
    endpoint_path = endpoint_path.replace("{marketType}", marketType)
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{symbol}", symbol)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page', 'granularity'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricalspotohlc(symbol: str, market: str, period: str, start: Optional[str] = None, end: Optional[str] = None, limit: Optional[str] = None, page: Optional[str] = None) -> str:
    """Get Historical Spot OHLC Data
    
    Path parameters:
    symbol: ['BTC_USDCETUAL', 'BTC-27JUN25', 'BTCETUAL', 'ETHETUAL', 'BTCDOMUSDT', 'BTCUSD_250627', 'BTCUSD_250926', 'BTCUSD_PERP', 'BTCUSDC', 'TBTCF0:USTF0', 'ETHUSD', 'ETHUSDT', 'BTCPERP', 'BTCUSD', 'BTCUSDM25', 'BTCUSDT', 'BTCUSDT-26DEC25', 'BTC-USD', 'BTC-USDT', 'ETH-USD', 'ETH-USDT', 'ETHFI-USDT', 'BTC-USD', 'BTC-USDC', 'BTC-USDT', 'ETH-USD', 'ETHFI-USDT']
    market: ['deribit', 'binance', 'bybit', 'coincall', 'okx']
    period: ['1', '2', '4', '8', '12', '18', '24', '48', '168', '336', '504', '720', '8760', 'ytd']
    
    Query parameters:
    start: YYYY-MM-DD format or Unix timestamp
    end: YYYY-MM-DD format or Unix timestamp
    limit: Integer (records per page)
    page: Integer (page number)
    """
    # Build the endpoint path
    endpoint_path = "/historical/spot/{market}/{symbol}/{period}"
    endpoint_path = endpoint_path.replace("{symbol}", symbol)
    endpoint_path = endpoint_path.replace("{market}", market)
    endpoint_path = endpoint_path.replace("{period}", period)
    
    # Build query parameters
    query_params = {
        k: v for k, v in locals().items() 
        if k in ['start', 'end', 'limit', 'page'] and v is not None
    }
    
    # Make the request
    result = await make_request('GET', endpoint_path, query_params)
    return str(result)


@mcp.tool()
async def gethistoricaloptionstrades(
    market: str,
    currency: str,
    date: str,
    limit: Optional[int] = None,
    page: Optional[int] = None
) -> str:
    """
    Retrieves historical options trade data for a specific currency in a given market.

    Required path parameters:
    - market: Market identifier (e.g., 'DERIBIT')
    - currency: Currency identifier (e.g., 'BTC')

    Required query parameters:
    - date: The date of the search range (e.g., '2025-05-19', '2025-05-19T10:15', '1747618500000'). This date will always be changed to start of day.

    Optional query parameters:
    - limit: The maximum number of results to return per page (max 144)
    - page: The page of results to return

    Returns:
    - meta: Object containing pagination info:
        - total: Total number of items
        - page: Current page number
        - items: Number of items on current page
        - total_pages: Total number of pages
    - items: Array of objects containing:
        - id: Unique identifier of the trade
        - market: The market where the trade took place
        - currency: The currency involved in the trade
        - option_type: The type of the option (call or put)
        - maturity: The maturity date of the option
        - date: The date when the trade was recorded
        - index_price: The price of the underlying index at the time of the trade
        - strike: The strike price of the option
        - mark_price: The market price of the option
        - implied_vol: The implied volatility of the option
        - trade_seq: The sequence number of the trade
        - trade_id: Unique identifier of the trade
        - liquidation: Indicator of whether the trade was a liquidation (1) or not (0)
        - block_trade_id: Identifier of a block trade if applicable
        - tick_direction: Direction of the price tick
        - price: The price at which the trade occurred
        - direction: Direction of the trade (0 for buy, 1 for sell)
        - amount: The amount traded
    """
    endpoint_path = f"/historical/options/trades/{market}/{currency}"
    query_params = {
        "date": date,
        "limit": limit,
        "page": page
    }
    # Remove None values from query_params
    query_params = {k: v for k, v in query_params.items() if v is not None}
    return await make_request("GET", endpoint_path, query_params)


if __name__ == "__main__":
    mcp.run(transport='stdio')
