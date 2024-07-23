from unittest.mock import ANY

from catalog.factories import ItemFactory


def test_item_list(api_client):
    item = ItemFactory()

    response = api_client.get("/api/items/")

    assert response.status_code == 200

    assert response.data == [
        {
            "id": item.id,
            "title": item.title,
            "description": item.description,
            "price": item.price,
            "order": item.order,
        }
    ]


def test_item_retrieve(api_client):
    item = ItemFactory()

    response = api_client.get(f"/api/items/{item.id}/")

    assert response.status_code == 200

    assert response.data == {
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "price": item.price,
        "order": item.order,
        "image": {
            "id": item.image.id,
            "image": ANY,
            "caption": item.image.caption,
            "order": item.image.order,
        },
        "details": {
            "id": item.details.id,
            "title": item.details.title,
            "value": item.details.value,
            "price": item.details.price,
            "order": item.details.order,
        },
    }
