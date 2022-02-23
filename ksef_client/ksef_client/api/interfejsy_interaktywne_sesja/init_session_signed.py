from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.exception_response import ExceptionResponse
from ...models.init_session_response import InitSessionResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/online/Session/InitSigned".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ExceptionResponse, InitSessionResponse]]:
    if response.status_code == 201:
        response_201 = InitSessionResponse.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = ExceptionResponse.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ExceptionResponse, InitSessionResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[ExceptionResponse, InitSessionResponse]]:
    """Inicjalizacja sesji, wskazanie kontekstu, uwierzytelnienie i autoryzacja

     Inicjalizacja sesji interaktywnej. Podpisany dokument
    http://ksef.mf.gov.pl/schema/gtw/svc/online/auth/request/2021/10/01/0001/InitSessionSignedRequest

    Returns:
        Response[Union[ExceptionResponse, InitSessionResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[ExceptionResponse, InitSessionResponse]]:
    """Inicjalizacja sesji, wskazanie kontekstu, uwierzytelnienie i autoryzacja

     Inicjalizacja sesji interaktywnej. Podpisany dokument
    http://ksef.mf.gov.pl/schema/gtw/svc/online/auth/request/2021/10/01/0001/InitSessionSignedRequest

    Returns:
        Response[Union[ExceptionResponse, InitSessionResponse]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[ExceptionResponse, InitSessionResponse]]:
    """Inicjalizacja sesji, wskazanie kontekstu, uwierzytelnienie i autoryzacja

     Inicjalizacja sesji interaktywnej. Podpisany dokument
    http://ksef.mf.gov.pl/schema/gtw/svc/online/auth/request/2021/10/01/0001/InitSessionSignedRequest

    Returns:
        Response[Union[ExceptionResponse, InitSessionResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[ExceptionResponse, InitSessionResponse]]:
    """Inicjalizacja sesji, wskazanie kontekstu, uwierzytelnienie i autoryzacja

     Inicjalizacja sesji interaktywnej. Podpisany dokument
    http://ksef.mf.gov.pl/schema/gtw/svc/online/auth/request/2021/10/01/0001/InitSessionSignedRequest

    Returns:
        Response[Union[ExceptionResponse, InitSessionResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
