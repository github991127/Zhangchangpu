"""Tests for Flask routes."""

import pytest

from routes import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert '张菖蒲' in resp.get_data(as_text=True)


def test_zhangchangpu_solution(client):
    resp = client.post('/api/zhangchangpu', json={'input': '1 2 3 5 5 6'})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['success'] is True
    assert len(data['data']['solutions']) > 0
    assert data['data']['input_count'] == 6
    assert data['data']['max_card_count'] == 6


def test_zhangchangpu_no_solution(client):
    resp = client.post('/api/zhangchangpu', json={'input': '1 2 4'})
    data = resp.get_json()
    assert data['data']['solutions'] == []
    assert data['data']['best_solutions'] == []


def test_mizhu_solution(client):
    resp = client.post('/api/mizhu', json={'input': '3 4 5 6 7 8 9 13'})
    data = resp.get_json()
    assert data['success'] is True
    assert data['data']['count'] > 0
    assert data['data']['combinations'][0]['text']


def test_invalid_input(client):
    resp = client.post('/api/zhangchangpu', json={'input': 'X Y Z'})
    assert resp.status_code == 400


def test_too_many_cards(client):
    resp = client.post('/api/mizhu', json={'input': ' '.join(['1'] * 31)})
    assert resp.status_code == 400
