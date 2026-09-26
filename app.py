import streamlit as st

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="Railway Ticket Booking",
    page_icon="🚆",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>
    .main {
        background-color: #f5f7fa;
    }

    .title {
        text-align: center;
        color: #1f4e79;
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666666;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .booking-box {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-top: 10px;
    }

    .section-title {
        color: #1f4e79;
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 15px;
    }

    .success-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #e8f5e9;
        border-left: 5px solid #2e7d32;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 45px;
        font-size: 16px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown(
    '<div class="title">🚆 Railway Ticket Booking</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Book your train journey quickly and easily</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------------------------------------------
# BOOKING FORM
# ---------------------------------------------------
with st.container():

    st.markdown(
        '<div class="section-title">👤 Passenger Details</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Enter Name",
            placeholder="Enter passenger name"
        )

        age = st.number_input(
            "Enter Age",
            min_value=5,
            max_value=105,
            value=18
        )

        gender = st.selectbox(
            "Gender",
            options=["Male", "Female", "Other"]
        )

    with col2:
        marital_status = st.radio(
            "Marital Status",
            options=["Single", "Married", "Separated"],
            horizontal=True
        )

        meal = st.multiselect(
            "Select Meal",
            options=[
                "Vada Pav",
                "Misal Pav",
                "Pav Bhaji",
                "Pulav"
            ],
            max_selections=2
        )

        coach = st.segmented_control(
            "Select Coach",
            options=[
                "3 Tier",
                "2 Tier",
                "First Class",
                "General"
            ]
        )


st.divider()


# ---------------------------------------------------
# JOURNEY DETAILS
# ---------------------------------------------------
with st.container():

    st.markdown(
        '<div class="section-title">🛤️ Journey Details</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        from_date = st.date_input(
            "From Date"
        )

    with col2:
        boarding_time = st.time_input(
            "Boarding Time"
        )


st.divider()


# ---------------------------------------------------
# FEEDBACK
# ---------------------------------------------------
with st.container():

    st.markdown(
        '<div class="section-title">⭐ Your Experience</div>',
        unsafe_allow_html=True
    )

    rating = st.feedback(
        "stars"
    )


st.divider()


# ---------------------------------------------------
# BUTTON
# ---------------------------------------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    if st.button(
        "🎫 Book Ticket",
        type="primary"
    ):

        if name == "":
            st.warning("⚠️ Please enter passenger name.")

        elif coach is None:
            st.warning("⚠️ Please select a coach.")

        else:

            st.success(
                f"✅ Ticket booked successfully for {name}!"
            )

            st.write("### Booking Details")

            st.write(f"**Passenger:** {name}")
            st.write(f"**Age:** {age}")
            st.write(f"**Gender:** {gender}")
            st.write(f"**Marital Status:** {marital_status}")
            st.write(f"**Coach:** {coach}")
            st.write(f"**Journey Date:** {from_date}")
            st.write(f"**Boarding Time:** {boarding_time}")

            if meal:
                st.write(
                    f"**Meal:** {', '.join(meal)}"
                )

            if rating is not None:
                st.write(f"**Rating:** {rating} ⭐")