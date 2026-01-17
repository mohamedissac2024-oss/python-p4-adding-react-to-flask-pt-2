#!/usr/bin/env python3
from app import app, db
from models import Movie

with app.app_context():
    print(f'Movies in DB: {Movie.query.count()}')
    
    # Test the /movies endpoint
    with app.test_client() as client:
        response = client.get('/movies')
        print(f'GET /movies status: {response.status_code}')
        data = response.get_json()
        print(f'Movies returned: {len(data)}')
        if data:
            print(f'First movie: {data[0]}')

