# import pandas as pd
# import numpy as np
import streamlit as st
import typer
from PIL import Image
import pandas as pd
import joblib


def app() -> None:
    # Title and info
    st.sidebar.title("Survival on the Titanic")

    st.sidebar.info(
        "Enter information in the form to create a fictional character, the model will then determine the chance of them surviving on the HMS Titanic.")
    image_1 = Image.open("./imgs/titanic-dock.jpg")
    st.sidebar.image(image_1, caption="HMS Titanic in the dock", use_column_width=True)

    image_2 = Image.open("./imgs/titanic-lifeboat.jpg")
    st.sidebar.image(image_2, caption="Survivers from the Titanic in lifeboats", use_column_width=True)

    # Input section
    st.title("Please fill in the details below:")
    title = st.selectbox(
        'Title ',
        ('Miss', 'Rev', 'Master', 'Countess', 'Mrs', 'Mr'))
    first_name = st.text_input(
        "First name"
    )
    surname = st.text_input(
        "Surname"
    )
    age = st.number_input(
        "Age (in whole years):"
    )

    sex = st.selectbox(
        'Sex (In records of the name this was recorded as male or female)',
        ('Female', 'Male'))

    # traveling with children or parents
    # Traveling with sibling or spouse
    # ticket
    # Port of boarding

    # Create dataframe
    character = pd.DataFrame(
        [[3.000000, 14.458300, 29.699118, 0.000000, 1.000000, 1.000000, 1.000000, 0.000000, 0.000000, 0.000000,
          0.000000,
          0.000000, 0.000000, 0.000000]],
        columns=['Pclass', 'Fare', 'Age', 'SibSp', '21', '71', '27', '30', '50', '1', '41', '2', '22', '26']
    )
    # Load model
    titanic_model = joblib.load("./artifacts/titanic_clf.joblib")

    # Run predictions
    if st.button("Predict chance of survical"):
        prediction = titanic_model.predict(character)
        survival = 'Died'
        if prediction == [1]:
            survival = 'Survived'
        st.title(f'Prediction: {survival}')
        # st.text("You survived!")
        # y = feature_engineering.transform([review])
        # prediction = classifier.predict(y)
        # probability = np.round(np.amax(classifier.predict_proba(y)), 2)
        #
        # def convert(prediction: int) -> str:
        #     return "Positive" if prediction == 1 else "Negative"
        #
        # if review != write_here:
        #     st.success(
        #         f"*Sentiment prediction*: **{convert(prediction).upper()}** with probability {100 * probability}%"
        #     )
        #     st.balloons()
        # else:
        #     st.error("You need to input a review for classification!")
    else:
        st.info(
            "**Enter the fields* above and **press the button** to predict the chance of survival."
        )


if __name__ == "__main__":
    # Need to do this try/except due to Streamlit weirdness
    # See https://github.com/streamlit/streamlit/issues/468
    try:
        typer.run(app)
    except SystemExit as e:
        if e.code != 0:
            raise
