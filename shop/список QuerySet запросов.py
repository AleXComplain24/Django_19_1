# 1. Создание покупателей
buyer1 = Buyer.objects.create(name="Alice", balance=200.00, age=25)
buyer2 = Buyer.objects.create(name="Bob", balance=150.00, age=17)
buyer3 = Buyer.objects.create(name="Charlie", balance=300.00, age=30)

# 2. Создание игр
game1 = Game.objects.create(title="Adventure Quest", cost=50.00, size=5.0, description="An exciting adventure game", age_limited=True)
game2 = Game.objects.create(title="Puzzle Master", cost=30.00, size=3.5, description="Challenging puzzles to solve", age_limited=False)
game3 = Game.objects.create(title="Action Blast", cost=60.00, size=7.0, description="High-energy action game", age_limited=True)

# 3. Связывание игр с покупателями
game1.buyer.set([buyer1])
game2.buyer.set([buyer1])
game3.buyer.set([buyer1])

# 4. Связывание игры без ограничения возраста с младшим 18 лет
game2.buyer.add(buyer2)

# 5. Связывание игры с другим покупателем
game1.buyer.add(buyer3)
