import requests
import json
from .exceptions import MCPRequestError

class MCPDeFiSDK:
    def __init__(self, base_url):
        """
        Initializes the MCPDeFiSDK with the base URL of the MCP server.
        """
        self.base_url = base_url

    def _make_request(self, endpoint, params=None):
        """
        Makes a GET request to the specified endpoint with the given parameters.
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            raise MCPRequestError(f"Error making request to {url}: {e}")

    def get_defi_risk(self, collateral_ratio, liquidity, volatility, market_cap=None):
        """
        Retrieves a DeFi risk score from the MCP server.
        """
        endpoint = "/mcp/defi/risk"
        params = {
            "collateral_ratio": collateral_ratio,
            "liquidity": liquidity,
            "volatility": volatility,
            "market_cap": market_cap,
        }
        return self._make_request(endpoint, params)

    def get_dao_vote_result(self, proposal_id, voter_weights):
        """
        Retrieves the result of a DAO vote from the MCP server.
        """
        endpoint = "/mcp/dao/vote"
        params = {
            "proposal_id": proposal_id,
            "voter_weights": json.dumps(voter_weights),  # Convert to JSON string
        }
        return self._make_request(endpoint, params)

    def get_nft_valuation(self, rarity_score, market_cap, trading_volume, artist_reputation=None):
        """
        Retrieves an NFT valuation from the MCP server.
        """
        endpoint = "/mcp/nft/valuation"
        params = {
            "rarity_score": rarity_score,
            "market_cap": market_cap,
            "trading_volume": trading_volume,
            "artist_reputation": artist_reputation,
        }
        return self._make_request(endpoint, params)

    def get_lending_rate(self, collateral_type, loan_duration, loan_amount, market_conditions=None):
        """
        Retrieves a lending rate from the MCP server.
        """
        endpoint = "/mcp/defi/lending_rate"
        params = {
            "collateral_type": collateral_type,
            "loan_duration": loan_duration,
            "loan_amount": loan_amount,
            "market_conditions": market_conditions,
        }
        return self._make_request(endpoint, params)

    def get_stablecoin_apy(self, stablecoin_name, deposit_amount, lockup_period, platform_risk=None):
        """
        Retrieves a stablecoin APY from the MCP server.
        """
        endpoint = "/mcp/defi/stablecoin_apy"
        params = {
            "stablecoin_name": stablecoin_name,
            "deposit_amount": deposit_amount,
            "lockup_period": lockup_period,
            "platform_risk": platform_risk,
        }
        return self._make_request(endpoint, params)
