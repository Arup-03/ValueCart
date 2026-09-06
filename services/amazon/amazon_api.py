import requests


class AmazonAPI:

    def __init__(
        self,
        client_id,
        client_secret,
        partner_tag,
        marketplace
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.partner_tag = partner_tag
        self.marketplace = marketplace

        # Amazon Creators API
        self.api_endpoint = (
            "https://creatorsapi.amazon/"
            "catalog/v1/searchItems"
        )

        # India uses the EU authentication region
        self.token_endpoint = (
            "https://api.amazon.co.uk/"
            "auth/o2/token"
        )

    def get_access_token(self):

        if not self.client_id or not self.client_secret:
            return None

        payload = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": "creatorsapi::default"
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:

            response = requests.post(
                self.token_endpoint,
                headers=headers,
                json=payload,
                timeout=10
            )

            if response.status_code != 200:
                return None

            data = response.json()

            return data.get("access_token")

        except requests.RequestException:
            return None

    def search_products(self, keywords):

        if not keywords or not keywords.strip():
            return []

        if not self.client_id:
            return []

        if not self.client_secret:
            return []

        if not self.partner_tag:
            return []

        access_token = self.get_access_token()

        if not access_token:
            return []

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "x-marketplace": self.marketplace
        }

        payload = {
            "keywords": keywords.strip(),
            "partnerTag": self.partner_tag,
            "marketplace": self.marketplace,
            "itemCount": 10,
            "resources": [
                "itemInfo.title",
                "offersV2.listings.price",
                "images.primary.large"
            ]
        }

        try:

            response = requests.post(
                self.api_endpoint,
                headers=headers,
                json=payload,
                timeout=10
            )

            if response.status_code != 200:
                return []

            data = response.json()

            return self._parse_results(data)

        except requests.RequestException:
            return []

    def _parse_results(self, data):

        products = []

        items = (
            data.get("searchResult", {})
            .get("items", [])
        )

        for item in items:

            title = (
                item.get("itemInfo", {})
                .get("title", {})
                .get("displayValue")
            )

            price = None

            listings = (
                item.get("offersV2", {})
                .get("listings", [])
            )

            if listings:

                price_data = (
                    listings[0]
                    .get("price", {})
                )

                price = price_data.get(
                    "amount"
                )

            products.append({
                "platform": "Amazon",
                "name": title or "Unknown Product",
                "price": price,
                "url": item.get(
                    "detailPageURL",
                    ""
                ),
                "status": "api"
            })

        return products