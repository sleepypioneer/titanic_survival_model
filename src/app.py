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
    image_1 = Image.open("imgs/titanic-dock.jpg")
    st.sidebar.image(image_1, caption="HMS Titanic in the dock", use_column_width=True)

    image_2 = Image.open("imgs/titanic-lifeboat.jpg")
    st.sidebar.image(image_2, caption="Survivers from the Titanic in lifeboats", use_column_width=True)

    # Input section
    st.title("Please fill in the details below:")
    title = st.selectbox(
        'Title ',
        ('Mr', 'Mrs', 'Miss', 'Master', 'Don', 'Rev', 'Dr', 'Mme', 'Ms',
         'Major', 'Lady', 'Sir', 'Mlle', 'Col', 'Capt', 'Countess',
         'Jonkheer'))

    male_titles = ['Mr', 'Master', 'Don', 'Rev', 'Major', 'Sir','Col', 'Capt','Jonkheer']
    female_titles = ['Mrs', 'Miss', 'Mme', 'Ms', 'Lady', 'Mlle','Countess']

    x0_Mr, x0_Mrs = 0,0
    if title in male_titles:
        x0_Mr = 1
    elif title in female_titles:
        x0_Mrs = 1

    first_name = st.text_input(
        "First name"
    )
    surname = st.text_input(
        "Surname"
    )
    age = st.number_input(
        "Age (in whole years):"
    )
    age = int(age)

    travelling_with_family = st.selectbox(
        'Will you be traveling with family members? How many including yourself with your group be?',
        ('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Eleven'))

    familySize = 1

    if travelling_with_family == 'Two':
        familySize = 2
    elif travelling_with_family == 'Three':
        familySize = 3
    elif travelling_with_family == 'Four':
        familySize = 3
    elif travelling_with_family == 'Five':
        familySize = 3
    elif travelling_with_family == 'Six':
        familySize = 3
    elif travelling_with_family == 'Seven':
        familySize = 3
    elif travelling_with_family == 'Eight':
        familySize = 3
    elif travelling_with_family == 'Nine':
        familySize = 3
    elif travelling_with_family == 'Ten':
        familySize = 3
    elif travelling_with_family == 'Eleven':
        familySize = 3
    else:
        familySize = 0

    ticket = st.selectbox(
        'Select a ticket for your journey',
        ('1st Class - 500', '1st Class - 256', '2nd Class - 135', '2nd Class - 35', '3rd Class - 25', '3rd Class - 10'))

    p_class = 3
    fare = 0
    if ticket == '1st Class - 500':
        p_class = 1
        fare = 500
    elif ticket == '1st Class - 256':
        p_class = 1
        fare = 256
    elif ticket == '2nd Class - 135':
        p_class = 2
        fare = 135
    elif ticket == '2nd Class - 35':
        p_class = 2
        fare = 35
    elif ticket == '3rd Class - 25':
        p_class = 3
        fare = 25
    elif ticket == '3rd Class - 10':
        p_class = 3
        fare = 10
    else:
        p_class = 3
        fare = 0

    sex = st.selectbox(
        'Sex (In records of the name this was recorded as male or female)',
        ('Female', 'Male'))

    x1_female, x1_male = 0, 0

    if sex == 'Female':
        x1_female = 1
    elif sex == 'Male':
        x1_male = 1

    # traveling with children or parents
    # Traveling with sibling or spouse
    # ticket
    # Port of boarding

    # Create dataframe
    character = pd.DataFrame(
        [[p_class, x1_female, x1_male, age, familySize, fare, x0_Mr, x0_Mrs]],
        columns=[
            'Pclass', 'x1_female', 'x1_male',
            'Age', 'FamilySize', 'Fare', 'x0_Mr', 'x0_Mrs'
        ]
    )
    # Load model
    titanic_model = joblib.load("./artifacts/titanic_refined_clf.joblib")

    # Run predictions
    if st.button("Predict chance of survival"):
        prediction = titanic_model.predict(character)
        survival = 'Died'
        if prediction == [1]:
            survival = 'Survived'
        st.title(f'Prediction: {survival} \n Model has 83% accuracy')
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
