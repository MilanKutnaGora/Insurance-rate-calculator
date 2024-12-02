import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models import Rate
from datetime import date

# Создаем тестовую базу данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    # Создаем тестовые данные перед каждым тестом
    db = TestingSessionLocal()
    db.query(Rate).delete()
    db.add(Rate(date=date(2020, 6, 1), cargo_type="Glass", rate=0.04))
    db.add(Rate(date=date(2020, 6, 1), cargo_type="Other", rate=0.01))
    db.commit()
    yield
    # Очищаем базу данных после каждого теста
    db.query(Rate).delete()
    db.commit()

def test_calculate_insurance():
    response = client.post(
        "/calculate_insurance",
        json={"date": "2020-06-01", "cargo_type": "Glass", "declared_value": 1000, "user_id": 1}
    )
    assert response.status_code == 200
    assert response.json() == {"insurance_cost": 40.0}

def test_create_rate():
    response = client.post(
        "/rates/",
        json={"date": "2020-07-01", "cargo_type": "Electronics", "rate": 0.02}
    )
    assert response.status_code == 200
    assert response.json()["cargo_type"] == "Electronics"
    assert response.json()["rate"] == 0.02

def test_read_rates():
    response = client.get("/rates/")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_update_rate():
    # Сначала создаем новый тариф
    create_response = client.post(
        "/rates/",
        json={"date": "2020-08-01", "cargo_type": "Furniture", "rate": 0.03}
    )
    rate_id = create_response.json()["id"]

    # Теперь обновляем его
    update_response = client.put(
        f"/rates/{rate_id}",
        json={"rate": 0.035}
    )
    assert update_response.status_code == 200
    assert update_response.json()["rate"] == 0.035

def test_delete_rate():
    # Сначала создаем новый тариф
    create_response = client.post(
        "/rates/",
        json={"date": "2020-09-01", "cargo_type": "Food", "rate": 0.025}
    )
    rate_id = create_response.json()["id"]

    # Теперь удаляем его
    delete_response = client.delete(f"/rates/{rate_id}")
    assert delete_response.status_code == 200

    # Проверяем, что тариф действительно удален
    get_response = client.get(f"/rates/{rate_id}")
    assert get_response.status_code == 404

def test_calculate_insurance_rate_not_found():
    response = client.post(
        "/calculate_insurance",
        json={"date": "2019-01-01", "cargo_type": "Glass", "declared_value": 1000, "user_id": 1}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Rate not found"
