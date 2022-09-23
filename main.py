from  class_Storage import *

def main():
    stor_items = {'печенье': 2, 'кофе': 7, 'чай': 2, 'сахар': 2, 'картофель': 2}
    shop_items = {'печенье': 2, 'кофе': 7 }
    stor = Store(stor_items)
    shop = Shop(shop_items)

    from_where = input('От куда будет осуществляться доставка - склад или  магазин')
    to = input('Куда доставить')
    product = input('Какой продукт доставить')
    amount = int(input('Введите количество доставляемого продукта'))
    conclusion = Request(from_where, to, amount, product)
    print(conclusion.__repr__())


    if from_where == 'склад':
        if stor.remove(product, amount):
            stor.remove(product, amount)
            if shop.add(product, amount):
                print(f'Курьер забирает {amount} {product} из {from_where}')
                print(f'Курьер везет {amount} {product} со {from_where} в {to}')
                print(f'Курьер доставил {amount} {product} в {to}')
            else:
                print('В магазине недостаточно места, попобуйте что то другое')
        else:
            print('Не хватает на складе, попробуйте заказать меньше')



    elif from_where == 'магазин':
            shop.remove(product, amount)
            if stor.add(product, amount):
                stor.add(product, amount)
                print(f'Курьер забирает {amount} {product} из {from_where}')
                print(f'Курьер везет {amount} {product} со {from_where} в {to}')
                print(f'Курьер доставил {amount} {product} в {to}')
            else:
                print('На складе недостаточно места, попобуйте что то другое')




    print(f'В складе хранится:')
    stor.get_items()
    print(f'В магазине хранится:')
    shop.get_items()


if __name__ == "__main__":
    main()

