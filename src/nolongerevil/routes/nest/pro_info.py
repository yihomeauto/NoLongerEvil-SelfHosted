"""Nest pro_info endpoint - installer information lookup."""

from aiohttp import web

from nolongerevil.lib.logger import get_logger

logger = get_logger(__name__)

async def handle_pro_info(request: web.Request) -> web.Response:
    """Handle installer information lookup request.

    The {code} path parameter is typically a pro installer code.
    Since we're self-hosted, we return a generic response.

    Returns:
        JSON response with installer info (or empty)
    """
    code = request.match_info.get("code", "")

    logger.debug(f"Pro info request for code: {code}")

    # https://github.com/codykociemba/NoLongerEvil-Thermostat/blob/774da29a29bf707c73a5fa666776819d09d09ee7/server/src/routes/nest/proInfo.ts
    return web.json_response(
        {
            "id": 1,
            "pro_id": code,
            "dba": 'nolongerevil',
            #"street_address_1": '7975 N Hayden Rd',
            #"street_address_2": 'Suite A210',
            "locality": 'A Self-Hosted Thermostat',
            #"region": 'Arizona',
            #"postal_code": '85388',
            #"email": 'cody@hackhouse.io',
            #"phone": '(855) 994-1337',
            "website": 'https://nolongerevil.com',
            "rating": 5.0,
            #"plain_email_address_for_referrals": 'cody@hackhouse.io',
        }
    )
    
def create_pro_info_routes(app: web.Application) -> None:
    """Register pro_info routes.

    Args:
        app: aiohttp application
    """
    app.router.add_get("/nest/pro_info/{code}", handle_pro_info)
