"""Item CRUD tests."""

import pytest


@pytest.fixture
async def auth_token(client):
    await client.post("/auth/register", json={
        "email": "items@example.com",
        "password": "secret123"
    })
    resp = await client.post("/auth/login", data={
        "username": "items@example.com",
        "password": "secret123"
    })
    return resp.json()["access_token"]


@pytest.mark.asyncio
async def test_create_item(client, auth_token):
    response = await client.post("/items/", json={
        "title": "Test Item",
        "description": "A test item"
    }, headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Item"


@pytest.mark.asyncio
async def test_list_items(client, auth_token):
    await client.post("/items/", json={"title": "Item 1"}, headers={"Authorization": f"Bearer {auth_token}"})
    response = await client.get("/items/", headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == 200
    assert len(response.json()) >= 1


@pytest.mark.asyncio
async def test_unauthorized_access(client):
    response = await client.get("/items/")
    assert response.status_code == 401
