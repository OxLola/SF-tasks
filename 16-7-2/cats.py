from kitty import Cat

cats = [
    {
        "name": "Сэм",
        "gender": "мальчик",
        "age": 2,
    },
    {
        "name": "Мурка",
        "gender": "девочка",
        "age": 1,
    },
    {
        "name": "Снежочек",
        "gender": "мальчик",
        "age": 33,
    },
    {
        "name": "Аннушка",
        "gender": "девочка",
        "age": 6,
    }, {
        "name": "Бултышка",
        "gender": "девочка",
        "age": 5,
    }, {
        "name": "Чёпа",
        "gender": "мальчик",
        "age": 1,
    },
]
for cat in cats:
     cat_obj = Cat()
     cat_obj.from_dict(cat)
     print(cat_obj.name, cat_obj.age, cat_obj.gender)