# 4. Все emails у которых есть слово test вывести в другой список
# l = ['webtest1@gmail.com',
#      'alex_dr5@gmail.com',
#      'elena_viktorovna@gmail.com',
#      'infotest@gmail.com',
#      'sigmatesst@gmail.com',
#      'planet.dollsatest@gmail.com',
#      'loadtestsinfo@gmail.com',
#      'straightwaytest@gmail.com',
#      'test.of.tests@gmail.com',
#      'bigmac@gmail.com',
#      'bigmactest@gmail.com',
#      'kfc_test_supply@gmail.com',
#      'cyberdesk@gmail.com',
#      'supportonlinetest@gmail.com'
#      ]

l = ['webtest1@gmail.com',
     'alex_dr5@gmail.com',
     'elena_viktorovna@gmail.com',
     'infotest@gmail.com',
     'sigmatesst@gmail.com',
     'planet.dollsatest@gmail.com',
     'loadtestsinfo@gmail.com',
     'straightwaytest@gmail.com',
     'test.of.tests@gmail.com',
     'bigmac@gmail.com',
     'bigmactest@gmail.com',
     'kfc_test_supply@gmail.com',
     'cyberdesk@gmail.com',
     'supportonlinetest@gmail.com'
      ]
l_test = []
for i in l:
    if 'test' in i:
        l_test.append(i)
print(l_test)

# результат
# ['webtest1@gmail.com', 'infotest@gmail.com', 'planet.dollsatest@gmail.com', 'loadtestsinfo@gmail.com',
# 'straightwaytest@gmail.com', 'test.of.tests@gmail.com', 'bigmactest@gmail.com', 'kfc_test_supply@gmail.com', 'supportonlinetest@gmail.com']
        
"""
# 2 вариант с выводом в столбик и не списком
l = ['webtest1@gmail.com',
     'alex_dr5@gmail.com',
     'elena_viktorovna@gmail.com',
     'infotest@gmail.com',
     'sigmatesst@gmail.com',
     'planet.dollsatest@gmail.com',
     'loadtestsinfo@gmail.com',
     'straightwaytest@gmail.com',
     'test.of.tests@gmail.com',
     'bigmac@gmail.com',
     'bigmactest@gmail.com',
     'kfc_test_supply@gmail.com',
     'cyberdesk@gmail.com',
     'supportonlinetest@gmail.com'
      ]
for i in l:
    if 'test' in i:
        print(i)

# результат
    webtest1@gmail.com
    infotest@gmail.com
    planet.dollsatest@gmail.com
    loadtestsinfo@gmail.com
    straightwaytest@gmail.com
    test.of.tests@gmail.com
    bigmactest@gmail.com
    kfc_test_supply@gmail.com
    supportonlinetest@gmail.com
"""
