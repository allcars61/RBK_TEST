import pandas as pd
import matplotlib.pyplot as plt

# load data from Excel file
xlsx = pd.read_excel(
    "Аналитик данных _Тестовое задание _РБК.xlsx", sheet_name="Выгрузка"
)
articles = pd.read_excel(
    "Аналитик данных _Тестовое задание _РБК.xlsx", sheet_name="База публикаций"
)

# process view data: exclude views with URLs containing certain patterns
if "Адрес страницы" in xlsx.columns:
    valid_views = ~xlsx["Адрес страницы"].str.contains(
        r"test\.pro|test\.v2\.pro|feature\-rbcnews|\/preview\/|staging\.pro|staging\.v2\.pro"
    )
    view_counts = xlsx[valid_views]["Просмотры"]
else:
    valid_views = pd.Series([True] * len(xlsx))
    view_counts = xlsx["Просмотры"]

# merge "Выгрузка" and "База публикаций" tables on "URL"
articles_views = articles.merge(
    xlsx, left_on="URL", right_on="Адрес страницы", how="left"
)

# create a table of top 20 articles by views with their titles
top20_articles = (
    articles_views.loc[valid_views]
    .groupby(["ID публикации", "Заголовок материала"])["Просмотры"]
    .sum()
    .nlargest(20)
)
top20_articles = top20_articles.reset_index()

# create dynamic visualization of the table or graph
try:
    fig, ax = plt.subplots()
    top20_articles.plot.bar(x="Заголовок материала", y="Просмотры", ax=ax)
    ax.set_title("ТОП-20 материалов по просмотрам")
    ax.set_xlabel("Заголовок материала")
    ax.set_ylabel("Количество просмотров")

    fig.set_size_inches(12, 13)  # изменяем размеры графика
    ax.set_position([0.1, 0.5, 0.8, 0.45])  # изменяем положение и размеры осей графика

    plt.show()

    # add clickable URLs to the table
    top20_articles["Заголовок материала"] = (
        '<a href="'
        + top20_articles["URL к материалу"]
        + '">'
        + top20_articles["Заголовок материала"]
        + "</a>"
    )
    top20_articles = top20_articles.drop(columns=["URL к материалу"])
    top20_articles = top20_articles.to_html(escape=False)
except KeyError:
    # if there is no "URL к материалу" column
    top20_articles = top20_articles.to_html(index=False)

# save the resulting table or graph to a file
with open("result.html", "w", encoding="utf-8") as file:
    file.write(top20_articles)
