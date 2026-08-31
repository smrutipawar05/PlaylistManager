from fastapi.testclient import TestClient
from fastapi import FastAPI
from FakeStorage import FakeStorage
from song_service import SongService
from router import create_router
import pytest
@pytest.fixture
def client():
    app=FastAPI()
    storage=FakeStorage()
    service=SongService(storage)
    router=create_router(service)
    app.include_router(router)
    return TestClient(app)

def test_create_song(client):
    response=client.post(
        "/songs",
        json={
            "title":"xyz",
            "artist":"abc",
            "info":"rock"
        }
    )
    assert response.status_code==200
    data=response.json()
    assert data["title"]=="xyz"
    assert data["artist"]=="abc"
    assert data["info"]=="rock"

def test_load_songs(client):
    client.post(
        "/songs",
        json={
            "title":"xyz",
            "artist":"abc",
            "info":"rock"
        }
    )
    client.post(
        "/songs",
        json={
            "title":"xyz`",
            "artist":"abc`",
            "info":"pop"
        }
    )
    response=client.get(
        "/songs",
    )
    assert response.status_code==200
    data=response.json()
    assert data[0]["title"]=="xyz"
    assert data[0]["artist"]=="abc"
    assert data[0]["info"]=="rock"    
    assert data[1]["title"]=="xyz`"
    assert data[1]["artist"]=="abc`"
    assert data[1]["info"]=="pop"

def test_load_song(client):
    client.post(
        "/songs",
        json={
            "title":"xyz",
            "artist":"abc",
            "info":"rock"
        }
    )
    client.post(
        "/songs",
        json={
            "title":"xyz`",
            "artist":"abc`",
            "info":"pop"
        }
    )
    response=client.get(
        "/song/1",
    )
    response_notfound=client.get(
        "/song/5",
    )
    assert response.status_code==200
    assert response_notfound.status_code==404
    data=response.json()
    assert data["title"]=="xyz"
    assert data["artist"]=="abc"
    assert data["info"]=="rock"

def test_update_song(client):
    client.post(
        "/songs",
        json={
            "title":"xyz",
            "artist":"abc",
            "info":"rock"
        }
    )
    client.post(
        "/songs",
        json={
            "title":"xyz`",
            "artist":"abc`",
            "info":"pop"
        }
    )
    response=client.patch(
        "/song/1",
        json={
            "title":"pqr"
        }
    )
    response_alreadyexists=client.patch(
        "/song/1",
        json={
            "title":"xyz`",
            "artist":"abc`",
            "info":"softpop"
        }
    )
    response_notfound=client.patch(
        "/song/5",
        json={
            "title":"nahhh"
        }
    )
    assert response.status_code==200
    assert response_alreadyexists.status_code==409
    assert response_notfound.status_code==404
    data=response.json()
    assert data["title"]=="pqr"
    assert data["artist"]=="abc"
    assert data["info"]=="rock"
def test_delete_song(client):
    client.post(
        "/songs",
        json={
            "title":"xyz",
            "artist":"abc",
            "info":"rock"
        }
    )
    response=client.delete(
        "/song/1"
    )
    response_deleted=client.get(
        "/song/1"
    )
    response_nonexistent=client.delete(
        "/song/1"
    )
    assert response.status_code==200
    assert response_deleted.status_code==404
    assert response_nonexistent.status_code==404