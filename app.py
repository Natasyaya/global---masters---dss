# ==================================================
# GLOBAL MASTERS DSS
# PART 1
# IMPORT + CONFIG + CSS + DATA
# ==================================================

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="GLOBAL MASTERS DSS",
    page_icon="🎓",
    layout="wide"
)

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

/* MAIN */
.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #111827
    );
}

/* SIDEBAR */
section[data-testid="stSidebar"]{
    background:#111827;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* TITLE */
h1,h2,h3,h4,h5,h6{
    color:#98FFCC !important;
}

/* TEXT */
p, label, div{
    color:white;
}

/* CARD */
.card{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.1);
    min-height:220px;
}

/* GOLD HIGHLIGHT */
.gold{
    color:#FFD700;
    font-weight:bold;
}

/* METRIC */
[data-testid="metric-container"]{
    background:rgba(255,255,255,0.05);
    border-radius:15px;
    padding:15px;
}

/* TABLE */
thead tr th{
    color:#FFD700 !important;
}

tbody tr td{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# DATA NEGARA
# ==================================================

data = {

"Country":[

# ASIA
"Japan",
"South Korea",
"Singapore",
"China",
"Malaysia",
"Thailand",
"Indonesia",
"India",

# EUROPE
"Germany",
"Netherlands",
"Sweden",
"Finland",
"Norway",
"France",
"United Kingdom",

# NORTH AMERICA
"Canada",
"United States",
"Mexico",

# SOUTH AMERICA
"Brazil",
"Argentina",

# AFRICA
"South Africa",
"Egypt",

# OCEANIA
"Australia",
"New Zealand"

],

"Continent":[

# ASIA
"Asia","Asia","Asia","Asia",
"Asia","Asia","Asia","Asia",

# EUROPE
"Europe","Europe","Europe",
"Europe","Europe","Europe",
"Europe",

# NORTH AMERICA
"North America",
"North America",
"North America",

# SOUTH AMERICA
"South America",
"South America",

# AFRICA
"Africa",
"Africa",

# OCEANIA
"Oceania",
"Oceania"

],

"Tuition":[

5000,6500,8000,4500,
3500,3000,2500,2800,

0,2500,0,0,0,3500,9000,

7000,15000,3000,

2500,2000,

3500,1800,

12000,9000

],

"LivingCost":[

1200,1100,1800,900,
850,750,650,700,

1100,1300,1200,1100,
1300,1200,1600,

1400,1800,800,

700,650,

750,600,

1700,1500

],

"Scholarship":[

85,80,82,75,
70,65,60,68,

90,84,92,93,
91,80,78,

88,76,60,

58,55,

65,50,

86,84

],

"Safety":[

90,88,92,75,
78,72,70,65,

89,87,94,95,
96,80,82,

88,75,60,

58,55,

65,62,

90,92

],

"Employment":[

88,85,90,80,
78,70,68,72,

90,88,86,84,
85,82,87,

86,90,62,

60,58,

64,55,

88,84

],

"Research":[

92,88,86,82,
70,65,60,75,

94,88,90,92,
91,85,93,

88,95,60,

58,55,

62,50,

90,84

],

"Certainty":[

69,70,76,73,
90,77,79,80,

81,82,91,74,
75,76,75,

78,72,74,

77,76,

70,78,

85,84

],

"Risk":[

60,62,75,70,
89,78,80,82,

81,83,90,74,
75,77,76,

82,70,72,

78,75,

68,79,

85,83

],

"Uncertainty":[

70,72,83,80,
85,83,89,88,

87,90,92,78,
80,77,76,

80,72,75,

81,79,

70,82,

85,84

]

}

df = pd.DataFrame(data)

# ==================================================
# SESSION STATE
# ==================================================

if "selected_continent" not in st.session_state:
    st.session_state.selected_continent = "Asia"

if "selected_country" not in st.session_state:
    st.session_state.selected_country = "Japan"

if "scholarship_w" not in st.session_state:
    st.session_state.scholarship_w = 80

if "safety_w" not in st.session_state:
    st.session_state.safety_w = 90

if "employment_w" not in st.session_state:
    st.session_state.employment_w = 80

if "research_w" not in st.session_state:
    st.session_state.research_w = 75

if "cost_w" not in st.session_state:
    st.session_state.cost_w = 70
    # ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("GLOBAL MASTERS DSS")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🌍 Region Selection",
        "📊 Country Insights",
        "⚙ Decision Preferences",
        "📈 Decision Environment",
        "🧠 DSS Calculation",
        "🏆 Recommendation",
        "🎓 Universities",
        "ℹ About"
    ]
)

# ==================================================
# HOME
# ==================================================

if menu == "🏠 Home":

    st.title("GLOBAL MASTERS DSS")

    st.caption(
        "Decision Support System for International Master's Study"
    )

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/World_map_-_low_resolution.svg/1280px-World_map_-_low_resolution.svg.png",
        use_container_width=True
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("Objective")

        st.write(
            """
            Assist students in selecting
            the most suitable country for
            postgraduate study using
            multiple decision indicators.
            """
        )

    with col2:

        st.subheader("Method")

        st.write(
            """
            Region Selection

            ↓

            Country Evaluation

            ↓

            DSS Calculation

            ↓

            Recommendation
            """
        )

    with col3:

        st.subheader("Indicators")

        st.write(
            """
            • Scholarship

            • Safety

            • Employment

            • Research

            • Tuition Fee

            • Living Cost
            """
        )

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Countries",
            len(df)
        )

    with c2:
        st.metric(
            "Continents",
            df["Continent"].nunique()
        )

    with c3:
        st.metric(
            "Indicators",
            10
        )

    with c4:
        st.metric(
            "Method",
            "DSS"
        )

    st.markdown("---")

    st.subheader(
        "Decision Environment Overview"
    )

    a, b, c, d = st.columns(4)

    with a:
        st.info(
            "Certainty\n\nPredictable outcomes."
        )

    with b:
        st.warning(
            "Risk\n\nKnown probabilities."
        )

    with c:
        st.error(
            "Uncertainty\n\nFuture difficult to predict."
        )

    with d:
        st.success(
            "Probability\n\nChance of success."
        )
        # ==================================================
# REGION SELECTION
# ==================================================

elif menu == "🌍 Region Selection":

    st.title("Region Selection")

    st.write(
        """
        Select the continent you would like
        to explore for your master's study.
        """
    )

    continent = st.selectbox(
        "Choose Continent",
        sorted(df["Continent"].unique())
    )

    st.session_state.selected_continent = continent

    filtered = df[
        df["Continent"] == continent
    ]

    st.success(
        f"{len(filtered)} countries available in {continent}"
    )

    st.dataframe(
        filtered[["Country"]],
        use_container_width=True
    )

# ==================================================
# COUNTRY INSIGHTS
# ==================================================

elif menu == "📊 Country Insights":

    st.title("Country Insights")

    continent = st.session_state.selected_continent

    filtered = df[
        df["Continent"] == continent
    ]

    country = st.selectbox(
        "Select Country",
        filtered["Country"]
    )

    st.session_state.selected_country = country

    row = filtered[
        filtered["Country"] == country
    ].iloc[0]

    st.subheader(country)

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Tuition Fee",
            f"${row['Tuition']:,}/year"
        )

        if row["Tuition"] < 5000:
            st.success("Low tuition fee")
        elif row["Tuition"] < 10000:
            st.info("Moderate tuition fee")
        else:
            st.warning("High tuition fee")

    with c2:

        st.metric(
            "Living Cost",
            f"${row['LivingCost']:,}/month"
        )

        if row["LivingCost"] < 1000:
            st.success("Affordable living cost")
        elif row["LivingCost"] < 1500:
            st.info("Moderate living cost")
        else:
            st.warning("High living cost")

    st.markdown("---")

    a, b, c, d = st.columns(4)

    with a:
        st.metric(
            "Scholarship",
            row["Scholarship"]
        )

    with b:
        st.metric(
            "Safety",
            row["Safety"]
        )

    with c:
        st.metric(
            "Employment",
            row["Employment"]
        )

    with d:
        st.metric(
            "Research",
            row["Research"]
        )

    st.markdown("---")

    st.subheader(
        "Indicator Explanation"
    )

    st.write(
        """
        Scholarship:
        Availability of funding opportunities.

        Safety:
        Security and quality of life.

        Employment:
        Career opportunities after graduation.

        Research:
        Research capability and innovation strength.
        """
    )

    st.markdown("---")

    chart_df = pd.DataFrame({

        "Indicator":[
            "Scholarship",
            "Safety",
            "Employment",
            "Research"
        ],

        "Score":[
            row["Scholarship"],
            row["Safety"],
            row["Employment"],
            row["Research"]
        ]

    })

    fig = px.bar(
        chart_df,
        x="Indicator",
        y="Score",
        text="Score"
    )

    fig.update_layout(
        title="Country Performance Overview",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==================================================
# DECISION PREFERENCES
# ==================================================

elif menu == "⚙ Decision Preferences":

    st.title("Decision Preferences")

    st.write("""
    Set the importance level of each indicator.
    Higher values mean greater influence on the
    final recommendation.
    """)

    scholarship_w = st.slider(
        "Scholarship",
        0, 100,
        st.session_state.scholarship_w
    )

    safety_w = st.slider(
        "Safety",
        0, 100,
        st.session_state.safety_w
    )

    employment_w = st.slider(
        "Employment",
        0, 100,
        st.session_state.employment_w
    )

    research_w = st.slider(
        "Research",
        0, 100,
        st.session_state.research_w
    )

    cost_w = st.slider(
        "Cost",
        0, 100,
        st.session_state.cost_w
    )

    st.session_state.scholarship_w = scholarship_w
    st.session_state.safety_w = safety_w
    st.session_state.employment_w = employment_w
    st.session_state.research_w = research_w
    st.session_state.cost_w = cost_w

    st.success(
        "Preferences saved successfully."
    )

# ==================================================
# DECISION ENVIRONMENT
# ==================================================

elif menu == "📈 Decision Environment":

    st.title("Decision Environment")

    country = st.session_state.selected_country

    row = df[
        df["Country"] == country
    ].iloc[0]

    st.subheader(
        f"Decision Environment: {country}"
    )

    a,b,c = st.columns(3)

    with a:

        st.metric(
            "Certainty",
            row["Certainty"]
        )

        if row["Certainty"] >= 81:
            st.success("Excellent")
        elif row["Certainty"] >= 61:
            st.info("High")
        elif row["Certainty"] >= 41:
            st.warning("Moderate")
        else:
            st.error("Low")

    with b:

        st.metric(
            "Risk",
            row["Risk"]
        )

        if row["Risk"] >= 81:
            st.success("High Risk")
        elif row["Risk"] >= 61:
            st.info("Moderate Risk")
        else:
            st.warning("Low Risk")

    with c:

        st.metric(
            "Uncertainty",
            row["Uncertainty"]
        )

        if row["Uncertainty"] >= 81:
            st.error("High Uncertainty")
        elif row["Uncertainty"] >= 61:
            st.warning("Moderate Uncertainty")
        else:
            st.success("Low Uncertainty")

    st.markdown("---")

    probability = round(
        (
            row["Certainty"]
            +
            (100-row["Risk"])
            +
            (100-row["Uncertainty"])
        ) / 3,
        2
    )

    st.metric(
        "Probability of Study Success",
        f"{probability}%"
    )

    st.markdown("---")

    st.subheader(
        "Score Interpretation"
    )

    st.write("""

    81 - 100 : Excellent

    61 - 80 : High

    41 - 60 : Moderate

    21 - 40 : Low

    0 - 20 : Very Low

    """)

    env_df = pd.DataFrame({

        "Indicator":[
            "Certainty",
            "Risk",
            "Uncertainty",
            "Probability"
        ],

        "Score":[
            row["Certainty"],
            row["Risk"],
            row["Uncertainty"],
            probability
        ]

    })

    fig = px.bar(
        env_df,
        x="Indicator",
        y="Score",
        text="Score"
    )

    fig.update_layout(
        title="Decision Environment Analysis",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    # ==================================================
# DSS CALCULATION
# ==================================================

elif menu == "🧠 DSS Calculation":

    st.title("DSS Calculation")

    country = st.session_state.selected_country

    row = df[
        df["Country"] == country
    ].iloc[0]

    # ==========================================
    # ACADEMIC & FINANCIAL
    # ==========================================

    scholarship = row["Scholarship"]
    safety = row["Safety"]
    employment = row["Employment"]
    research = row["Research"]

    cost_score = 100 - (

        (
            row["Tuition"]/15000
        )*50

        +

        (
            row["LivingCost"]/2000
        )*50

    )

    sw = st.session_state.scholarship_w
    sf = st.session_state.safety_w
    ew = st.session_state.employment_w
    rw = st.session_state.research_w
    cw = st.session_state.cost_w

    academic_df = pd.DataFrame({

        "Criteria":[

            "Scholarship",
            "Safety",
            "Employment",
            "Research",
            "Cost"

        ],

        "Score":[

            scholarship,
            safety,
            employment,
            research,
            round(cost_score,2)

        ],

        "Weight":[

            sw,
            sf,
            ew,
            rw,
            cw

        ]

    })

    academic_df["Weighted Score"] = (

        academic_df["Score"]

        *

        academic_df["Weight"]

    )

    academic_score = round(

        academic_df["Weighted Score"].sum()

        /

        academic_df["Weight"].sum(),

        2

    )

    st.subheader(
        "Academic & Financial Factors"
    )

    st.dataframe(
        academic_df,
        use_container_width=True
    )

    st.success(
        f"Academic Score : {academic_score}"
    )

    st.markdown("---")

    # ==========================================
    # DECISION ENVIRONMENT
    # ==========================================

    certainty = row["Certainty"]

    risk = row["Risk"]

    uncertainty = row["Uncertainty"]

    risk_adjustment = (
        100-risk
    )

    probability = round(

        (

            certainty

            +

            (100-risk)

            +

            (100-uncertainty)

        ) / 3,

        2

    )

    env_df = pd.DataFrame({

        "Criteria":[

            "Certainty",

            "Risk Adjustment",

            "Uncertainty",

            "Probability"

        ],

        "Score":[

            certainty,

            risk_adjustment,

            uncertainty,

            probability

        ],

        "Weight":[

            70,

            70,

            70,

            80

        ]

    })

    env_df["Weighted Score"] = (

        env_df["Score"]

        *

        env_df["Weight"]

    )

    env_score = round(

        env_df["Weighted Score"].sum()

        /

        env_df["Weight"].sum(),

        2

    )

    st.subheader(
        "Decision Environment Factors"
    )

    st.dataframe(
        env_df,
        use_container_width=True
    )

    st.success(
        f"Decision Environment Score : {env_score}"
    )

    st.markdown("---")

    # ==========================================
    # FINAL DSS
    # ==========================================

    final_dss = round(

        (

            academic_score

            +

            env_score

        ) / 2,

        2

    )

    st.subheader(
        "Final DSS Result"
    )

    c1,c2,c3 = st.columns(3)

    with c1:

        st.metric(
            "Academic Score",
            academic_score
        )

    with c2:

        st.metric(
            "Environment Score",
            env_score
        )

    with c3:

        st.metric(
            "Final DSS Score",
            final_dss
        )

    st.info("""

Final DSS Score is calculated using:

1. Academic & Financial Factors

2. Decision Environment Factors

The final score is obtained by combining
both components equally.

""")

# ==================================================
# RECOMMENDATION
# ==================================================

elif menu == "🏆 Recommendation":

    st.title(
        "Final Recommendation"
    )

    region = st.session_state.selected_continent

    temp = df[
        df["Continent"] == region
    ].copy()

    sw = st.session_state.scholarship_w
    sf = st.session_state.safety_w
    ew = st.session_state.employment_w
    rw = st.session_state.research_w
    cw = st.session_state.cost_w

    # ======================================
    # COST SCORE
    # ======================================

    temp["CostScore"] = 100 - (

        (
            temp["Tuition"]/15000
        )*50

        +

        (
            temp["LivingCost"]/2000
        )*50

    )

    # ======================================
    # ACADEMIC SCORE
    # ======================================

    temp["AcademicScore"] = (

        temp["Scholarship"]*sw

        +

        temp["Safety"]*sf

        +

        temp["Employment"]*ew

        +

        temp["Research"]*rw

        +

        temp["CostScore"]*cw

    ) / (

        sw+sf+ew+rw+cw

    )

    # ======================================
    # ENVIRONMENT SCORE
    # ======================================

    temp["RiskAdjustment"] = (

        100-temp["Risk"]

    )

    temp["Probability"] = (

        temp["Certainty"]

        +

        (100-temp["Risk"])

        +

        (100-temp["Uncertainty"])

    ) / 3

    temp["EnvironmentScore"] = (

        temp["Certainty"]*70

        +

        temp["RiskAdjustment"]*70

        +

        temp["Uncertainty"]*70

        +

        temp["Probability"]*80

    ) / (

        70+70+70+80

    )

    # ======================================
    # FINAL DSS
    # ======================================

    temp["DSS Score"] = (

        temp["AcademicScore"]

        +

        temp["EnvironmentScore"]

    ) / 2

    ranking = temp.sort_values(

        "DSS Score",

        ascending=False

    )

    st.subheader(
        f"Top Recommendations in {region}"
    )

    top5 = ranking.head(5)

    st.dataframe(

        top5[
            [
                "Country",
                "AcademicScore",
                "EnvironmentScore",
                "DSS Score"
            ]
        ],

        use_container_width=True

    )

    best = ranking.iloc[0]

    st.success(f"""

🥇 Recommended Country

{best['Country']}

Final DSS Score:
{round(best['DSS Score'],2)}

""")

    st.session_state.best_country = (
        best["Country"]
    )
    # ==================================================
# UNIVERSITIES
# ==================================================

elif menu == "🎓 Universities":

    st.title("Recommended Universities")

    continent = st.session_state.selected_continent

    st.subheader(
        f"Top Universities in {continent}"
    )

    universities = {

        "Asia":[

            {
                "name":"National University of Singapore (NUS)",
                "location":"Singapore",
                "achievement":"QS World Top 10 University",
                "scholarship":"NUS Graduate Scholarship, ASEAN Scholarship",
                "field":"Data Science, Statistics, Computer Science, Business Analytics"
            },

            {
                "name":"University of Tokyo",
                "location":"Japan",
                "achievement":"Leading Research University in Asia",
                "scholarship":"MEXT Scholarship, JASSO Scholarship",
                "field":"Engineering, Economics, Artificial Intelligence"
            },

            {
                "name":"KAIST",
                "location":"South Korea",
                "achievement":"Top Technology University in Asia",
                "scholarship":"KAIST International Scholarship",
                "field":"Data Science, Technology, Engineering"
            }

        ],

        "Europe":[

            {
                "name":"Technical University of Munich (TUM)",
                "location":"Germany",
                "achievement":"Top Engineering University in Europe",
                "scholarship":"DAAD Scholarship",
                "field":"Engineering, Artificial Intelligence, Data Science"
            },

            {
                "name":"LMU Munich",
                "location":"Germany",
                "achievement":"World-Class Research Institution",
                "scholarship":"DAAD Scholarship",
                "field":"Statistics, Economics, Mathematics"
            },

            {
                "name":"University of Amsterdam",
                "location":"Netherlands",
                "achievement":"Top European Research University",
                "scholarship":"Amsterdam Excellence Scholarship",
                "field":"Data Analytics, Social Science, Business"
            }

        ],

        "North America":[

            {
                "name":"University of Toronto",
                "location":"Canada",
                "achievement":"Highest Ranked University in Canada",
                "scholarship":"Lester B. Pearson Scholarship",
                "field":"Statistics, Data Science, Artificial Intelligence"
            },

            {
                "name":"University of British Columbia (UBC)",
                "location":"Canada",
                "achievement":"Global Research Excellence",
                "scholarship":"International Scholars Program",
                "field":"Computer Science, Analytics, Mathematics"
            },

            {
                "name":"McGill University",
                "location":"Canada",
                "achievement":"Leading Research University",
                "scholarship":"McGill Entrance Scholarship",
                "field":"Statistics, Economics, Public Policy"
            }

        ],

        "South America":[

            {
                "name":"University of São Paulo",
                "location":"Brazil",
                "achievement":"Top University in Latin America",
                "scholarship":"International Mobility Scholarship",
                "field":"Statistics, Economics, Engineering"
            },

            {
                "name":"Pontifical Catholic University of Chile",
                "location":"Chile",
                "achievement":"Leading Research University",
                "scholarship":"International Graduate Scholarship",
                "field":"Data Analytics, Business, Technology"
            },

            {
                "name":"University of Buenos Aires",
                "location":"Argentina",
                "achievement":"Prestigious Public University",
                "scholarship":"International Student Support Program",
                "field":"Economics, Statistics, Social Science"
            }

        ],

        "Africa":[

            {
                "name":"University of Cape Town",
                "location":"South Africa",
                "achievement":"Highest Ranked University in Africa",
                "scholarship":"UCT International Scholarship",
                "field":"Data Science, Economics, Public Health"
            },

            {
                "name":"Stellenbosch University",
                "location":"South Africa",
                "achievement":"Strong Research Performance",
                "scholarship":"International Merit Scholarship",
                "field":"Statistics, Agriculture, Engineering"
            },

            {
                "name":"Cairo University",
                "location":"Egypt",
                "achievement":"Leading University in North Africa",
                "scholarship":"International Graduate Scholarship",
                "field":"Technology, Economics, Mathematics"
            }

        ],

        "Oceania":[

            {
                "name":"University of Melbourne",
                "location":"Australia",
                "achievement":"Top University in Australia",
                "scholarship":"Melbourne Graduate Scholarship",
                "field":"Statistics, Data Science, Business Analytics"
            },

            {
                "name":"University of Sydney",
                "location":"Australia",
                "achievement":"World Top Research University",
                "scholarship":"Sydney International Scholarship",
                "field":"Economics, Computer Science, Analytics"
            },

            {
                "name":"Monash University",
                "location":"Australia",
                "achievement":"Global Top 100 University",
                "scholarship":"Monash International Scholarship",
                "field":"Artificial Intelligence, Statistics, Data Science"
            }

        ]

    }

    for uni in universities[continent]:

        st.markdown("---")

        st.subheader(
            f"🎓 {uni['name']}"
        )

        st.write(
            f"📍 Location : {uni['location']}"
        )

        st.write(
            f"🏆 Achievement : {uni['achievement']}"
        )

        st.write(
            f"🎁 Scholarship : {uni['scholarship']}"
        )

        st.write(
            f"🔬 Strength Area : {uni['field']}"
        )
        st.markdown("---")

st.subheader("Developer Information")

st.markdown("""

Global Masters DSS is an interactive Decision Support System
designed to assist prospective students in selecting the most
suitable country for pursuing an international master's degree.

The system integrates academic, financial, and decision
environment indicators, including scholarship opportunities,
safety, employment prospects, research performance, certainty,
risk, uncertainty, and probability. By combining these factors,
the dashboard provides personalized recommendations that support
more informed and objective decision making.

This project was developed as part of the Decision Support System
course and demonstrates the application of multi-criteria decision
analysis in educational planning.

""")

st.info("""

**Developer**

Linda Natasya Siahaan

Statistics Study Program

Faculty of Mathematics and Natural Sciences

Universitas Negeri Medan

Academic Year 2025/2026

Course: Decision Support System

""")