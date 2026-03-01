import plotly.express as px

def line_chart(df):
    fig = px.line(df)
    return fig
