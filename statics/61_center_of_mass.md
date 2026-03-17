# Центр тяжести

<details><summary><b>В чём сила, брат?</b></summary><img width="1020" height="1139" alt="image" src="https://github.com/user-attachments/assets/6dccbdb5-015c-4e12-a618-d494fc91bb98" />
</details>

## Центр тяжести тела
На каждую частицу тела, находящегося вблизи земной поверхности, действует направленная вертикально вниз сила тяжести.
Для тел, размеры которых малы по сравнению с земным радиусом, силы тяжести, действующие на частицы тела, можно считать параллельными и сохраняющими постоянное значение при любых поворотах тела.
**Координаты центра тяжести**
```math
\begin{cases} x_c = \frac{\sum P_k \cdot x_k}{P} \\ y_c = \frac{\sum P_k \cdot y_k}{P} \\ z_c = \frac{\sum P_k \cdot z_k}{P} \end{cases}
```
**Модуль силы тяжести:**
```math
P = \sum_{k=1}^{n} P_k
```
<img width="794" height="556" alt="image" src="https://github.com/user-attachments/assets/730e9ff4-8c94-43d8-befe-d694c5a35d80" />

## Центр тяжести плоской фигуры

Пусть тело представляет собой однородную тонкую пластинку. Обозначим $F$ – площадь фигуры, ограничивающей пластинку. Вес однородной пластинки выразится формулой:
```math
𝑃 = 𝛾\cdot 𝐹
```
где 𝛾 – вес единицы площади, а вес частицы:
```math
𝑃_𝑘= 𝛾\cdot ∆𝐹_𝑘
```
где $∆𝐹_𝑘$ - площадь рассматриваемой частицы.
```math
x_c = \frac{\sum P_k \cdot x_k}{P} = \frac{\sum 𝛾 \cdot ∆𝐹_𝑘 \cdot x_k}{𝛾\cdot 𝐹} = \frac{\sum ∆𝐹_𝑘 \cdot x_k}{𝐹}
```
В пределе при $∆𝐹_𝑘→0$ формулы для определения координат центра тяжести однородной пластинки принимают вид:
```math
x_c = \frac{1}{F} \int{xdF}
```
```math
y_c = \frac{1}{F} \int{ydF}
```

<img width="814" height="557" alt="image" src="https://github.com/user-attachments/assets/73914749-ddcc-42b6-b140-ed3439c97b9c" />

## Центр тяжести линии
Вес проволоки
```math
𝑃 =𝛾\cdot 𝐿
```
где L = AB, а 𝛾 – вес единицы длины проволоки.
Разобьем проволоку на элементарные участки $∆𝐿_𝑘$. Вес каждого участка:
```math
𝑃_𝑘= 𝛾\cdot ∆𝐿_𝑘
```
<img width="792" height="514" alt="image" src="https://github.com/user-attachments/assets/abae4fd9-ce13-4cd8-b458-8c1d794c0c96" />

Подставляя эти величины в формулы для координат центра тяжести тела, получаем:
```math
x_c = \frac{\sum P_k \cdot x_k}{P} = \frac{\sum 𝛾 \cdot ∆L_𝑘 \cdot x_k}{𝛾\cdot L} = \frac{\sum ∆L_𝑘 \cdot x_k}{L}
```
или в интегральном исчислении:
```math
x_c = \frac{1}{L} \int{xdL}
```
```math
y_c = \frac{1}{L} \int{ydL}
```
```math
z_c = \frac{1}{L} \int{zdL}
```
