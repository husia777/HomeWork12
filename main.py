from  class_Storage import *

def main(stor_items, shop_items):
    while True:
        process = input('go для итерации или exit для выхода')
        if process.lower() == 'go':
            stor = Store(stor_items)
            shop = Shop(shop_items)

            print(f'В складе хранится:')
            stor.get_items

            print(f'В магазине хранится:')
            shop.get_items

            from_where = input('От куда будет осуществляться доставка - склад или  магазин')
            to = input('Куда доставить')
            product = input('Какой продукт доставить')
            amount = int(input('Введите количество доставляемого продукта'))
            conclusion = Request(from_where, to, amount, product)
            print(conclusion.__repr__())


            if from_where == 'склад':
                if product in stor_items:
                    try:
                        stor.remove(product, amount)
                        shop.add(product, amount)
                        print(f'Курьер забирает {amount} {product} из {from_where}')
                        print(f'Курьер везет {amount} {product} со {from_where} в {to}')
                        print(f'Курьер доставил {amount} {product} в {to}')
                    except:
                        print('В магазине недостаточно места или не хватает на складе, попобуйте заказать что то другое  или заказать меньше')
                else:
                    print('Такого продукта нету на складе')


            elif from_where == 'магазин':
                if product in shop_items:
                    try:
                        shop.remove(product, amount)
                        stor.add(product, amount)
                        print(f'Курьер забирает {amount} {product} из {from_where}')
                        print(f'Курьер везет {amount} {product} со {from_where} в {to}')
                        print(f'Курьер доставил {amount} {product} в {to}')
                    except:
                        print('На складе недостаточно места или не хватает в магазине, попобуйте заказать что то другое  или заказать меньше')
                else:
                    print('Такого продукта нету в магазине')

            print(f'В складе хранится:')
            stor.get_items

            print(f'В магазине хранится:')
            shop.get_items

            main(stor_items, shop_items)

        elif process.lower() == 'exit':
            print(f'В складе хранится:')
            stor.get_items

            print(f'В магазине хранится:')
            shop.get_items
            break



stor_items = {'печенье': 2, 'кофе': 7, 'чай': 2, 'сахар': 2, 'картофель': 2}
shop_items = {'печенье': 2, 'кофе': 7 }
if __name__ == "__main__":
    main(stor_items, shop_items)

