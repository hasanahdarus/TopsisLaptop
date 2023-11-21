def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS data(author TEXT,title TEXT,article TEXT,postdate DATE)')

def add_data(laptopName, brandName, diskType, durability, graphicCard, newPrice, processors, ram, screenResolution, screenSize, secondPrice, storage, weight):
    c.execute('INSERT INTO blogtable(author TEXT,title,article,postdate) VALUES (?,?,?,?)',(author,title,postdate))
    conn.commit()

def view_all_notes():
    c.execute('SELECT * FROM blogtable')
    data = c.fetchall()
    return data

def main():
    st.tittle("CRUD")

    menu = ["Home","View Posts","Add Post","Search","Manege Blog"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
        result = view_all_notes()
        st.write(result)
    
    elif choice == "View Posts":
        st.subheader("View Articles")
        create_table()
        blog_author = st.text_input("Enter Author Name",max_change=50)
        blog_title = st.text_input("Enter Post Title")
        blog_article = st.text_area("Post Article Here",height=50)
        blog_post_date = st.date_input("Date")
        if st.button("Add"):
            add_data(blog_author,blog_title,blog_article,blog_post_date)
            st.success("Post:{} saved".format)(blog_title)

    elif choice == "Add Posts":
        st.subheader("Add Articles")

    elif choice == "Search ":
        st.subheader("Search Articles")

    elif choice == "Manage Blog":
        st.subheader("Manage Blog")