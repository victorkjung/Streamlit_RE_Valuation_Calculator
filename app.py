import streamlit as st

def calculate_grm(price: float, gross_rent: float):
    if gross_rent != 0:
        return price / gross_rent
    else:
        return 0

def calculate_cap_rate(net_income: float, price: float):
    if price != 0:
        return (net_income / price) * 100
    else:
        return 0

st.title('RE :classical_building: Valuation :chart_with_upwards_trend: Calculator')

# Add description and developer info to the sidebar
st.sidebar.markdown('## About this App')
st.sidebar.markdown('''
This app is a real estate valuation calculator. 
It allows users to calculate the Gross Rent Multiplier (GRM) and Capitalization Rate (Cap Rate) 
for a property based on various inputs such as price, gross rental income, and various expenses.
''')

st.sidebar.markdown('## Instructions')
st.sidebar.markdown('''
1. Enter the property's price.
2. Enter the gross annual rental income.
3. Enter the annual expenses: Mortgage, Real Estate Taxes, Water & Sewer, Utilities, Insurance, Maintenance, Repairs, Management Fees, Other Expenses.
4. Click on the "Calculate" button to get the GRM and Cap Rate.
''')

st.sidebar.markdown('## About the Developer')
st.sidebar.markdown('''
**Victor Jung** is a serial entrepreneur and technology hobbyist. 
With a passion for innovation and problem-solving, Victor has successfully launched and managed multiple ventures. 
He combines business acumen with a deep understanding of technology to create impactful solutions.

The real estate valuation Calculator was developed by Victor Jung using **PyCharm**, a powerful integrated development environment (IDE), 
and **GitHub Co-Pilot**, an AI-powered coding assistant. 
This collaboration helped streamline the programming process, resulting in efficient code generation and error correction.
''')

price = st.number_input("Enter the property's price", min_value=0.0, step=0.01)
gross_rent = st.number_input("Enter the gross annual rental income", min_value=0.0, step=0.01)

st.header('Enter Annual Operating Expenses ($)')
mortgage = st.number_input("Mortgage", min_value=0.0, step=0.01)
re_taxes = st.number_input("Real Estate Taxes", min_value=0.0, step=0.01)
water_sewer = st.number_input("Water & Sewer", min_value=0.0, step=0.01)
utilities = st.number_input("Utilities", min_value=0.0, step=0.01)
insurance = st.number_input("Insurance", min_value=0.0, step=0.01)
maintenance = st.number_input("Maintenance", min_value=0.0, step=0.01)
repairs = st.number_input("Repairs", min_value=0.0, step=0.01)
management_fees = st.number_input("Management Fees", min_value=0.0, step=0.01)
other_expenses = st.number_input("Other Expenses", min_value=0.0, step=0.01)

total_expenses = mortgage + re_taxes + water_sewer + utilities + insurance + maintenance + repairs + management_fees + other_expenses
st.write(f'Total Operating Expenses: **${total_expenses:,.2f}**')

if st.button('**Calculate**'):
    grm = calculate_grm(price, gross_rent)
    net_income = gross_rent - total_expenses
    cap_rate = calculate_cap_rate(net_income, price)

    st.write(f'<h4>The GRM (Gross Rent Multiplier) of this property is: {grm:,.2f}</h4>', unsafe_allow_html=True)
    st.write(f'<h4>The Cap Rate of this property is: {cap_rate:.2f}%</h4>', unsafe_allow_html=True)

    # Provide a purchase recommendation based on Cap Rate
    if cap_rate < 6.00:
        st.write('<h3> Not &#x1F622; worth it to purchase in today\'s environment &#x1F4C9;.</h3>', unsafe_allow_html=True)
    elif cap_rate >= 6.00:
        st.write('<h3>Buy &#x2705; it all day &#x1F60E; long!</h3>', unsafe_allow_html=True)
