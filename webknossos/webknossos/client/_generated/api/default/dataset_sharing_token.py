from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.dataset_sharing_token_response_200 import DatasetSharingTokenResponse200
from ...types import Response


def _get_kwargs(
    organization_name: str,
    data_set_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/datasets/{organizationName}/{dataSetName}/sharingToken".format(
        client.base_url, organizationName=organization_name, dataSetName=data_set_name
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[DatasetSharingTokenResponse200]:
    if response.status_code == 200:
        response_200 = DatasetSharingTokenResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[DatasetSharingTokenResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    organization_name: str,
    data_set_name: str,
    *,
    client: Client,
) -> Response[DatasetSharingTokenResponse200]:
    kwargs = _get_kwargs(
        organization_name=organization_name,
        data_set_name=data_set_name,
        client=client,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    organization_name: str,
    data_set_name: str,
    *,
    client: Client,
) -> Optional[DatasetSharingTokenResponse200]:
    """ """

    return sync_detailed(
        organization_name=organization_name,
        data_set_name=data_set_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_name: str,
    data_set_name: str,
    *,
    client: Client,
) -> Response[DatasetSharingTokenResponse200]:
    kwargs = _get_kwargs(
        organization_name=organization_name,
        data_set_name=data_set_name,
        client=client,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    organization_name: str,
    data_set_name: str,
    *,
    client: Client,
) -> Optional[DatasetSharingTokenResponse200]:
    """ """

    return (
        await asyncio_detailed(
            organization_name=organization_name,
            data_set_name=data_set_name,
            client=client,
        )
    ).parsed
