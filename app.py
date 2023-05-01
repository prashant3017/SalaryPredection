import pickle
import streamlit as st

BOARD_LIST_10 = [
    'Andhra Pradesh Board',
    'Bihar Board',
    'Central Board of Secondary Education',
    'Uttar Pradesh Board',
    'Haryana Board',
    'Orissa Board',
    'Rajasthan Board',
    'Gujarat Board',
    'Kerala Board',
    'Delhi Board',
    'Chattisgarh Board',
    'Himachal Pradesh Board',
    'Maharashtra Board',
    'Indian Certificate of Secondary Education',
    'Jammu and Kashmir Board',
    'Jharkhand Board',
    'Karnataka Board',
    'Madhya Pradesh Board',
    'Matriculation Board',
    'Nagpur Board',
    'Nashik Board',
    'Pune Board',
    'Punjab Board',
    'Secondary School Certificate',
    'Secondary School of Education',
    'West Bengal Board',
    'Tamil Nadu Board',
    'Uttrakhand Board',
    'Uttaranchal Board',
    'State Board',
    'Board of Secondary Education',
    'Secondary School Certificate',
    'Hyderabad Board',
    'Board of Intermediate Education',
    'Bangalore Board',
    'Dav Public School, Hehal',
    'Indian School Certificate Examination',
    'Kentucky Education Assosication',
    'Upper Arlington Board',
    'Meghalaya Board'
]

BOARD_LIST_12 = ['Central board of secondary education', 'State board', 'Secondary school certificate', 'Haryana board', 'Uttar pradesh board', 'Rajasthan board', 'Andhra pradesh board', 'Karnataka board', 'Board of intermediate education', 'Bangalore board', 'Maharashtra board', 'Indian certificate of secondary education', 'Gujarat board', 'Indian school certificate examination',
                'Tamil nadu board', 'Puc', 'Madhya pradesh board', 'Nagpur board', 'Bihar board', 'Jammu and kashmir board', 'Matriculation board', 'Pu board', 'Ipe', 'Kerala board', 'Board of secondary education', 'Uttrakhand board', 'Sbtet', 'West bengal board', 'Pune board', 'Jharkhand board', 'Uttaranchal board', 'Nios', 'Delhi board', 'Punjab board', 'Pue', 'Himachal pradesh board']

SPECIALIZATION_LIST = ['Instrumentation and control engineering', 'Computer science & engineering', 'Electronics & telecommunications', 'Biotechnology', 'Mechanical engineering', 'Information technology', 'Electronics and communication engineering', 'Computer engineering', 'Computer application', 'Computer science and technology', 'Electrical engineering', 'Automobile/automotive engineering', 'Electronics and electrical engineering', 'Information science engineering', 'Chemical engineering', 'Instrumentation engineering', 'Electronics & instrumentation eng', 'Ceramic engineering', 'Metallurgical engineering', 'Aeronautical engineering', 'Electronics engineering',
                    'Electronics and instrumentation engineering', 'Applied electronics and instrumentation', 'Civil engineering', 'Computer and communication engineering', 'Industrial & production engineering', 'Computer networking', 'Other', 'Electronics and computer engineering', 'Control and instrumentation engineering', 'Mechanical & production engineering', 'Mechanical and automation', 'Industrial & management engineering', 'Biomedical engineering', 'Electrical and power engineering', 'Telecommunication engineering', 'Industrial engineering', 'Mechatronics', 'Embedded systems technology', 'Electronics', 'Information & communication technology', 'Information science']

STATE_LIST = [
    'Delhi',
    'Uttar Pradesh',
    'Maharashtra',
    'Tamil Nadu',
    'Punjab',
    'West Bengal',
    'Telangana',
    'Andhra Pradesh',
    'Harayana',
    'Karantaka',
    'Orissa',
    'Chhattisgarh',
    'Rajashtan',
    'Madhya Pradesh',
    'Uttarakhand',
    'Gujarat',
    'Jharakhand',
    'Himachal Pradesh',
    'Bihar',
    'Union Territory',
    'Jammu and Kashmir',
    'kerala',
    'Assam',
    'Sikkim',
    'Meghalaya',
    'Goa',
]

DEGREE_LIST = [
    "B.Tech/B.E.",
    "M.Tech./M.E.",
    "MCA",
    "M.Sc. (Tech.)"
]


def get_board_10(option):
    BOARD_DICT_10 = {
        "central board of secondary education": 1,
        "indian certificate of secondary education": 2,
        "state board": 3,
        "delhi board": 4,
        "secondary school certificate": 5,
        "haryana board": 6,
        "rajasthan board": 7,
        "uttar pradesh board": 8,
        "west bengal board": 9,
        "matriculation board": 10,
        "andhra pradesh board": 11,
        "madhya pradesh board": 12,
        "karnataka board": 13,
        "kerala board": 14,
        "board of secondary education": 15,
        "gujarat board": 16,
        "maharashtra board": 17,
        "tamil nadu board": 18,
        "nagpur board": 19,
        "bihar board": 20,
        "jammu and kashmir board": 21,
        "secondary school of education": 22,
        "pune board": 23,
        "uttrakhand board": 24,
        "anglo indian": 25,
        "jharkhand board": 26,
        "uttaranchal board": 27,
        "himachal Pradesh board": 28
    }
    for key, value in BOARD_DICT_10.items():
        if option in key:
            return value


def get_board_12(option):
    BOARD_LIST_12 = {
        "central board of secondary education": 1,
        "state board": 2,
        "secondary school certificate": 3,
        "haryana board": 4,
        "uttar pradesh board": 5,
        "rajasthan board": 6,
        "andhra pradesh board": 7,
        "karnataka board": 8,
        "board of intermediate education": 9,
        "bangalore board": 10,
        "maharashtra board": 11,
        "indian certificate of secondary education": 12,
        "gujarat board": 13,
        "indian school certificate examination": 14,
        "tamil nadu board": 15,
        "puc": 16,
        "madhya pradesh board": 17,
        "nagpur board": 18,
        "bihar board": 19,
        "jammu and kashmir board": 20,
        "matriculation board": 21,
        "pu board": 22,
        "ipe": 23,
        "kerala board": 24,
        "board of secondary education": 25,
        "uttrakhand board": 26,
        "sbtet": 27,
        "west bengal board": 28,
        "pune board": 29,
        "jharkhand board": 30,
        "uttaranchal board": 31,
        "nios": 32,
        "delhi board": 33,
        "punjab board": 34,
        "pue": 35,
        "himachal pradesh board": 36
    }
    for key, value in BOARD_LIST_12.items():
        if option in key:
            return value


def get_specialization(option):
    SPECIALIZATION_DICT = {
        "instrumentation and control engineering": 1,
        "computer science & engineering": 2,
        "electronics & telecommunications": 3,
        "biotechnology": 4,
        "mechanical engineering": 5,
        "information technology": 6,
        "electronics and communication engineering": 7,
        "computer engineering": 8,
        "computer application": 9,
        "computer science and technology": 10,
        "electrical engineering": 11,
        "automobile/automotive engineering": 12,
        "electronics and electrical engineering": 13,
        "information science engineering": 14,
        "chemical engineering": 15,
        "instrumentation engineering": 16,
        "electronics & instrumentation eng": 17,
        "ceramic engineering": 18,
        "metallurgical engineering": 19,
        "aeronautical engineering": 20,
        "electronics engineering": 21,
        "electronics and instrumentation engineering": 22,
        "applied electronics and instrumentation": 23,
        "civil engineering": 24,
        "computer and communication engineering": 25,
        "industrial & production engineering": 26,
        "computer networking": 27,
        "other": 28,
        "electronics and computer engineering": 29,
        "control and instrumentation engineering": 30,
        "mechanical & production engineering": 31,
        "mechanical and automation": 32,
        "industrial & management engineering": 33,
        "biomedical engineering": 34,
        "electrical and power engineering": 35,
        "telecommunication engineering": 36,
        "industrial engineering": 37,
        "mechatronics": 38,
        "embedded systems technology": 39,
        "electronics": 40,
        "information & communication technology": 41,
        "information science": 42
    }
    for key, value in SPECIALIZATION_DICT.items():
        if option in key:
            return value


def get_state(option):
    STATE_DICT = {
        'Delhi': 1,
        'Uttar Pradesh': 2,
        'Maharashtra': 3,
        'Tamil Nadu': 4,
        'Punjab': 5,
        'West Bengal': 6,
        'Telangana': 7,
        'Andhra Pradesh': 8,
        'Harayana': 9,
        'Karantaka': 10,
        'Orissa': 11,
        'Chhattisgarh': 12,
        'Rajashtan': 13,
        'Madhya Pradesh': 14,
        'Uttarakhand': 15,
        'Gujarat': 16,
        'Jharakhand': 17,
        'Himachal Pradesh': 18,
        'Bihar': 19,
        'Union Territory': 20,
        'Jammu and Kashmir': 21,
        'kerala': 22,
        'Assam': 23,
        'Sikkim': 24,
        'Meghalaya': 25,
        'Goa': 26,
    }
    for key, value in STATE_DICT.items():
        if option in key:
            return value


def get_degree(option):
    DEGREE_DICT = {
        "B.Tech/B.E.": 1,
        "M.Tech./M.E.": 2,
        "MCA": 3,
        "M.Sc. (Tech.)": 4
    }
    for key, value in DEGREE_DICT.items():
        if option in key:
            return value


def predict_salary(data):
    model = pickle.load(open('random.pkl', 'rb'))
    prediction = model.predict([data])
    return prediction[0]


def main():
    st.title('Salary Prediction App')
    st.markdown('Enter the following details to predict your salary')

    GENDER = [0, 1] if st.selectbox(
        'Gender', ['Male', 'Female']) == 'Male' else [1, 0]
    DOB = st.number_input('Year of Birth', min_value=1985, max_value=2002)
    PERCENTAGE_10 = st.number_input(
        '10th Percentage', min_value=0.0, max_value=100.0, value=0.0)
    BOARD_10 = get_board_10(st.selectbox('10th Board', BOARD_LIST_10).lower())
    GRADUATION_YEAR_12 = st.date_input('12th Passing Year').strftime('%Y')
    PERCENTAGE_12 = st.number_input(
        '12th Percentage', min_value=0.0, max_value=100.0, value=0.0)
    BOARD_12 = get_board_12(st.selectbox('12th Board', BOARD_LIST_12).lower())
    COLLAGE_TIER = 1 if st.selectbox(
        'Collage Tier', ['Tier 1', 'Tier 2']) == 'Tier 1' else 2
    DEGREE = get_degree(st.selectbox('Degree', DEGREE_LIST))
    SPECIALIZATION = get_specialization(st.selectbox(
        'Specialization', SPECIALIZATION_LIST).lower())
    COLLEGE_GPA = st.number_input(
        'College GPA', min_value=5.0, max_value=9.0, value=5.0)
    COLLEGE_STATE = get_state(st.selectbox(
        'College State', STATE_LIST))
    GRADUATION_YEAR = st.date_input('Graduation Year').strftime('%Y')
    ENGLISH_SCORE = st.number_input(
        'English Score', min_value=0.0, max_value=1000.0, value=0.0)
    LOGICAL_SCORE = st.number_input(
        'Logical Score', min_value=0.0, max_value=1000.0, value=0.0)
    QUANT_SCORE = st.number_input(
        'Quant Score', min_value=0.0, max_value=1000.0, value=0.0)
    DOMAIN_SCORE = st.number_input(
        'Domain Score', min_value=0.0, max_value=1.0, value=0.0)
    COMPUTER_PROGRAMMING_SCORE = st.number_input(
        'Computer Programming Score', min_value=0.0, max_value=1000.0, value=0.0)
    ELECTRONICS_AND_COMMUNICATION_SCORE = st.number_input(
        'Electronics and Communication Score', min_value=0.0, max_value=1000.0, value=0.0)
    COMPUTER_SCIENCE_SCORE = st.number_input(
        'Computer Science Score', min_value=0.0, max_value=1000.0, value=0.0)
    MECHANICAL_SCORE = st.number_input(
        'Mechanical Score', min_value=0.0, max_value=1000.0, value=0.0)
    ELECTRICAL_SCORE = st.number_input(
        'Electrical Score', min_value=0.0, max_value=1000.0, value=0.0)
    TELECOMMUNICATION_SCORE = st.number_input(
        'Telecommunication Score', min_value=0.0, max_value=1000.0, value=0.0)
    CIVIL_SCORE = st.number_input(
        'Civil Score', min_value=0.0, max_value=1000.0, value=0.0)
    CONSCIENTIOUSNESS = st.number_input(
        'Conscientiousness', min_value=-10.0, max_value=10.0, value=0.0)
    AGREEABLENESS = st.number_input(
        'Agreeableness', min_value=-10.0, max_value=10.0, value=0.0)
    EXTRAVERTED = st.number_input(
        'Extraversion', min_value=-10.0, max_value=10.0, value=0.0)
    NERVOUS = st.number_input(
        'Nervous', min_value=-10.0, max_value=10.0, value=0.0)
    OPENNESS = st.number_input(
        'Openness', min_value=-10.0, max_value=10.0, value=0.0)

    data = [
        DOB, PERCENTAGE_10, GRADUATION_YEAR_12, PERCENTAGE_12, COLLAGE_TIER, COLLEGE_GPA, ENGLISH_SCORE, LOGICAL_SCORE, QUANT_SCORE, DOMAIN_SCORE, COMPUTER_PROGRAMMING_SCORE, ELECTRONICS_AND_COMMUNICATION_SCORE, COMPUTER_SCIENCE_SCORE, MECHANICAL_SCORE, ELECTRICAL_SCORE, TELECOMMUNICATION_SCORE, CIVIL_SCORE, CONSCIENTIOUSNESS, AGREEABLENESS, EXTRAVERTED, NERVOUS, OPENNESS, GENDER[0], GENDER[1], 0, 0, 1, 0, 0, BOARD_10, BOARD_12, DEGREE, COLLEGE_STATE, SPECIALIZATION, GRADUATION_YEAR
    ]

    if st.button('Predict'):
        result = predict_salary(data)
        st.success(f'Your salary is ₹{round(result, 2)}')

if __name__ == '__main__':
    main()
