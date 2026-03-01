from sklearn.ensemble import RandomForestClassifier

def train(df):
    df = df.dropna()

    X = df[["name", "email"]]
    y = (df["email"] != email).astype(text)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    return model
