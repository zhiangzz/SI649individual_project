import streamlit as st
import altair as alt 
import pandas as pd
from PIL import Image

public_ela = pd.read_csv("ny-ela-results-2013-2019-public-all.csv")
public_math = pd.read_csv("ny-math-results-2013-2019-public-all.csv")

# Just for you to explore the features [COMMENT OUT WHEN SUBMITTING IT] 
# st.write(movies_test) ~ to see the dataset


#Title
st.title("Individual Project by Zhiang Zhang")


### Making of all charts [ Add altair code chunk for each of the specific charts]

# Visualization 1
Vis1 = Image.open("layout.jpg")

# st.write(Vis1)
# Visualization 2

Vis2 = Image.open("vis2.png")
# st.write(Vis2)

# Visualization 3
#TODO: Replicate Vis 3 
# NY = public[public['location_city']=='NEW YORK']
# NY['pupil_teacher_ratio'] == NY["pupil_teacher_ratio"].replace('?€?',0)
# NY[NY['pupil_teacher_ratio']=='†']
public_math.columns = public_math.columns.str.lower().str.replace(' ','_')
public_ela.columns = public_ela.columns.str.lower().str.replace(' ','_')
ps8=public_math[(public_math["school_name"]=='P.S. 008 ROBERT FULTON')&(public_math["grade"]=='All Grades')]
ps8_ela=public_ela[(public_ela["school_name"]=='P.S. 008 ROBERT FULTON')&(public_ela["grade"]=='All Grades')]
ps8_bar=alt.Chart(ps8).transform_fold(
    ["%_level_1","%_level_2","%_level_3","%_level_4"],
    as_=["level","percent"]
).mark_bar().encode(
    x = alt.X('year:O'),
    y = alt.Y('percent:Q',title='Math Test Result in P.S.8'),
    color='level:N'  
).properties(width=300)

selection_single = alt.selection_single(encodings=["color"])

colorCondition1 = alt.condition(selection_single,"level:N",alt.value("lightgray"))

c1 = ps8_bar.add_selection(selection_single).encode(
    color= colorCondition1
)

ps8_bar2=alt.Chart(ps8_ela).transform_fold(
    ["%_level_1","%_level_2","%_level_3","%_level_4"],
    as_=["level","percent"]
).mark_bar().encode(
    x = alt.X('year:O'),
    y = alt.Y('percent:Q',title='ELA Test Result in P.S.8'),
    color='level:N'  
).properties(width=300)

selection_single = alt.selection_single(encodings=["color"])

colorCondition1 = alt.condition(selection_single,"level:N",alt.value("lightgray"))

c2 = ps8_bar2.add_selection(selection_single).encode(
    color= colorCondition1
)
ps307=public_math[(public_math["school_name"]=='P.S. 307 DANIEL HALE WILLIAMS')&(public_math["grade"]=='All Grades')]
ps307_ela=public_ela[(public_ela["school_name"]=='P.S. 307 DANIEL HALE WILLIAMS')&(public_ela["grade"]=='All Grades')]
ps307_bar=alt.Chart(ps307).transform_fold(
    ["%_level_1","%_level_2","%_level_3","%_level_4"],
    as_=["level","percent"]
).mark_bar().encode(
    x = alt.X('year:O'),
    y = alt.Y('percent:Q',title='Math Test Result in P.S.307'),
    color='level:N'
).properties(width=300)
selection_single = alt.selection_single(encodings=["color"])

colorCondition1 = alt.condition(selection_single,"level:N",alt.value("lightgray"))

c3 = ps307_bar.add_selection(selection_single).encode(
    color= colorCondition1
)


ps307_bar2 = alt.Chart(ps307_ela).transform_fold(
    ["%_level_1","%_level_2","%_level_3","%_level_4"],
    as_=["level","percent"]
).mark_bar().encode(
    x = alt.X('year:O'),
    y = alt.Y('percent:Q',title='ELA Test Result in P.S.307'),
    color='level:N'  
).properties(width=300)

selection_single = alt.selection_single(encodings=["color"])

colorCondition1 = alt.condition(selection_single,"level:N",alt.value("lightgray"))

c4 = ps307_bar2.add_selection(selection_single).encode(
    color= colorCondition1
)
Vis3=((c1|c3).resolve_scale(x="shared"))&((c2|c4).resolve_scale(x="shared"))
# st.write(Vis3)
# Visualization 4

add_selectbox = st.sidebar.selectbox(
    "Select a visualization to display",
    ("Vis1","Vis2","Vis3")
)
if add_selectbox=="Vis1":
    st.image(Vis1)
elif add_selectbox=="Vis2":
    st.image(Vis2)
elif add_selectbox=="Vis3":
    st.write(Vis3)

