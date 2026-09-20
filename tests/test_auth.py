"""Auth tests."""

import pytest


@pytest.mark.asyncio
async def test_register(client):
    response = await client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "secret123"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"


@pytest.mark.asyncio
async def test_login(client):
    await client.post("/auth/register", json={
        "email": "login@example.com",
        "password": "secret123"
    })
    response = await client.post("/auth/login", data={
        "username": "login@example.com",
        "password": "secret123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()


@pytest.mark.asyncio
async def test_duplicate_email(client):
    await client.post("/auth/register", json={
        "email": "dup@example.com",
        "password": "secret123"
    })
    response = await client.post("/auth/register", json={
        "email": "dup@example.com",
        "password": "secret123"
    })
    assert response.status_code == 400
