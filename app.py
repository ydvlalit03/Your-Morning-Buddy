import streamlit as st
import random
from application import temperature_of_city, get_news, news_summarizer, smart_plan

# --- Page Configuration ---

# --- Helper Functions ---
def get_random_quote():
    quotes = [
        "Passionate professional with a background in Artificial Intelligence. Proud Yadav, committed to excellence and growth.",
        "Rooted in Yadav values, driven by ambition. Believing in hard work and the power of dreams.",
        "Expert in Yadav traditions and occasional shenanigans. Life’s too short to be serious all the time!",
        "फौलादी सीना अहीरों का हिमालय की अकड़ रखते हैं पसंद नहीं हमें जंग हार ना हम जीत पर पकड़ रखते हैं! #जय यदुवंश",
        "Dedicated Yadav Entrepreneur 🚀 | Driving innovation in Artificial Intelligence | Committed to excellence and growth | Let’s connect and achieve greatness together 🌟",
        "Rao Sahab ka jazba kabhi thakta nahi, mushkilein chahe jitni bhi badi ho, iraade usse bade hote hain.",
        "Swag and self-respect — both are written in Rao Sahab’s blood.",
        "Rao Sahab may fall, but he never stays down — every setback writes a new victory."
    ]
    return random.choice(quotes)

def get_random_image():
    image_urls = [
        "https://m.media-amazon.com/images/I/31joMgqjFEL._AC_UF894,1000_QL80_.jpg",
        "https://a10.gaanacdn.com/gn_img/albums/d41WjnWPLq/1Wj1ggNn3P/size_m.jpg",
        "https://i.ytimg.com/vi/NBf5u9p53HU/sddefault.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgWZA3Bi2yLHhMa4T1yB8vq7QFYdxo4oxidw&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQf7MWVrFjqqmS34ew8IgC69zDUSNw62Fi14w&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhNiiKlDD6XopZIV0go-z3_beAgZddZmDX6Q&s"
    ]
    return random.choice(image_urls)


# --- Page Definitions ---

def home_page():
    """Displays the home page with a quote and image."""
    st.title("☀️ Your Morning Buddy")
    st.markdown("---")
    st.subheader("A Thought for Your Day")
    st.info(f'"{get_random_quote()}"')
    st.image(get_random_image(), caption="A beautiful morning to start your day", use_container_width=True)
    st.markdown("---")
    st.write("Use the sidebar on the left to get your daily updates!")

def weather_news_page():
    """Displays the page for getting weather and news by city."""
    st.header("Get Weather of the city")
    city = st.text_input("Enter your city name:")

    if st.button("Fetch Information"):
        if city:
            temperature_output= temperature_of_city(city)
            st.subheader(f"Weather Info: {temperature_output}")
            st.success("Weather  fetched successfully!!!!")
        else:
            st.error("Please enter a city name.")

def interest_news_page():
    """Displays the page for getting news by interest."""
    st.header("Get News Based on Your Interests")
    interest = st.text_input("Enter your area of interest (e.g., Technology, Sports, Health):", "Technology")

    if st.button("Fetch News"):
        if interest:
            articles= get_news(interest)
            title=[]
            url=[]
            image_url=[]
            for i in articles:
                title.append(i["title"])
                url.append(i['url'])
                image_url.append(i["urlToImage"])

            if not articles:
                st.error("No news found.")
            col1, col2, col3, col4, col5= st.columns(5)
            with col1:
                st.subheader(title[0])
                st.markdown("---")
                st.image(image_url[0])
                st.markdown("---")
                st.write("Read full article here.", url[0])
                st.markdown("---")
                st.write(news_summarizer(url[0]))

            with col2:
                st.subheader(title[1])
                st.markdown("---")
                st.image(image_url[1])
                st.markdown("---")
                st.write("Read full article here.", url[1])
                st.markdown("---")
                st.write(news_summarizer(url[1]))


            with col3:
                st.subheader(title[2])
                st.markdown("---")
                st.image(image_url[2])
                st.markdown("---")
                st.write("Read full article here.", url[2])
                st.markdown("---")
                st.write(news_summarizer(url[2]))


            with col4:
                st.subheader(title[3])
                st.markdown("---")
                st.image(image_url[3])
                st.markdown("---")
                st.write("Read full article here.", url[3])
                st.markdown("---")
                st.write(news_summarizer(url[3]))


            with col5:
                st.subheader(title[4])
                st.markdown("---")
                st.image(image_url[4])
                st.markdown("---")
                st.write("Read full article here.", url[4])
                st.markdown("---")
                st.write(news_summarizer(url[4]))

        else:
            st.error("Please enter an area of interest")


def smart_planner():
    """Displays the page for viewing the day's schedule."""
    st.header("Your Smart Planner Day")
    city = st.text_input("Enter your city name:")
    if st.button("Let's Plan"):
        if city:
            smart_plans= smart_plan(city)
            st.subheader(smart_plans)
            st.success("Have a nice day.")
        else:
            st.error("Please enter  a  city name")


# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
st.sidebar.markdown("---")
page_option = st.sidebar.radio("Choose a page:", ("Home", "Get Weather of your City", "News by Interest", "Smart Planner"))
st.sidebar.markdown("---")


# --- Page Routing ---
if page_option == "Home":
    home_page()
elif page_option == "Get Weather of your City":
    weather_news_page()
elif page_option == "News by Interest":
    interest_news_page()
elif page_option == "Smart Planner":
    smart_planner()