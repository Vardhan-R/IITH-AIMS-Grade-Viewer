from pages.common.decryption import decrypt_file
import streamlit as st
import os

if "view_grades_exists" not in st.session_state:
    st.session_state["view_grades_exists"] = os.path.exists("./pages/runtime/view_grades.py")
if not st.session_state["view_grades_exists"]:
    view_grades_contents = decrypt_file("./pages/common/view_grades.py.enc", st.secrets["vg_key"]).decode()
    os.makedirs("./pages/runtime", exist_ok=True)
    with open("./pages/runtime/view_grades.py", 'w') as fp:
        fp.write(view_grades_contents)
    st.session_state["view_grades_exists"] = True

st.set_page_config("View my Grades")
st.title("View my Grades")

grade_viewer_tab, help_tab = st.tabs(["Grade viewer", "Help"])

with grade_viewer_tab:
    cookie = grade_viewer_tab.text_input("`JSESSIONID` cookie", type="password")

    if cookie:
        from pages.runtime.view_grades import view_grades
        view_grades(cookie, grade_viewer_tab)

with help_tab:
    help_tab.subheader("Obtaining the Cookie")
    help_tab.markdown("""
                    1. Log in to [the AIMS website](https://aims.iith.ac.in/aims/).

                    2. Follow the steps in the image below to obtain the `JSESSIONID` cookie.

                    3. Make sure that the cookie doesn't expire (don't log out, nor get logged out of the AIMS website).
                    """
                )
    help_tab.image("./images/JSESSIONID_cookie.png", "Obtaining the `JSESSIONID` cookie.")
