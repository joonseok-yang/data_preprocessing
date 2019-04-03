import pandas as pd
import matplotlib.pyplot as plt


def select_menu():
    return input("""\n제품수량관리
===========
1. 입력
2. 출력
3. 검색
4. 정렬
5. 차트보기(바차트)
6. 종료\n
메뉴를 선택하세요: """)


def search_item(sr):
    print("search item")
    if len(sr) == 0:
        print("No item")
        return
    format_print(sr[sr.index.str.contains(input("Product Name: "))])


def format_print(sr):
    print("=" * 30)
    print("%10s%10s" % ('name', 'quantity'))
    print("=" * 30)
    for k, v in sr.items():
        print("%10s%10d" % (k, v))


def print_items(sr):
    print("print items")
    if len(sr) == 0:
        print("No item")
        return
    format_print(sr)


def get_items(sr):
    while True:
        print()
        product_name = input("Product Name: ")
        quantity = int(input("Quantity: "))

        sr[product_name] = quantity
        if input("More Items (y/n)").lower() != 'y':
            break


def print_sorted_list(sr):
    print("sort index")
    if len(sr) == 0:
        print("No item")
        return
    format_print(sr.sort_index())


def show_chart(sr):
    if len(sr) == 0:
        print("No item")
        return
    sr.plot(kind='bar')
    plt.show()


def main():

    fcns = {'1': get_items, '2': print_items, '3': search_item, '4': print_sorted_list, '5': show_chart}
    sr = pd.Series()

    while True:
        menu = select_menu()
        todo = fcns.get(menu, None)
        if not todo:
            break
        else:
            todo(sr)


if __name__ == "__main__":
    main()
