import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_admin_redirects_to_login(client):
    response = client.get(reverse("admin:index"))

    assert response.status_code == 302
