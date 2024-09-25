from fastapi import Query, APIRouter

hotels = [
    {"id": 1, "title": "Сочи", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"},
    {"id": 3, "title": "Мальдивы", "name": "maldivi"},
    {"id": 4, "title": "Геленджик", "name": "gelendzhik"},
    {"id": 5, "title": "Москва", "name": "moscow"},
    {"id": 6, "title": "Казань", "name": "kazan"},
    {"id": 7, "title": "Санкт-Петербург", "name": "spb"},
]

router = APIRouter(prefix='/hotels', tags=["Отели"])


@router.get("", description="Получить список отелей или отель по названию", name="Список отелей")
async def get_hotels(
        hotel_id: int | None = Query(None, description="Айдишник"),
        title: str | None = Query(None, description="Название отеля"),
        page: int | None = Query(1, description="Номер страницы"),
        per_page: int | None = Query(3, description="Количество отелей на странице"),
):
    if hotel_id or title:
        hotels_ = []
        for hotel in hotels:
            if hotel_id and hotel["id"] != hotel_id:
                continue
            if title and hotel["title"] != title:
                continue
            hotels_.append(hotel)
        return hotels_

    if page != 1:
        page -= 1
        start = page * per_page
        end = start + per_page
        print(hotels[start:end])
        return hotels[start:end]
    if page == 1:
        print(hotels[0:per_page])
        return hotels[0:per_page]


