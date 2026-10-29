
import streamlit as st
import bank

st.set_page_config(
    page_title="PocketBank",
    page_icon="🏦",
    layout="centered"
)

st.title("PocketBank")
st.caption("A simple banking system built with Python and SQLite.")

st.warning(
    "Educational project only. Do not use real banking credentials or money."
)

# Login session
if "account_no" not in st.session_state:
    st.session_state.account_no = None

# Sidebar navigation
with st.sidebar:
    st.header("Navigation")

    page = st.radio(
        "Select an option",
        ["Home", "Create Account", "Account Dashboard"]
    )

    if st.session_state.account_no:
        st.success("Logged in")
        if st.button("Logout"):
            st.session_state.account_no = None
            st.rerun()


# HOME PAGE
if page == "Home":
    st.subheader("Welcome to PocketBank")

    st.write("""
    Manage your demo bank account through a simple interface.

    - Create an account
    - Deposit money
    - Withdraw money
    - View account details
    - Update your details
    - Delete your account
    """)

    st.info("Select an option from the sidebar to get started.")


# CREATE ACCOUNT PAGE
elif page == "Create Account":
    st.subheader("Create a New Account")

    with st.form("create_form"):
        name = st.text_input("Full Name")
        age = st.number_input(
            "Age", min_value=1, max_value=120, value=18
        )
        email = st.text_input("Email")
        pin = st.text_input("Create PIN", type="password")
        confirm_pin = st.text_input(
            "Confirm PIN", type="password"
        )

        submitted = st.form_submit_button("Create Account")

    if submitted:
        if pin != confirm_pin:
            st.error("PINs do not match.")

        else:
            try:
                account_no = bank.create_account(
                    name, int(age), email, pin
                )

                st.success("Account created successfully!")
                st.write("Your account number is:")
                st.code(account_no)
                st.info("Save this number for future login.")

            except ValueError as error:
                st.error(str(error))


# ACCOUNT DASHBOARD
elif page == "Account Dashboard":

    # LOGIN
    if not st.session_state.account_no:
        st.subheader("Login to Your Account")

        with st.form("login_form"):
            account_no = st.text_input("Account Number")
            pin = st.text_input("PIN", type="password")

            login = st.form_submit_button("Login")

        if login:
            account = bank.authenticate(account_no, pin)

            if account:
                st.session_state.account_no = account["account_no"]
                st.rerun()
            else:
                st.error("Invalid account number or PIN.")

    # LOGGED-IN DASHBOARD
    else:
        account_no = st.session_state.account_no
        account = bank.get_account(account_no)

        if account is None:
            st.session_state.account_no = None
            st.error("Account not found.")
            st.stop()

        st.subheader(f"Welcome, {account['name']}")

        st.metric(
            "Available Balance",
            f"₹{account['balance']:,}"
        )

        st.caption(f"Account No: {account['account_no']}")

        deposit_tab, withdraw_tab, details_tab, update_tab, delete_tab = (
            st.tabs([
                "Deposit",
                "Withdraw",
                "Details",
                "Update",
                "Delete Account"
            ])
        )

        # DEPOSIT
        with deposit_tab:
            with st.form("deposit_form"):
                amount = st.number_input(
                    "Deposit Amount (₹)",
                    min_value=1,
                    value=100,
                    step=100
                )

                deposit_button = st.form_submit_button("Deposit")

            if deposit_button:
                try:
                    balance = bank.deposit(account_no, int(amount))
                    st.success(
                        f"Deposit successful! Balance: ₹{balance:,}"
                    )
                    st.rerun()

                except ValueError as error:
                    st.error(str(error))

        # WITHDRAW
        with withdraw_tab:
            with st.form("withdraw_form"):
                amount = st.number_input(
                    "Withdrawal Amount (₹)",
                    min_value=1,
                    value=100,
                    step=100
                )

                withdraw_button = st.form_submit_button("Withdraw")

            if withdraw_button:
                try:
                    balance = bank.withdraw(
                        account_no, int(amount)
                    )

                    st.success(
                        f"Withdrawal successful! Balance: ₹{balance:,}"
                    )
                    st.rerun()

                except ValueError as error:
                    st.error(str(error))

        # ACCOUNT DETAILS
        with details_tab:
            st.write(f"**Name:** {account['name']}")
            st.write(f"**Age:** {account['age']}")
            st.write(f"**Email:** {account['email']}")
            st.write(f"**Account Number:** {account['account_no']}")
            st.write(f"**Balance:** ₹{account['balance']:,}")

        # UPDATE DETAILS
        with update_tab:
            with st.form("update_form"):
                new_name = st.text_input(
                    "Name", value=account["name"]
                )
                new_email = st.text_input(
                    "Email", value=account["email"]
                )
                new_pin = st.text_input(
                    "New PIN (optional)", type="password"
                )
                confirm_new_pin = st.text_input(
                    "Confirm New PIN", type="password"
                )

                update_button = st.form_submit_button(
                    "Update Details"
                )

            if update_button:
                if new_pin != confirm_new_pin:
                    st.error("PINs do not match.")

                else:
                    try:
                        bank.update_details(
                            account_no,
                            new_name,
                            new_email,
                            new_pin or None
                        )

                        st.success("Details updated successfully.")
                        st.rerun()

                    except ValueError as error:
                        st.error(str(error))

        # DELETE ACCOUNT
        with delete_tab:
            st.error("Account deletion cannot be undone.")

            confirm_delete = st.checkbox(
                "I want to permanently delete my account."
            )

            delete_pin = st.text_input(
                "Enter PIN to confirm deletion",
                type="password"
            )

            if st.button(
                "Delete Account",
                disabled=not confirm_delete
            ):
                verified = bank.authenticate(
                    account_no, delete_pin
                )

                if not verified:
                    st.error("Incorrect PIN.")
                else:
                    bank.delete_account(account_no)
                    st.session_state.account_no = None
                    st.success("Account deleted.")
                    st.rerun()
