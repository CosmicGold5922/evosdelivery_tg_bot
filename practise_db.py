from loader import db




db.create_users_table()
db.create_product_table()
db.create_category_table()
db.create_orders_table()
db.create_type_table()
db.create_location_table()





db.add_category('Лаваш', 'BACK-896/6-oy/Evos Bot/images/categories/lavash.jpg')
db.add_category('Триндвич', 'BACK-896/6-oy/Evos Bot/images/categories/trindwich.jpg')
db.add_category('Шаурма', 'BACK-896/6-oy/Evos Bot/images/categories/shaurma.jpg')
db.add_category('Бургеры', 'BACK-896/6-oy/Evos Bot/images/categories/burger.jpg')
db.add_category('Саб', 'BACK-896/6-oy/Evos Bot/images/categories/sab.jpg')
db.add_category('Картошка', 'BACK-896/6-oy/Evos Bot/images/categories/kartoshka.jpg')
db.add_category('Хот-Доги', 'BACK-896/6-oy/Evos Bot/images/categories/hotdog.jpg')
db.add_category('Снэки', 'BACK-896/6-oy/Evos Bot/images/categories/sneki.jpg')
db.add_category('Гарниры, салаты, хлеб', 'BACK-896/6-oy/Evos Bot/images/categories/garnir.jpg')
db.add_category('Соусы, добавки', 'BACK-896/6-oy/Evos Bot/images/categories/sous.jpg')
db.add_category('Наборы (сеты)', 'BACK-896/6-oy/Evos Bot/images/categories/nabor.jpg')
db.add_category('Десерты', 'BACK-896/6-oy/Evos Bot/images/categories/desert.jpg')
db.add_category('Горячие напитки', 'BACK-896/6-oy/Evos Bot/images/categories/coffee.jpg')
db.add_category('Холодные напитки', 'BACK-896/6-oy/Evos Bot/images/categories/cola.jpg')
db.add_category('Комбо', 'BACK-896/6-oy/Evos Bot/images/categories/kombo.jpg')





db.add_product('Лаваш с курицей', 'BACK-896/6-oy/Evos Bot/images/products/lavash/kuritsa.jpg', 'Лаваш')
db.add_type('Мини', 23000, 1)
db.add_type('Биг', 28000, 1)

db.add_product('Лаваш с говядиной и сыром', 'BACK-896/6-oy/Evos Bot/images/products/lavash/govyadina_sir.jpg', 'Лаваш')
db.add_type('Мини', 28000, 2)
db.add_type('Биг', 33000, 2)

db.add_product('Лаваш острый с говядиной', 'BACK-896/6-oy/Evos Bot/images/products/lavash/ostriy_govyadina.jpg', 'Лаваш', """Сочные кусочки говядины гриль и спелых помидоров, золотистые чипсы, томатный острый соус Калампир со свежим луком в румяном ред-лаваше.\n Цена: 30 000 сум""")
db.add_type(None, 30000, 3)

db.add_product('Лаваш острый с курицей', 'BACK-896/6-oy/Evos Bot/images/products/lavash/ostriy_kuritsa.jpg', 'Лаваш', """Пикантное куриное мясо гриль, кусочки спелых помидоров, золотистые чипсы, ломтик сыра "Чеддер",  томатный острый соус Калампир со свежим луком в румяном ред-лаваше.\n Цена: 28 000 сум""")
db.add_type(None, 28000, 4)

db.add_product('Лаваш с курицей и сыром', 'BACK-896/6-oy/Evos Bot/images/products/lavash/kuritsa_sir.jpg', 'Лаваш')
db.add_type('Мини', 26000, 5)
db.add_type('Биг', 31000, 5)

db.add_product('Фиттер', 'BACK-896/6-oy/Evos Bot/images/products/lavash/fitter.jpg', 'Лаваш', """Нежное куриное мясо гриль, салат "Айсберг", кусочки спелого помидора и свежего огурца, мягкий сыр "Фетакса", легкий сливочный соус Эко в нежно-салатовом лаваше Фиттер\n Цена: 26 000 сум""")
db.add_type(None, 26000, 6)

db.add_product('Лаваш с говядиной', 'BACK-896/6-oy/Evos Bot/images/products/lavash/govyadina.jpg', 'Лаваш')
db.add_type('Мини', 25000, 7)
db.add_type('Биг', 30000, 7)





db.add_product('Триндвич с курицей', 'BACK-896/6-oy/Evos Bot/images/products/trindwich/kuritsa.jpg', 'Триндвич', """Нежное куриное мясо-гриль с сыром и помидорами под ароматным соусом в мягкой тортилье!\n Цена: 26 000 сум""")
db.add_type(None, 26000, 8)

db.add_product('Триндвич с говядиной', 'BACK-896/6-oy/Evos Bot/images/products/trindwich/govyadina.jpg', 'Триндвич', """Нежное мясо говядины гриль с сыром и  помидорами под особым соусом в мягкой  сырной тортилье!\n Цена: 28 000 сум""")
db.add_type(None, 28000, 9)





db.add_product('Шаурма острая с говядиной', 'BACK-896/6-oy/Evos Bot/images/products/shaurma/ostriy_govyadina.jpg', 'Шаурма')
db.add_type('Мини', 24000, 10)
db.add_type('Биг', 28000, 10)

db.add_product('Шаурма с курицей', 'BACK-896/6-oy/Evos Bot/images/products/shaurma/kuritsa.jpg', 'Шаурма')
db.add_type('Мини', 23000, 11)
db.add_type('Биг', 26000, 11)

db.add_product('Шаурма острая c курицей', 'BACK-896/6-oy/Evos Bot/images/products/shaurma/ostriy_kuritsa.jpg', 'Шаурма')
db.add_type('Мини', 23000, 12)
db.add_type('Биг', 26000, 12)

db.add_product('Шаурма с говядиной', 'BACK-896/6-oy/Evos Bot/images/products/shaurma/govyadina.jpg', 'Шаурма')
db.add_type('Мини', 24000, 13)
db.add_type('Биг', 28000, 13)





db.add_product('Гамбургер', 'BACK-896/6-oy/Evos Bot/images/products/burger/gamburger.jpg', 'Бургеры', """Сочная котлета из натуральной говядины, круглые кусочки спелого свежего помидора и маринованного огурца, салат Айсберг", кольца красного сладкого лука под сливочно-томатным соусом в мягкой круглой булочке\n Цена: 23 000 сум""")
db.add_type(None, 23000, 14)

db.add_product('Даблбургер', 'BACK-896/6-oy/Evos Bot/images/products/burger/dablburger.jpg', 'Бургеры', """Две сочные котлеты из натуральной говядины, круглые кусочки спелого свежего помидора и маринованного огурца, салат Айсберг", кольца красного сладкого лука под сливочно-томатным соусом в мягкой булочке\n Цена: 35 000 сум""")
db.add_type(None, 35000, 15)

db.add_product('Чизбургер', 'BACK-896/6-oy/Evos Bot/images/products/burger/chizburger.jpg', 'Бургеры', """Сочная котлета из натуральной говядины, круглые кусочки спелого свежего помидора и маринованного огурца, салат Айсберг, ломтик сыра "Чеддер" под сливочно-томатным соусом в мягкой круглой булочке\n Цена: 25 000 сум""")
db.add_type(None, 25000, 16)

db.add_product('Даблчизбургер', 'BACK-896/6-oy/Evos Bot/images/products/burger/dablchizburger.jpg', 'Бургеры', """Две сочных котлеты из натуральной говядины, круглые кусочки спелого свежего помидора и маринованного огурца, салат Айсберг, два ломтика сыра "Чеддер" под сливочно-томатным соусом в мягкой круглой булочке\n Цена: 39 000 сум""")
db.add_type(None, 39000, 17)

db.add_product('Кидс-Квадрич', 'BACK-896/6-oy/Evos Bot/images/products/burger/kidzkwadrich.jpg', 'Бургеры', """Кидс-Квадрич – квадратный сэндвич в хрустящей сырной чиабатте c добавлением натурального морковного сока, сочной куриной котлетой, сыром Чеддер со сливочно-томатным соусом.\n Цена: 14 000 сум""")
db.add_type(None, 14000, 18)





db.add_product('Саб с курицей', 'BACK-896/6-oy/Evos Bot/images/products/sab/kuritsa.jpg', 'Саб', """Куриное мясо гриль, кольца свежего красного лука, соус "барбекю" с дымком  в удлиненной и пышной булочке\n Цена: 18 000 сум""")
db.add_type(None, 18000, 19)

db.add_product('Саб с курицей и сыром', 'BACK-896/6-oy/Evos Bot/images/products/sab/kuritsa_sir.jpg', 'Саб', """Куриное мясо гриль, кольца свежего красного лука, соус "барбекю" с дымком, ломтик ароматного сыра "Чеддер"  в удлиненной и пышной булочке\n Цена: 20 000 сум""")
db.add_type(None, 20000, 20)

db.add_product('Саб с говядиной и сыром', 'BACK-896/6-oy/Evos Bot/images/products/sab/govyadina_sir.jpg', 'Саб', """Сочная говядина гриль, кольца свежего красного лука, ломтик ароматного  сыра "Чеддер" и соус "барбекю" с дымком  в удлиненной пышной булочке\n Цена: 22 000 сум""")
db.add_type(None, 22000, 21)

db.add_product('Саб с говядиной', 'BACK-896/6-oy/Evos Bot/images/products/sab/govyadina.jpg', 'Саб', """Сочная говядина гриль, кольца свежего красного лука, соус "барбекю" с дымком в удлиненной пышной булочке\n Цена: 20 000 сум""")
db.add_type(None, 20000, 22)





db.add_product('Картофель по-деревенски', 'BACK-896/6-oy/Evos Bot/images/products/kartoshka/derevenskiy.jpg', 'Картошка', """Аппетитные и вкусные крупные ломтики картошки, обжаренные в растительном фритюре с ароматными специями. Попробуйте с любимым соусом!\n Цена: 16 000 сум""")
db.add_type(None, 16000, 23)

db.add_product('Картофель Фри', 'BACK-896/6-oy/Evos Bot/images/products/kartoshka/fri.jpg', 'Картошка', """Вкусные, обжаренные в растительном фритюре и слегка посоленные палочки картофеля. Идеально - в паре с любимым вкусом соуса.\n Цена: 15 000 сум""")
db.add_type(None, 15000, 24)

db.add_product('Наггетсы, 4 шт', 'BACK-896/6-oy/Evos Bot/images/products/kartoshka/naggetsi_4.jpg', 'Картошка', """Хрустящие кусочки куриного филе в  аппетитной панировке. Порция - 4 шт\n Цена: 9 000 сум""")
db.add_type(None, 9000, 25)

db.add_product('Наггетсы, 8 шт', 'BACK-896/6-oy/Evos Bot/images/products/kartoshka/naggetsi_8.jpg', 'Картошка', """Хрустящие кусочки куриного филе в  аппетитной панировке. Порция - 8 шт.\n Цена: 18 000 сум""")
db.add_type(None, 18000, 26)





db.add_product('Хот-дог', 'BACK-896/6-oy/Evos Bot/images/products/hotdog/hotdog.jpg', 'Хот-Доги', """Аппетитная сосиска, кусочки свежего помидора и хрустящего маринованного огурца, листья салата Айсберг под специальным сливочным соусом  в нежном кунжутном багете\n Цена: 15 000 сум""")
db.add_type(None, 15000, 27)

db.add_product('ДаблХот-дог', 'BACK-896/6-oy/Evos Bot/images/products/hotdog/dablhotdog.jpg', 'Хот-Доги', """Две аппетитных сосиски, кусочки свежего помидора и хрустящего маринованного огурца, листья салата Айсберг, кусочки свежего помидора и ломтик сыра "Чеддер" под специальным сливочным  соусом  в нежном кунжутном багете\n Цена: 22 000 сум""")
db.add_type(None, 22000, 28)

db.add_product('Хот-дог детский', 'BACK-896/6-oy/Evos Bot/images/products/hotdog/kidz_hotdog.jpg', 'Хот-Доги', """Кандские сосиски из индейки,  хрустящая луковая стружка-фри, сырный соус в мягкой  булочке\n Цена: 9 000 сум""")
db.add_type(None, 9000, 29)

db.add_product('Хот-дог Мини', 'BACK-896/6-oy/Evos Bot/images/products/hotdog/mini_hotdog.jpg', 'Хот-Доги', """Кандские сосиски из индейки, хрустящая луковая стружка-фри  и томатно-горчичный соус в классической длинной булочке\n Цена: 9 000 сум""")
db.add_type(None, 9000, 30)





db.add_product('Смайлики', 'BACK-896/6-oy/Evos Bot/images/products/sneki/smayliki.jpg', 'Снэки', """Румяные картофельные смайлики - улыбка на весь день!\n Цена: 15 000 сум""")
db.add_type(None, 15000, 31)

db.add_product('Стрипсы', 'BACK-896/6-oy/Evos Bot/images/products/sneki/stripsi.jpg', 'Снэки', """Сочная, нежная курица в хрустящей панировке\n Цена: 20 000 сум""")
db.add_type(None, 20000, 32)





db.add_product('Рис', 'BACK-896/6-oy/Evos Bot/images/products/garniri/ris.jpg', 'Гарниры, салаты, хлеб', """Вкусный и полезный гарнир из белого риса и арпы\n Цена: 8 000 сум""")
db.add_type(None, 8000, 33)

db.add_product('Хлеб', 'BACK-896/6-oy/Evos Bot/images/products/garniri/xleb.jpg', 'Гарниры, салаты, хлеб', """Ароматный свежий хлеб\n Цена: 4 000 сум""")
db.add_type(None, 4000, 34)

db.add_product('Салат', 'BACK-896/6-oy/Evos Bot/images/products/garniri/salat.jpg', 'Гарниры, салаты, хлеб', """Свежие огурцы и красная капуста с добавлением зелени "кашнич", приправленные лимонным соком и восточными специями\n Цена: 8 000 сум""")
db.add_type(None, 8000, 35)

db.add_product('Салат Цезарь', 'BACK-896/6-oy/Evos Bot/images/products/garniri/salat_tsesar.jpg', 'Гарниры, салаты, хлеб', """Кусочки обжаренной в кляре курицы, свежие помидоры, сыр, хрустящие чесночные сухарики, листья салата Айсберг под фирменным соусом «Цезарь»\n Цена: 25 000 сум""")
db.add_type(None, 25000, 36)

db.add_product('Салат Греческий', 'BACK-896/6-oy/Evos Bot/images/products/garniri/salat_grecheskiy.jpg', 'Гарниры, салаты, хлеб', """Свежие томаты и огурцы, терпкие маслины,  нежный сыр “Фетакса” с пряным масляным соусом. Любимая классика в новом исполнении!\n Цена: 24 000 сум""")
db.add_type(None, 24000, 37)





db.add_product('Соус Цезарь', 'BACK-896/6-oy/Evos Bot/images/products/sous/tsesar.jpg', 'Соусы, добавки', """Соус для салата Цезарь\n Цена: 3 000 сум""")
db.add_type(None, 3000, 38)

db.add_product('Соус Греческий', 'BACK-896/6-oy/Evos Bot/images/products/sous/grecheskiy.jpg', 'Соусы, добавки', """Соус для салата Греческий\n Цена: 3 000 сум""")
db.add_type(None, 3000, 39)

db.add_product('Чили соус', 'BACK-896/6-oy/Evos Bot/images/products/sous/chili.jpg', 'Соусы, добавки', """Порция пикантно-острого соуса "чили" . Вес - 25 гр.\n Цена: 3 000 сум""")
db.add_type(None, 3000, 40)

db.add_product('Кетчуп', 'BACK-896/6-oy/Evos Bot/images/products/sous/ketchup.jpg', 'Соусы, добавки', """Порция кетчупа из натуральных свежих томатов со специями.\nВес - 25 гр.\n Цена: 3 000 сум""")
db.add_type(None, 3000, 41)

db.add_product('Чесночный соус', 'BACK-896/6-oy/Evos Bot/images/products/sous/chesnok.jpg', 'Соусы, добавки', """Порция ароматного чесночного соуса. Вес - 25 гр.\n Цена: 3 000 сум""")
db.add_type(None, 3000, 42)

db.add_product('Сырный соус', 'BACK-896/6-oy/Evos Bot/images/products/sous/sir.jpg', 'Соусы, добавки', """Порция густого и аппетитного сырного соуса . Вес - 25 гр.\n Цена: 3 000 сум""")
db.add_type(None, 3000, 43)

db.add_product('Барбекю соус', 'BACK-896/6-oy/Evos Bot/images/products/sous/barbyukyu.jpg', 'Соусы, добавки', """Порция карамелизированного томатного соуса с дымным вкусом. Вес - 25 гр.\n Цена: 3 000 сум""")
db.add_type(None, 3000, 44)

db.add_product('Майонез', 'BACK-896/6-oy/Evos Bot/images/products/sous/mayonez.jpg', 'Соусы, добавки', """Порция классического майонеза. Вес - 25 гр.\n Цена: 3 000 сум""")
db.add_type(None, 3000, 45)





db.add_product('Комбо Плюс', 'BACK-896/6-oy/Evos Bot/images/products/nabori/plyus.jpg', 'Наборы (сеты)', """Порция золотистой картошки фри и стакан "Pepsi"\n Цена: 18 000 сум""")
db.add_type(None, 18000, 46)

db.add_product('Комбо плюс горячий (зеленый чай)', 'BACK-896/6-oy/Evos Bot/images/products/nabori/zeleniy_chay.jpg', 'Наборы (сеты)', """Порция золотистой картошки фри и стакан зеленый лимонный чай\n Цена: 18 000 сум""")
db.add_type(None, 18000, 47)

db.add_product('Донар с говядиной', 'BACK-896/6-oy/Evos Bot/images/products/nabori/donar_govyadina.jpg', 'Наборы (сеты)', """Кусочки сочной говядины гриль, золотистая картошка "фри", рис, натуральный фирменный салат, специальный соус и ароматная лепешка на комбинированном блюде\n Цена: 45 000 сум""")
db.add_type(None, 45000, 48)

db.add_product('ФитКомбо', 'BACK-896/6-oy/Evos Bot/images/products/nabori/fit.jpg', 'Наборы (сеты)', """Нежное куриное мясо гриль, салат "Айсберг", кусочки спелого помидора и свежего огурца, мягкий сыр "Фетакса", легкий сливочный соус Эко в нежно-салатовом лаваше Фиттер. Малокалорийный сок без сахара Dena 0,33л в дополнении\n Цена: 33 000 сум""")
db.add_type(None, 33000, 49)

db.add_product('Донар c курицей', 'BACK-896/6-oy/Evos Bot/images/products/nabori/donar_kuritsa.jpg', 'Наборы (сеты)', """Кусочки куриного мяса гриль, золотистая картошка "фри", рис, натуральный фирменный салат, специальный соус и ароматной лепешкой  на комбинированном блюде\n Цена: 43 000 сум""")
db.add_type(None, 43000, 50)

db.add_product('Комбо плюс горячий (чёрный чай)', 'BACK-896/6-oy/Evos Bot/images/products/nabori/cherniy_chay.jpg', 'Наборы (сеты)', """Порция золотистой картошки фри и стакан чёрный лимонный чай\n Цена: 18 000 сум""")
db.add_type(None, 18000, 51)

db.add_product('Детское комбо', 'BACK-896/6-oy/Evos Bot/images/products/nabori/kidz_kombo.jpg', 'Наборы (сеты)', """Вкуснейший Хот Дог "Детский", натуральный детский сок "Bliss Smile" (200мл) и порция золотистой картошки фри\n Цена: 18 000 сум""")
db.add_type(None, 18000, 52)

db.add_product('Донар-бокс с курицей', 'BACK-896/6-oy/Evos Bot/images/products/nabori/boks_kuritsa.jpg', 'Наборы (сеты)', """Сытная комбинация слоев сочного куриного мяса гриль, хрустящей картошки фри и рассыпчатого риса под белым кунжутным соусом. Удобная компактная, но сытная упаковка!\n Цена: 35 000 сум""")
db.add_type(None, 35000, 53)

db.add_product('Донар-бокс с говядиной', 'BACK-896/6-oy/Evos Bot/images/products/nabori/boks_govyadina.jpg', 'Наборы (сеты)', """Необычайно вкусное сочетание нового фирменного соуса терияки, говядины гриль, хрустящей картошки фри и рассыпчатого риса. Удобная компактная, но сытная упаковка!\n Цена: 37 000 сум""")
db.add_type(None, 37000, 54)





db.add_product('Донат карамельный', 'BACK-896/6-oy/Evos Bot/images/products/desert/karamel.jpg', 'Десерты', """Мягкий нежный донат в карамельной глазури\n Цена: 16 000 сум""")
db.add_type(None, 16000, 55)

db.add_product('Медовик', 'BACK-896/6-oy/Evos Bot/images/products/desert/medovik.jpg', 'Десерты', """Медовый мягкий бисквит со сметанным кремом\n Цена: 18 000 сум""")
db.add_type(None, 18000, 56)

db.add_product('Чизкейк', 'BACK-896/6-oy/Evos Bot/images/products/desert/chizkeyk.jpg', 'Десерты', """Ванильный бисквит с сырно-сливочным кремом\n Цена: 18 000 сум""")
db.add_type(None, 18000, 57)

db.add_product('Донат ягодный', 'BACK-896/6-oy/Evos Bot/images/products/desert/yagodniy.jpg', 'Десерты', """Мягкий нежный донат в клубнично-йогуртовой глазури\n Цена: 16 000 сум""")
db.add_type(None, 16000, 58)





db.add_product('Кофе Глясе', 'BACK-896/6-oy/Evos Bot/images/products/hot_drinks/glyase.jpg', 'Горячие напитки', """Горячий зерновой американо с охлаждающим сливочным мороженым\n Цена: 14 000 сум""")
db.add_type(None, 14000, 59)

db.add_product('Чай зеленый с лимоном', 'BACK-896/6-oy/Evos Bot/images/products/hot_drinks/zeleniy_chay_limon.jpg', 'Горячие напитки', """Зеленый цейлонский крупнолистовой чай со свежим лимоном\n Цена: 6 000 сум""")
db.add_type(None, 6000, 60)

db.add_product('Латте', 'BACK-896/6-oy/Evos Bot/images/products/hot_drinks/latte.jpg', 'Горячие напитки', """Натуральный зерновой кофе, состоящий из трех слоев - молока, эспрессо и взбитого молока.\n Цена: 14 000 сум""")
db.add_type(None, 14000, 61)

db.add_product('Чай черный с лимоном', 'BACK-896/6-oy/Evos Bot/images/products/hot_drinks/cherniy_chay_limon.jpg', 'Горячие напитки', """Черный цейлонский крупнолистовой чай со свежим лимоном,\n Цена: 6 000 сум""")
db.add_type(None, 6000, 62)

db.add_product('Чай черный', 'BACK-896/6-oy/Evos Bot/images/products/hot_drinks/cherniy_chay.jpg', 'Горячие напитки', """Черный цейлонский крупнолистовой чай\n Цена: 5 000 сум""")
db.add_type(None, 5000, 63)

db.add_product('Чай зеленый', 'BACK-896/6-oy/Evos Bot/images/products/hot_drinks/zeleniy_chay.jpg', 'Горячие напитки', """Зеленый цейлонский крупнолистовой чай\n Цена: 5 000 сум""")
db.add_type(None, 5000, 64)

db.add_product('Капучино', 'BACK-896/6-oy/Evos Bot/images/products/hot_drinks/kapuchino.jpg', 'Горячие напитки', """Натуральный зерновой кофе со взбитым молоком на основе эспрессо.\n Цена: 14 000 сум""")
db.add_type(None, 14000, 65)

db.add_product('Американо', 'BACK-896/6-oy/Evos Bot/images/products/hot_drinks/amerikano.jpg', 'Горячие напитки', """Бодрящая классика зернового кофе\n Цена: 12 000 сум""")
db.add_type(None, 12000, 66)

db.add_product('Пунш Малина и смородина', 'BACK-896/6-oy/Evos Bot/images/products/hot_drinks/yagoda.jpg', 'Горячие напитки', """Пунш Малина и смородина - ароматный горячий напиток из натуральных лесных ягод малины и черной смородины. Сочный ягодный вкус для прохладного дня!\n Цена: 15 000 сум""")
db.add_type(None, 15000, 67)





db.add_product('Сок Яблочный без сахара, 0,33л', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/sok_033.jpg', 'Холодные напитки', """Цена: 10 000 сум""")
db.add_type(None, 10000, 68)

db.add_product('Вода с газом 0,5л', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/gaz_water_05.jpg', 'Холодные напитки', """Газированная очищенная питьевая вода, 0,5 л "Chortoq"\n Цена: 5 000 сум""")
db.add_type(None, 5000, 69)

db.add_product('7up разлив', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/7up.jpg', 'Холодные напитки', """Разливной 7up в фирменном бумажном стакане 0,4 л\n Цена: 9 000 сум""")
db.add_type(None, 9000, 70)

db.add_product('Детский сок', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/kidz_sok.jpg', 'Холодные напитки', """Сок из натуральных ягод и фруктов\n Цена: 3 000 сум""")
db.add_type(None, 3000, 71)

db.add_product('Вода без газа 0,5л', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/no_gaz_water_05.jpg', 'Холодные напитки', """Негазированная очищенная питьевая вода, 0,5 л "Chortoq"\n Цена: 5 000 сум""")
db.add_type(None, 5000, 72)

db.add_product('Сок яблочный, 1 литр', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/sok_1l.jpg', 'Холодные напитки', """Яблочный сок, 1 литр\n Цена: 18 000 сум""")
db.add_type(None, 18000, 73)

db.add_product('Стакан 200мл', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/stakan_200ml.jpg', 'Холодные напитки', """Стакан 200мл\n Цена: 300 сум""")
db.add_type(None, 300, 74)

db.add_product('Пепси, бутылка 0,5л', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/pepsi_05.jpg', 'Холодные напитки', """Цена: 10 000 сум""")
db.add_type(None, 10000, 75)

db.add_product('Пепси, бутылка 1,5л', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/pepsi_15.jpg', 'Холодные напитки', """Цена: 19 000 сум""")
db.add_type(None, 19000, 76)

db.add_product('Пепси, стакан 0,4л', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/pepsi_04.jpg', 'Холодные напитки', """Цена: 9 000 сум""")
db.add_type(None, 9000, 77)

db.add_product('Мохито', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/moxito.jpg', 'Холодные напитки', """Мохито – охлаждающий лимонад с соком ароматного лайма, холодной газированной водой и дольками свежего лимона. Цитрусовая формула свежести для жаркого дня!\n Цена: 14 000 сум""")
db.add_type(None, 14000, 78)

db.add_product('Пина колада', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/pina_kolada.jpg', 'Холодные напитки', """Пина колада – освежающий лимонад из мякоти кокоса, ананасового сока и холодной газированной воды. Экзотическая свежесть!\n Цена: 14 000 сум""")
db.add_type(None, 14000, 79)

db.add_product('Миринда, стакан 0,4л', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/mirinda.jpg', 'Холодные напитки', """Разливная Mirinda в фирменном стакане 0,4 л\n Цена: 9 000 сум""")
db.add_type(None, 9000, 80)

db.add_product('Сок вишневый, 1 литр', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/vishnya.jpg', 'Холодные напитки', """Вишневый сок, 1 литр\n Цена: 18 000 сум""")
db.add_type(None, 18000, 81)

db.add_product('Сок апельсиновый, 1 литр', 'BACK-896/6-oy/Evos Bot/images/products/cold_drinks/apelsin.jpg', 'Холодные напитки', """Апельсиновый сок, 1 литр\n Цена: 18 000 сум""")
db.add_type(None, 18000, 82)





db.add_product('Студент-Комбо', 'BACK-896/6-oy/Evos Bot/images/products/kombo/student.jpg', 'Комбо', """Идеальный вариант легко и быстро, а главное экономно перекусить! В состав Студ-Комбо входит мини Хот-Дог, Картофель фри мини, Pepsi 0,4л. в фирменном стакане\n Цена: 18 000 сум""")
db.add_type(None, 18000, 83)

db.add_product('М-Комбо №1', 'BACK-896/6-oy/Evos Bot/images/products/kombo/m_1.jpg', 'Комбо', """Предложения серии M - Комбо подойдут для покупателей, которые хотят сытно покушать. В состав данной серии входят комплексное блюдо, снек и напиток. В состав M - Комбо №1 входит Донар-бокс с говядиной, картофельные смайлики и стакан "Pepsi"\n Цена: 47 000 сум""")
db.add_type(None, 47000, 84)

db.add_product('М-Комбо №2', 'BACK-896/6-oy/Evos Bot/images/products/kombo/m_2.jpg', 'Комбо', """Предложения серии M - Комбо подойдут для покупателей, которые хотят сытно покушать. В состав данной серии входят комплексное блюдо, снек и напиток. В состав M - Комбо №2 входит Донар-бокс с курицей, картофельные смайлики и стакан "Pepsi"\n Цена: 47 000 сум""")
db.add_type(None, 47000, 85)

db.add_product('S-Комбо №1', 'BACK-896/6-oy/Evos Bot/images/products/kombo/s_1.jpg', 'Комбо', """Комбо серии S подойдут для покупателей, которые хотят быстро, выгодно и разнообразно перекусить. В состав предложений этой серии входят мини-версии самых популярных блюд. В S-комбо №1 входит: лаваш мини с говядиной, порция золотистой картошки фри мини и стакан "Pepsi"\n Цена: 30 000 сум""")
db.add_type(None, 30000, 86)

db.add_product('S-Комбо №2', 'BACK-896/6-oy/Evos Bot/images/products/kombo/s_2.jpg', 'Комбо', """Комбо серии S подойдут для покупателей, которые хотят быстро, выгодно и разнообразно перекусить. В состав предложений этой серии входят мини-версии самых популярных блюд. В S-комбо №2 входит: лаваш мини с курицей, порция золотистой картошки фри мини и стакан "Pepsi"\n Цена: 30 000 сум""")
db.add_type(None, 30000, 87)

db.add_product('S-Комбо №3', 'BACK-896/6-oy/Evos Bot/images/products/kombo/s_3.jpg', 'Комбо', """Комбо серии S подойдут для покупателей, которые хотят быстро, выгодно и разнообразно перекусить. В состав предложений этой серии входят мини-версии самых популярных блюд. В S-комбо №3 входит: мини-шаурма с говядиной, порция золотистой картошки фри мини и стакан "Pepsi"\n Цена: 30 000 сум""")
db.add_type(None, 30000, 88)

db.add_product('S-Комбо №4', 'BACK-896/6-oy/Evos Bot/images/products/kombo/s_4.jpg', 'Комбо', """Комбо серии S подойдут для покупателей, которые хотят быстро, выгодно и разнообразно перекусить. В состав предложений этой серии входят мини-версии самых популярных блюд. В S-комбо №4 входит: мини-шаурма с курицей, порция золотистой картошки фри мини и стакан "Pepsi"\n Цена: 30 000 сум""")
db.add_type(None, 30000, 89)

db.add_product('Дабл-Комбо №1', 'BACK-896/6-oy/Evos Bot/images/products/kombo/dabl_1.jpg', 'Комбо', """Серия Дабл-комбо - выгодное решение на двоих! В Дабл-Комбо №1 входит двойная порция лаваша с говядиной и хрустящих картофельных смайликов и, конечно же, 2 стакана «Pepsi»\n Цена: 80 000 сум""")
db.add_type(None, 80000, 90)

db.add_product('Дабл-Комбо №2', 'BACK-896/6-oy/Evos Bot/images/products/kombo/dabl_2.jpg', 'Комбо', """Серия Дабл-комбо - выгодное решение на двоих! В Дабл-Комбо №2 входит двойная порция лаваша с курицей и хрустящих картофельных смайликов и, конечно же, 2 стакана «Pepsi».\n Цена: 80 000 сум""")
db.add_type(None, 80000, 91)

db.add_product('Дабл-Комбо №3', 'BACK-896/6-oy/Evos Bot/images/products/kombo/dabl_3.jpg', 'Комбо', """Серия Дабл-комбо - выгодное решение на двоих! В Дабл-Комбо №3 входит двойная порция шаурма с говядиной и  картошки по-деревенскии, конечно же, 2 стакана «Pepsi».\n Цена: 80 000 сум""")
db.add_type(None, 80000, 92)

db.add_product('Дабл-Комбо №4', 'BACK-896/6-oy/Evos Bot/images/products/kombo/dabl_4.jpg', 'Комбо', """Серия Дабл-комбо - выгодное решение на двоих! В Дабл-Комбо №4 входит две порции хрустящей шаурмы с курицей, двойная порция картошки по-деревенски, два стакана "Pepsi".\n Цена: 80 000 сум""")
db.add_type(None, 80000, 93)

db.add_product('Семейный-Комбо №1', 'BACK-896/6-oy/Evos Bot/images/products/kombo/semeyniy_1.jpg', 'Комбо', """СериСемейное комбо - выгодное удовольствие для всей семьи! В Семейный-Комбо№1 входит: 2 (два) стандартных + 2 (два) мини-лаваша с говядиной, 2 (две) порции хрустящей картошки фри, две (2) порции веселых картофельных смайликов, которые порадуют детей и взрослых. В состав набора входит 4 стакана "Pepsi".\n Цена: 150 000 сум""")
db.add_type(None, 150000, 94)

db.add_product('Семейный-Комбо №2', 'BACK-896/6-oy/Evos Bot/images/products/kombo/semeyniy_2.jpg', 'Комбо', """Семейное комбо - выгодное удовольствие для всей семьи! В Семейный-Комбо№1 входит: 2 (два) стандартных + 2 (два) мини-лаваша с курицей, 2 (две) порции хрустящей картошки фри, две (2) порции веселых картофельных смайликов, которые порадуют детей и взрослых. В состав набора входит 4 стакана "Pepsi".\n Цена: 150 000 сум""")
db.add_type(None, 150000, 95)

db.add_product('Комбо Плюс 7up', 'BACK-896/6-oy/Evos Bot/images/products/kombo/plyus_7up.jpg', 'Комбо', """Порция золотистой картошки фри и стакан 7up\n Цена: 18 000 сум""")
db.add_type(None, 18000, 96)