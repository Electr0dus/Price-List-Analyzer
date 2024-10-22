<b>Анализатор прайс-листов</b>
<div>Программа загрузаеж данные из всех прайс-листов и предоставляет интерфейс для поиска товара по фрагменту названия с сорторовкой по цене за килогорамм.
Интерфейс для поиска реализован через консоль, циклически получая информацию от пользователя.
Если введено слово <em>"exit"</em>, то цикл обмена с пользователем завершается, программа выводит сообщение о том, что работа закончена и завершает свою работу. 
В противном случае введенный текст считается текстом для поиска.
Предусмотрен вывод массива данных в текстовый файл в формате <b>html</b>.
Программа должна вывести список найденных позиций в виде таблицы:</div>

<div>№     Наименование                              цена  вес     файл     цена за кг.</div>
<div>1     филе гигантского кальмара                  617    1  price_0.csv  617.0</div>
<div>2     филе гигантского кальмара                  639    1  price_4.csv  639.0</div>
<div>3     филе гигантского кальмара                  639    1  price_6.csv  639.0</div>
<div>4     филе гигантского кальмара                  683    1  price_1.csv  683.0</div>
<div>5     филе гигантского кальмара                 1381    2  price_5.csv  690.5</div>
<div>6     кальмар тушка                             3420    3  price_3.csv  1140.0</div>
<div>7     кальмар тушка                             4756    4  price_0.csv  1189.0</div>

<div>Пример работы:</div>
![image]([https://github.com/user-attachments/assets/eef59a56-665b-4ab5-8b38-5d3b22eecab0](https://github.com/Electr0dus/Price-List-Analyzer/blob/main/example.png))
