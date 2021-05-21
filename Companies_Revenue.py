import pandas as pd
import plotly.express as px

df_list = pd.read_html( # Note - read_html() returns a list of DataFrames
    "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue",
    match="Breakdown by country"
)
#print('df_list', df_list)

df = df_list[0]
#print('df', df)

top_10 = df.loc[0:10,['Country','Companies']] # Top 10
plot_data = top_10.head(10)[::-1] # Largest on top
print('TOP 10\n', plot_data)

companies_figure = px.bar(plot_data, x=('Companies'), y=('Country'))

companies_figure.update_layout(
    title_text="Home Countries of Largest Companies by Revenue",
    xaxis_title_text="No. of Companies",
    yaxis_title_text="Home Country",
    legend_title_text="",
    height=500
)
companies_figure.update_traces(marker_color="royalblue")

companies_figure.show()
